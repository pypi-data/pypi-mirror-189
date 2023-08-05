import datetime
import json

import numpy as np
import pytest
import skimage.measure as skime
from astropy.io import fits
from dkist_data_simulator.dataset import key_function
from dkist_data_simulator.spec122 import Spec122Dataset
from dkist_header_validator import spec122_validator
from dkist_header_validator.translator import translate_spec122_to_spec214_l0
from dkist_processing_common._util.scratch import WorkflowFileSystem
from dkist_processing_common.tests.conftest import FakeGQLClient
from dkist_processing_pac.fitter.fitter_parameters import PolcalDresserParameters
from dkist_processing_pac.input_data.drawer import Drawer
from dkist_processing_pac.input_data.dresser import Dresser
from dkist_processing_pac.optics.calibration_unit import CalibrationUnit
from dkist_processing_pac.optics.telescope import Telescope

from dkist_processing_visp.models.tags import VispTag
from dkist_processing_visp.parsers.visp_l0_fits_access import VispL0FitsAccess
from dkist_processing_visp.tasks.background_light import BackgroundLightCalibration
from dkist_processing_visp.tests.conftest import VispConstantsDb
from dkist_processing_visp.tests.conftest import VispTestingParameters
from dkist_processing_visp.tests.conftest import WavelengthParameter


@pytest.fixture(scope="session")
def background_full_beam_shape() -> tuple[int, int]:
    """
    One-stop shop for adjusting the shape used for testing.

    Bigger takes longer and doesn't add much
    """
    return (100, 3)


