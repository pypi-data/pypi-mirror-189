# Copyright (C) Evan Goetz (2021)
#
# This file is part of pyDARM.
#
# pyDARM is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# pyDARM is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# pyDARM. If not, see <https://www.gnu.org/licenses/>.

import numpy as np
from scipy import signal

from .utils import compute_digital_filter_response, digital_delay_filter
from .model import Model


class PcalModel(Model):
    """
    A photon calibrator (pcal) model object

    The class serves to return transfer functions that
    are important to the pcal system, be it corrections
    to the response when pulling the PCAL channels from
    the frames, or establishing force coefficients.

    """

    def __init__(self, config):
        super().__init__(config, measurement='pcal')

    def pcal_dewhiten_response(self, frequencies):
        """
        Compute the dewhitening response

        Parameters
        ----------
        frequencies : `float`, array-like
            array of frequencies to compute the response

        Returns
        -------
        tf : `complex128`, array-like
            transfer function response of the Pcal dewhitening filter

        """

        filt = signal.ZerosPolesGain(
            [], -2.0*np.pi*np.asarray(self.pcal_dewhiten),
            np.prod(-2.0*np.pi*np.asarray(self.pcal_dewhiten)))

        return signal.freqresp(filt, 2.0*np.pi*frequencies)[1]

    def compute_pcal_correction(self, frequencies, endstation=False,
                                include_dewhitening=True):
        """
        Compute the Pcal correction for the offline analysis
        See G1501518
        NOTE: This also includes the Pcal arm sign, so be aware!

        Parameters
        ----------
        frequencies : `float`, array-like
            array of frequencies to compute the response
        endstation : `bool`, optional
            When false (default), the correction is computed for CAL-CS
            PCAL channel, which includes 1 16k clock cycle delay that we must
            compensate (undo). Otherwise, when true, the correction is computed
            at the end station, which does not include 1 16k clock cycle delay
        include_dewhitening : `bool`, optional
            if the dewhitening filter is on (default), then the correction will
            include the two 1 Hz poles

        Returns
        -------
        tf : `complex128`, array-like
            transfer function response of the correction

        """

        pcal_sign = self.ref_pcal_2_darm_act_sign

        pcal_dewhitening = 1
        if include_dewhitening:
            pcal_dewhitening = self.pcal_dewhiten_response(frequencies)

        pcal_analog_aa = self.analog_aa_or_ai_filter_response(frequencies)
        # As per the Pcal correction factor shown in G1501518, the front end
        # Pcal calibration already takes into account any analog AA gain
        # (if there is any). Therefore, we don't need the analog AA gain
        # to be included in the pcal correction factor
        pcal_analog_aa_hi_f = pcal_analog_aa / \
            np.abs(self.analog_aa_or_ai_filter_response(1e-2))

        pcal_digital_aa = self.digital_aa_or_ai_filter_response(frequencies)

        # delay filter for end station to CALCS otherwise no delay is used
        # in the correction factor
        if endstation is False:
            end_to_calcs_response = (
                signal.dfreqresp(digital_delay_filter(1, 2**14),
                                 2.0*np.pi*frequencies/2**14)[1])
        else:
            end_to_calcs_response = 1

        return (pcal_sign *
                pcal_dewhitening /
                (pcal_analog_aa_hi_f * pcal_digital_aa) /
                end_to_calcs_response)

    def digital_filter_response(self, frequencies):
        """
        Importing suspension filter from FOTON file which normalized by whitening
          filter 2 1Hz poles (susnorm) and mpN_DC gain.

        Parameters
        ----------
        frequencies : `float`, array-like
            array of frequencies to compute the response

        Returns
        -------
        tf : `complex128`, array-like
            transfer function response of the correction

        """

        response = np.ones(len(frequencies), dtype='complex128')
        for n in range(len(self.pcal_filter_modules_in_use)):
            if n == 0:
                tf, pfilt = compute_digital_filter_response(
                    self.dpath(self.pcal_filter_file),
                    self.pcal_filter_bank,
                    self.pcal_filter_modules_in_use[n],
                    self.pcal_filter_gain, frequencies, pfilt=None)
            else:
                tf = compute_digital_filter_response(
                    self.dpath(self.pcal_filter_file),
                    self.pcal_filter_bank,
                    self.pcal_filter_modules_in_use[n],
                    self.pcal_filter_gain, frequencies, pfilt=pfilt)[0]
            response *= tf

        return response
