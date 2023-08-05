"""VBI Write L1 task."""
from typing import Literal
from typing import Type

import numpy as np
from astropy.io import fits
from astropy.time import Time
from astropy.time import TimeDelta
from dkist_processing_common.models.constants import ConstantsBase
from dkist_processing_common.tasks.write_l1 import WriteL1Frame

from dkist_processing_vbi.models.constants import VbiConstants
from dkist_processing_vbi.models.spectral_line import VBI_SPECTRAL_LINES


class VbiWriteL1Frame(WriteL1Frame):
    """
    Task class for writing out calibrated L1 VBI frames.

    Parameters
    ----------
    recipe_run_id : int
        id of the recipe run used to identify the workflow run this task is part of
    workflow_name : str
        name of the workflow to which this instance of the task belongs
    workflow_version : str
        version of the workflow to which this instance of the task belongs
    """

    @property
    def constants_model_class(self) -> Type[ConstantsBase]:
        """Supply the correct class so we can access VBI-specific constants."""
        return VbiConstants

    def add_dataset_headers(
        self, header: fits.Header, stokes: Literal["I", "Q", "U", "V"]
    ) -> fits.Header:
        """
        Add the VBI specific dataset headers to L1 FITS files.

        Parameters
        ----------
        header : fits.Header
            calibrated data header

        stokes :
            stokes parameter

        Returns
        -------
        fits.Header
            calibrated header with correctly written l1 headers
        """
        header["DNAXIS"] = 3  # spatial, spatial, temporal
        header["DAAXES"] = 2  # Spatial, spatial
        header["DEAXES"] = 1  # Temporal

        # ---Spatial 1---
        header["DNAXIS1"] = header["NAXIS1"]
        header["DTYPE1"] = "SPATIAL"
        header["DPNAME1"] = "helioprojective latitude"
        header["DWNAME1"] = "helioprojective latitude"
        header["DUNIT1"] = header["CUNIT1"]

        # ---Spatial 2---
        header["DNAXIS2"] = header["NAXIS2"]
        header["DTYPE2"] = "SPATIAL"
        header["DPNAME2"] = "helioprojective longitude"
        header["DWNAME2"] = "helioprojective longitude"
        header["DUNIT2"] = header["CUNIT2"]

        # ---Temporal---
        num_exp_per_dsp = header["VBINFRAM"]
        header["DNAXIS3"] = self.constants.num_dsps_repeats * num_exp_per_dsp
        header["DTYPE3"] = "TEMPORAL"
        header["DPNAME3"] = "time"
        header["DWNAME3"] = "time"
        header["DUNIT3"] = "s"
        # Temporal position in dataset
        current_dsps_repeat = header["DSPSNUM"]
        current_exposure = header["VBICFRAM"]
        header["DINDEX3"] = (
            current_dsps_repeat - 1 - self.constants.dsps_repeat_pedestal
        ) * num_exp_per_dsp + current_exposure

        # ---Wavelength Info---
        # Do we need to check that this has length == 1?
        spectral_line = [l for l in VBI_SPECTRAL_LINES if l.name == self.constants.spectral_line][0]
        header["WAVEMIN"] = spectral_line.wavemin
        header["WAVEMAX"] = spectral_line.wavemax
        header["WAVEBAND"] = spectral_line.name
        header["WAVEUNIT"] = -9  # nanometers
        header["WAVEREF"] = "Air"

        # --- Mosaic ---
        number_of_spatial_steps = int(header["VBINSTP"])
        current_step = int(header["VBISTP"])
        axis_length = int(np.sqrt(number_of_spatial_steps))
        if number_of_spatial_steps not in [1, 4, 9]:  # not a square grid
            raise ValueError(
                f"Mosaic grid must be square or 'sit-and-stare'. "
                f"Number of spatial steps in these data are {number_of_spatial_steps}"
            )
        if number_of_spatial_steps == 4 or 9:  # a 2x2 or 3x3 grid (example for n = 9)
            header["MAXIS"] = 2
            header["MAXIS1"] = axis_length  # ex. 3
            header["MAXIS2"] = axis_length  # ex. 3
            header["MINDEX1"] = int((current_step - 1) % axis_length + 1)  # ex. 1,2,3,1,2,3,1,2,3
            header["MINDEX2"] = int((current_step - 1) // axis_length + 1)  # ex. 1,1,1,2,2,2,3,3,3

        # ---Other info---
        header["LEVEL"] = 1

        # Binning headers
        header["NBIN1"] = 1
        header["NBIN2"] = 1
        header["NBIN3"] = 1
        header["NBIN"] = header["NBIN1"] * header["NBIN2"] * header["NBIN3"]

        return header

    def _calculate_date_end(self, header: fits.Header) -> str:
        """
        Calculate the VBI specific version of the "DATE-END" keyword.

        Parameters
        ----------
        header
            The input fits header

        Returns
        -------
        The isot formatted string of the DATE-END keyword value
        """
        return (
            Time(header["DATE-BEG"], format="isot", precision=6)
            + TimeDelta(float(header["TEXPOSUR"]) / 1000, format="sec")
        ).to_value("isot")