@pytest.fixture(scope="session")
def background_testing_parameters(background_full_beam_shape) -> VispTestingParameters:
    # We do this like this so it can depend on the full_beam_shape fixture for the beam border

    num_wave = background_full_beam_shape[0]
    cont_idx = list(range(num_wave // 2))
    return VispTestingParameters(
        visp_background_num_spatial_bins=WavelengthParameter(values=(1, 1, 1, 1)),
        visp_background_wavelength_subsample_factor=WavelengthParameter(values=(20, 20, 20, 20)),
        visp_background_num_fit_iterations=WavelengthParameter(values=(10, 10, 10, 10)),
        visp_background_continuum_index=WavelengthParameter(
            values=(cont_idx, cont_idx, cont_idx, cont_idx)
        ),
        visp_beam_border=num_wave,
    )


@pytest.fixture(scope="session")
def background_testing_parameters_switch_off() -> VispTestingParameters:
    return VispTestingParameters(
        visp_background_on=False,
        visp_background_num_spatial_bins=WavelengthParameter(values=(1, 1, 1, 1)),
        visp_background_wavelength_subsample_factor=WavelengthParameter(values=(20, 20, 20, 20)),
        visp_background_num_fit_iterations=WavelengthParameter(values=(10, 10, 10, 10)),
        visp_background_continuum_index=WavelengthParameter(values=(1, 1, 1, 1)),
        visp_beam_border=2,
    )


@pytest.fixture(scope="session")
def background_light(background_full_beam_shape) -> np.ndarray:
    num_wave, num_spatial = background_full_beam_shape
    beam1 = np.arange(num_wave) * 10.0 + 2
    beam2 = np.arange(num_wave) * 2.0 + 10

    full_frame = np.ones((1, num_wave * 2, num_spatial))
    full_frame[:, :num_wave, :] *= beam1[None, :, None]
    full_frame[:, num_wave:, :] *= beam2[None, :, None]

    return full_frame


## Copied from dkist-processing-pac because we need a real-looking CS
class CalibrationSequenceStepDataset(Spec122Dataset):
    def __init__(
        self,
        array_shape: tuple[int, ...],
        time_delta: float,
        pol_status: str,
        pol_theta: float,
        ret_status: str,
        ret_theta: float,
        dark_status: str,
        instrument: str = "visp",
        num_mod: int = 3,
        start_time: str | datetime.datetime | None = None,
    ):
        self.num_mod = num_mod

        # Make up a Calibration sequence. Mostly random except for two clears and two darks at start and end, which
        # we want to test
        self.pol_status = pol_status
        self.pol_theta = pol_theta
        self.ret_status = ret_status
        self.ret_theta = ret_theta
        self.dark_status = dark_status
        dataset_shape = (self.num_mod,) + array_shape[1:]
        super().__init__(
            dataset_shape, array_shape, time_delta, instrument=instrument, start_time=start_time
        )
        self.add_constant_key("DKIST004", "polcal")
        self.add_constant_key("WAVELNTH", 854.0)

    @key_function("VISP_011")
    def modstate(self, key: str) -> int:
        return (self.index % self.num_mod) + 1

    @key_function("VISP_010")
    def nummod(self, key: str) -> int:
        return self.num_mod

    @key_function("PAC__004")
    def polarizer_status(self, key: str) -> str:
        return self.pol_status

    @key_function("PAC__005")
    def polarizer_angle(self, key: str) -> str:
        return "none" if self.pol_status == "clear" else str(self.pol_theta)

    @key_function("PAC__006")
    def retarter_status(self, key: str) -> str:
        return self.ret_status

    @key_function("PAC__007")
    def retarder_angle(self, key: str) -> str:
        return "none" if self.ret_status == "clear" else str(self.ret_theta)

    @key_function("PAC__008")
    def gos_level3_status(self, key: str) -> str:
        return self.dark_status


@pytest.fixture(scope="session")
def cs_with_correct_geometry():
    dark_status = [
        "DarkShutter",
        "FieldStop (5arcmin)",
        "FieldStop (5arcmin)",
        "FieldStop (5arcmin)",
        "FieldStop (5arcmin)",
        "FieldStop (5arcmin)",
        "FieldStop (5arcmin)",
        "FieldStop (5arcmin)",
        "FieldStop (5arcmin)",
        "FieldStop (5arcmin)",
        "FieldStop (5arcmin)",
        "FieldStop (5arcmin)",
        "FieldStop (5arcmin)",
        "DarkShutter",
    ]
    ret_theta = [0, 0, 0, 0, 0, 0, 60, 120, 30, 90, 150, 0, 0, 0]
    ret_status = [
        "clear",
        "clear",
        "clear",
        "clear",
        "clear",
        "SiO2 SAR",
        "SiO2 SAR",
        "SiO2 SAR",
        "SiO2 SAR",
        "SiO2 SAR",
        "SiO2 SAR",
        "SiO2 SAR",
        "clear",
        "clear",
    ]
    pol_theta = [0, 0, 0, 60, 120, 0, 0, 0, 45, 45, 45, 45, 0, 0]
    pol_status = [
        "clear",
        "clear",
        "Sapphire Polarizer",
        "Sapphire Polarizer",
        "Sapphire Polarizer",
        "Sapphire Polarizer",
        "Sapphire Polarizer",
        "Sapphire Polarizer",
        "Sapphire Polarizer",
        "Sapphire Polarizer",
        "Sapphire Polarizer",
        "Sapphire Polarizer",
        "clear",
        "clear",
    ]
    data_shape = (1, 1, 1)
    num_steps = len(pol_theta)
    out_dict = dict()
    start_time = datetime.datetime.fromisoformat("2022-05-25T12:00:00")
    for n in range(num_steps):
        ds = CalibrationSequenceStepDataset(
            array_shape=(1, 2, 2),
            time_delta=2.0,
            pol_status=pol_status[n],
            pol_theta=pol_theta[n],
            ret_status=ret_status[n],
            ret_theta=ret_theta[n],
            dark_status=dark_status[n],
            start_time=start_time,
            num_mod=10,
        )
        header_list = [
            spec122_validator.validate_and_translate_to_214_l0(
                d.header(), return_type=fits.HDUList
            )[0].header
            for d in ds
        ]
        hdu_list = []
        for m in range(ds.num_mod):
            hdu_list.append(
                fits.PrimaryHDU(
                    data=np.ones(data_shape) * 1e3, header=fits.Header(header_list.pop(0))
                )
            )

        out_dict[n] = [VispL0FitsAccess(h, auto_squeeze=False) for h in hdu_list]
        start_time = ds.start_time + datetime.timedelta(seconds=60)

    return out_dict, data_shape


@pytest.fixture(scope="session")
def visp_modulation_matrix() -> np.ndarray:
    # Modulation matrix for AdW's synthetic ViSP data from mod_matrix_630.out
    return np.array(
        [
            [1.0, 0.19155013, 0.80446989, -0.47479524],
            [1.0, -0.65839661, 0.68433984, 0.00466389],
            [1.0, -0.80679413, -0.16112977, 0.48234158],
            [1.0, -0.04856211, -0.56352868, 0.77578117],
            [1.0, 0.56844858, 0.03324473, 0.77289873],
            [1.0, 0.19155013, 0.80446989, 0.47479524],
            [1.0, -0.65839661, 0.68433984, -0.00466389],
            [1.0, -0.80679413, -0.16112977, -0.48234158],
            [1.0, -0.04856211, -0.56352868, -0.77578117],
            [1.0, 0.56844858, 0.03324473, -0.77289873],
        ],
        dtype=np.float64,
    )


@pytest.fixture(scope="session")
def fully_realistic_cs(
    cs_with_correct_geometry, visp_modulation_matrix, background_light
) -> dict[int, list[VispL0FitsAccess]]:

    fit_mode = "use_M12"
    init_set = "OCCal_VIS"
    cs_dict, data_shape = cs_with_correct_geometry
    dresser = Dresser()
    dresser.add_drawer(Drawer(cs_dict, skip_darks=False))
    CM = CalibrationUnit(dresser)
    TM = Telescope(dresser)
    full_params = PolcalDresserParameters(dresser, fit_mode, init_set)

    global_params = full_params.init_params._all_parameters[0]
    pardict = global_params.valuesdict()
    CM.load_pars_from_dict(pardict)
    TM.load_pars_from_dict(pardict)

    CM.I_sys[0] = 1e4

    # Has shape (4, N)
    S = np.sum((TM.TM @ CM.CM @ TM.M12) * CM.S_in[:, None, :], axis=2).T

    # Has shape (M, N)
    observed = visp_modulation_matrix @ S

    # Now set the "observed" value for each of the input objects
    for m in range(dresser.nummod):
        for n in range(dresser.numsteps):
            full_data = (
                np.ones(background_light.shape) * observed[m, n] / np.mean(cs_dict[n][m].data)
            )
            cs_dict[n][m].data = full_data + background_light

    return cs_dict


@pytest.fixture(scope="function")
def background_light_calibration_task(
    tmp_path,
    assign_input_dataset_doc_to_task,
    init_visp_constants_db,
    recipe_run_id,
    fully_realistic_cs,
    background_full_beam_shape,
    background_testing_parameters,
):
    constants_db = VispConstantsDb(
        SOLAR_EXPOSURE_TIMES=(10.0,),
        OBSERVE_EXPOSURE_TIMES=(10.0,),
        POLCAL_EXPOSURE_TIMES=(10.0,),
        NUM_CS_STEPS=len(fully_realistic_cs),
    )
    init_visp_constants_db(recipe_run_id, constants_db)
    with BackgroundLightCalibration(
        recipe_run_id=recipe_run_id,
        workflow_name="background_light_calibration",
        workflow_version="vX.Y",
    ) as task:
        number_of_beams = 2
        try:  # This try... block is here to make sure the dbs get cleaned up if there's a failure in the fixture
            task.scratch = WorkflowFileSystem(
                scratch_base_path=tmp_path, recipe_run_id=recipe_run_id
            )
            assign_input_dataset_doc_to_task(task, background_testing_parameters)

            dark_cal = np.zeros(background_full_beam_shape)
            # Need a dark for each beam
            for b in range(number_of_beams):
                task.intermediate_frame_helpers_write_arrays(
                    arrays=dark_cal, beam=b + 1, task="DARK", exposure_time=10.0
                )

            # Now write polcal frames
            num_steps = len(fully_realistic_cs)
            num_mod = len(fully_realistic_cs[0])
            total_polcal_files = num_mod * num_steps
            num_dark_polcal_files = num_mod * 2
            for n in range(num_steps):
                for m in range(num_mod):
                    hdu = fully_realistic_cs[n][m]._hdu
                    translated_header = translate_spec122_to_spec214_l0(hdu.header)
                    hdul = fits.HDUList(
                        [fits.PrimaryHDU(data=hdu.data, header=fits.Header(translated_header))]
                    )
                    task.fits_data_write(
                        hdu_list=hdul,
                        tags=[
                            VispTag.input(),
                            VispTag.task("POLCAL"),
                            VispTag.modstate(m + 1),
                            VispTag.cs_step(n),
                            VispTag.exposure_time(10.0),
                            VispTag.frame(),
                        ],
                    )
            yield task, total_polcal_files, num_dark_polcal_files
        except:
            raise
        finally:
            task.scratch.purge()
            task.constants._purge()


@pytest.fixture(scope="function")
def background_light_calibration_task_with_bad_exposure_times(
    tmp_path,
    assign_input_dataset_doc_to_task,
    init_visp_constants_db,
    recipe_run_id,
    background_testing_parameters,
):
    constants_db = VispConstantsDb(
        SOLAR_EXPOSURE_TIMES=(1.0,),
        OBSERVE_EXPOSURE_TIMES=(10.0,),
        POLCAL_EXPOSURE_TIMES=(100.0,),
    )
    init_visp_constants_db(recipe_run_id, constants_db)
    with BackgroundLightCalibration(
        recipe_run_id=recipe_run_id,
        workflow_name="background_light_calibration",
        workflow_version="vX.Y",
    ) as task:
        try:  # This try... block is here to make sure the dbs get cleaned up if there's a failure in the fixture
            task.scratch = WorkflowFileSystem(
                scratch_base_path=tmp_path, recipe_run_id=recipe_run_id
            )
            assign_input_dataset_doc_to_task(task, background_testing_parameters)
            yield task
        except:
            raise
        finally:
            task.scratch.purge()
            task.constants._purge()


@pytest.fixture(scope="function")
def background_light_calibration_task_non_polarimetric_dataset(
    tmp_path,
    assign_input_dataset_doc_to_task,
    init_visp_constants_db,
    recipe_run_id,
    background_testing_parameters,
):
    constants_db = VispConstantsDb(
        SOLAR_EXPOSURE_TIMES=(10.0,),
        OBSERVE_EXPOSURE_TIMES=(10.0,),
        POLCAL_EXPOSURE_TIMES=(10.0,),
        POLARIMETER_MODE="observe_intensity",
    )
    init_visp_constants_db(recipe_run_id, constants_db)
    with BackgroundLightCalibration(
        recipe_run_id=recipe_run_id,
        workflow_name="background_light_calibration",
        workflow_version="vX.Y",
    ) as task:
        try:  # This try... block is here to make sure the dbs get cleaned up if there's a failure in the fixture
            task.scratch = WorkflowFileSystem(
                scratch_base_path=tmp_path, recipe_run_id=recipe_run_id
            )
            assign_input_dataset_doc_to_task(task, background_testing_parameters)
            yield task
        except:
            raise
        finally:
            task.scratch.purge()
            task.constants._purge()


@pytest.fixture(scope="session")
def dummy_array() -> np.ndarray:
    return np.random.random((100, 2560))


def test_background_light_calibration_task(
    background_light_calibration_task, background_light, mocker
):
    """
    Give: a BackgroundLightCalibrationTask with a valid set of polcal data
    When: running the task
    Then: BACKGROUND intermediate frames are generated for each beam
    """
    mocker.patch(
        "dkist_processing_common.tasks.mixin.metadata_store.GraphQLClient", new=FakeGQLClient
    )
    task, total_polcal_files, num_dark_polcal_files = background_light_calibration_task
    task()

    beam_1_bg = list(task.read(tags=[VispTag.beam(1), VispTag.task("BACKGROUND")]))
    assert len(beam_1_bg) == 1
    assert beam_1_bg[0].exists()

    beam_2_bg = list(task.read(tags=[VispTag.beam(2), VispTag.task("BACKGROUND")]))
    assert len(beam_2_bg) == 1
    assert beam_2_bg[0].exists()

    quality_record = list(task.read(tags=[VispTag.quality("TASK_TYPES")]))
    assert len(quality_record) == 1
    with open(quality_record[0], "r") as f:
        data = json.load(f)
        assert data["task_type"] == "BACKGROUND"
        assert data["total_frames"] == total_polcal_files - num_dark_polcal_files
        assert data["frames_not_used"] == 0

    # We don't currently test the actual accuracy of the calibration. We might never want to do this
    # beam_1_data = fits.open(beam_1_bg[0])[0].data
    # np.testing.assert_array_equal(beam_1_data, background_light[0, :1000, :])
    # beam_2_data = fits.open(beam_2_bg[0])[0].data
    # np.testing.assert_array_equal(beam_2_data, background_light[0, 1000:, :])


def test_background_light_bad_exposure_times(
    background_light_calibration_task_with_bad_exposure_times, mocker
):
    """
    Given: A set of data where the polcal exposure times don't match those of solar gain and observe
    When: Trying to run BackgroundLightCalibration
    Then: An error is raised
    """
    mocker.patch(
        "dkist_processing_common.tasks.mixin.metadata_store.GraphQLClient", new=FakeGQLClient
    )
    task = background_light_calibration_task_with_bad_exposure_times
    with pytest.raises(ValueError, match="do not all have the same exposure time"):
        task()


def test_background_light_non_polarimetric_dataset(
    background_light_calibration_task_non_polarimetric_dataset, mocker
):
    """
    Given: A dataset that is non-polarimetric (i.e., Stokes-I only)
    When: Running the BackgroundLightCalibration task
    Then: Nothing is done and no files are written
    """
    mocker.patch(
        "dkist_processing_common.tasks.mixin.metadata_store.GraphQLClient", new=FakeGQLClient
    )
    task = background_light_calibration_task_non_polarimetric_dataset
    task()

    # Test that no BACKGROUND files were created
    beam_1_bg = list(task.read(tags=[VispTag.beam(1), VispTag.task("BACKGROUND")]))
    assert len(beam_1_bg) == 0
    beam_2_bg = list(task.read(tags=[VispTag.beam(2), VispTag.task("BACKGROUND")]))
    assert len(beam_2_bg) == 0


def test_background_light_switch_off(
    background_light_calibration_task,
    assign_input_dataset_doc_to_task,
    background_testing_parameters_switch_off,
    mocker,
):
    """
    Given: A task with the background light switch turned off
    When: Running the BackgroundLightCalibration task
    Then: Nothing is done and no files are written
    """
    mocker.patch(
        "dkist_processing_common.tasks.mixin.metadata_store.GraphQLClient", new=FakeGQLClient
    )
    task, _, _ = background_light_calibration_task
    assign_input_dataset_doc_to_task(task, background_testing_parameters_switch_off)
    task()

    # Test that no BACKGROUND files were created
    beam_1_bg = list(task.read(tags=[VispTag.beam(1), VispTag.task("BACKGROUND")]))
    assert len(beam_1_bg) == 0
    beam_2_bg = list(task.read(tags=[VispTag.beam(2), VispTag.task("BACKGROUND")]))
    assert len(beam_2_bg) == 0


def test_looping_spatial_resample(
    background_light_calibration_task_non_polarimetric_dataset, dummy_array
):
    """
    Given: A 3-dimensional array
    When: Resampling the last dimension with the looping version of block_reduce in BackgroundLightCaibration
    Then: The result is the same as calling the method on the large array all at once
    """
    task = background_light_calibration_task_non_polarimetric_dataset

    spat_block = dummy_array.shape[-1] // task.parameters.background_num_spatial_bins
    expected = skime.block_reduce(dummy_array, block_size=(1, spat_block), func=np.median)
    observed = task.resample_spatial_dimension(
        dummy_array, task.parameters.background_num_spatial_bins
    )

    assert np.array_equal(expected, observed)


def test_looping_spatial_resample_fail_on_bad_bin_param(
    background_light_calibration_task_non_polarimetric_dataset, dummy_array
):
    """
    Given: A 3-dimensional array
    When: Resampling the last dimension with the looping version of block_reduce in BackgroundLightCaibration
    Then: The result is the same as calling the method on the large array all at once
    """
    task = background_light_calibration_task_non_polarimetric_dataset

    bad_bin_number = dummy_array.shape[-1] / 2 + 1

    with pytest.raises(ValueError):
        observed = task.resample_spatial_dimension(dummy_array, bad_bin_number)
