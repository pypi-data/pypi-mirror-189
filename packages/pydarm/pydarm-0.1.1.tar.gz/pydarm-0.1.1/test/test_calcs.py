import unittest
import pydarm
import numpy as np
import os
import tempfile


class TestOpticalResponseRatio(unittest.TestCase):

    def setUp(self):
        self.frequencies = np.logspace(0, np.log10(5000), 10)
        self.known_ratio = np.array(
            [0.9687610764499911+0.2047970729401173j,
             0.9924685506670072+0.11021624181361893j,
             0.9996996369445023-0.017419284109037984j,
             1.0000395381056308+9.034598303705724e-05j,
             1.0000460037549426-0.0015728765784223393j,
             0.9999143680349047-0.0053037784890201944j,
             0.9995587616354148-0.013435445411127945j,
             1.0028033347285978-0.03182314724508758j,
             1.037094494083799-0.08469882750680675j,
             1.3450148887458857-0.4063843161408741j])

    def tearDown(self):
        del self.frequencies
        del self.known_ratio

    def test_optical_response_ratio(self):
        calcs = pydarm.calcs.CALCSModel('''
[metadata]
[interferometer]
[sensing]
coupled_cavity_optical_gain = 3.22e6
coupled_cavity_pole_frequency = 410.6
detuned_spring_frequency = 4.468
detuned_spring_Q = 52.14
is_pro_spring = True
[calcs]
foton_invsensing_tf = \
  test/2019-04-04_H1CALCS_InverseSensingFunction_Foton_SRCD-2N_Gain_tf.txt
[actuation]
[digital]
''')
        test_ratio = calcs.optical_response_ratio(self.frequencies)
        for n in range(len(self.frequencies)):
            self.assertAlmostEqual(
                np.abs(test_ratio[n]), np.abs(self.known_ratio[n]))
            self.assertAlmostEqual(
                np.angle(test_ratio[n], deg=True),
                np.angle(self.known_ratio[n], deg=True))


class TestSusResponseRatio(unittest.TestCase):

    def setUp(self):
        self.frequencies = np.logspace(0, np.log10(5000), 10)
        self.known_ratio = np.array(
            [0.8487526667231122-0.023180214028295554j,
             1.000634769947796+0.0006302384282468779j,
             1.0005977801588317+0.000363760972346402j,
             1.000597290467924+0.0005874422057399667j,
             1.000637303467556+0.0013777513334851089j,
             1.0009076909644028+0.003498218128442966j,
             1.0027066353202043+0.009016021154521546j,
             1.0148035382784029+0.023637108614939135j,
             1.10165381013647+0.06878863262289596j,
             2.235309261287587+0.5026819806767127j])

    def tearDown(self):
        del self.frequencies
        del self.known_ratio

    def test_sus_response_ratio(self):
        calcs = pydarm.calcs.CALCSModel('''
[metadata]
[interferometer]
[sensing]
[digital]
[actuation_x_arm]
suspension_file = test/H1susdata_O3.mat
[actuation]
[calcs]
xarm_tst_analog = test/H1CALCS_ETMX_L3_ANALOG.txt
''')
        test_ratio = calcs.sus_response_ratio(self.frequencies, arm='x',
                                              stage='tst')
        for n in range(len(self.frequencies)):
            self.assertAlmostEqual(
                np.abs(test_ratio[n]), np.abs(self.known_ratio[n]))
            self.assertAlmostEqual(
                np.angle(test_ratio[n], deg=True),
                np.angle(self.known_ratio[n], deg=True))


class TestGdsSensingCorrection(unittest.TestCase):

    def setUp(self):
        # Pre-computed values
        self.frequencies = np.logspace(0, np.log10(5000.), 10)
        self.known_C_corr = np.array(
            [0.9690020217321972+0.203657344927382j,
             0.9927987606585151+0.10720767543223012j,
             0.9995339485303539-0.025225038758617827j,
             0.9998404602179516-0.020026699699416443j,
             0.9986274137784608-0.053379506643647906j,
             0.9903407804505594-0.13838726788917072j,
             0.9366306937437336-0.3499516632708973j,
             0.6085919368544006-0.7993628642506994j,
             -0.7703535216582147-0.704625047873796j,
             1.0438549765849148-0.4323868901519636j])
        self.known_gds_correction = np.array(
            [0.9883325892921246-0.2077200940000379j,
             0.9956434485655548-0.10751485991908585j,
             0.9998294812828395+0.0252324970597059j,
             0.9997584654376137+0.020025057352554037j,
             0.9985214873445555+0.053373844571182875j,
             0.9904141727779854+0.1383975235141808j,
             0.9368712606521091+0.3500415458577869j,
             0.6029452733652817+0.7919461818617544j,
             -0.7067846031289654+0.6464799871936803j,
             0.8176890307238232+0.3387041543479065j])
        self.model_string = '''
[metadata]
[interferometer]
[sensing]
x_arm_length = 3994.4704
y_arm_length = 3994.4692
coupled_cavity_optical_gain = 3.22e6
coupled_cavity_pole_frequency = 410.6
detuned_spring_frequency = 4.468
detuned_spring_Q = 52.14
sensing_sign = 1
is_pro_spring = True
anti_aliasing_rate_string = 16k
anti_aliasing_method      = biquad
analog_anti_aliasing_file = test/H1aa.mat, test/H1aa.mat
omc_meas_p_trans_amplifier_uncompensated   = 13.7e3, 17.8e3: 13.7e3, 17.8e3
whitening_mode_names = test, test
omc_meas_p_whitening_uncompensated_test   = 11.346e3, 32.875e3, 32.875e3: 11.521e3, 32.863e3, 32.863e3
gain_ratio = 1, 1
balance_matrix = 1, 1
omc_path_names = A, B
single_pole_approximation_delay_correction = -12e-6
super_high_frequency_poles_apparent_delay = 0, 0
adc_gain = 1638.001638001638, 1638.001638001638
omc_filter_file = test/H1OMC_1239468752.txt
omc_filter_bank = OMC_DCPD_A, OMC_DCPD_B
omc_filter_noncompensating_modules = 4: 4
omc_filter_gain = 1, 1
omc_front_end_trans_amplifier_compensation = ON, ON
omc_front_end_whitening_compensation_test = ON, ON
[calcs]
foton_invsensing_tf = \
  test/2019-04-04_H1CALCS_InverseSensingFunction_Foton_SRCD-2N_Gain_tf.txt
[actuation]
[digital]
'''

    def tearDown(self):
        del self.frequencies
        del self.known_gds_correction
        del self.known_C_corr
        del self.model_string

    def test_gds_correction(self):
        """ Test the computation of the GDS correction """
        calcs = pydarm.calcs.CALCSModel(self.model_string)
        gds_corr = calcs.gds_sensing_correction(self.frequencies)
        for n in range(len(self.frequencies)):
            self.assertAlmostEqual(
                np.abs(gds_corr[n]), np.abs(self.known_gds_correction[n]))
            self.assertAlmostEqual(
                np.angle(gds_corr[n], deg=True),
                np.angle(self.known_gds_correction[n], deg=True))
    
    def test_C_corr(self):
        """ Test the computation of C_corr """
        calcs = pydarm.calcs.CALCSModel(self.model_string)
        C_corr = calcs.C_corr(self.frequencies)
        for n in range(len(self.frequencies)):
            self.assertAlmostEqual(
                np.abs(C_corr[n]), np.abs(self.known_C_corr[n]))
            self.assertAlmostEqual(
                np.angle(C_corr[n], deg=True),
                np.angle(self.known_C_corr[n], deg=True))


class TestDrivealignOutToDisplacement(unittest.TestCase):

    def setUp(self):
        self.frequencies = np.logspace(0, np.log10(5000), 10)
        self.model_string = '''
[metadata]
[interferometer]
[digital]
[sensing]
[actuation]
[calcs]
xarm_uim_analog = test/H1CALCS_ETMX_L1_ANALOG.txt
xarm_pum_analog = test/H1CALCS_ETMX_L2_ANALOG.txt
xarm_tst_analog = test/H1CALCS_ETMX_L3_ANALOG.txt
xarm_output_matrix = 0.0, -1.0, -1.0, -1.0
[actuation_x_arm]
tst_NpV2 = 4.427e-11
actuation_esd_bias_voltage = -9.3
tst_driver_DC_gain_VpV_HV = 40
tst_driver_DC_gain_VpV_LV = 1.881
dac_gain = 7.62939453125e-05
pum_driver_DC_trans_ApV = 2.6847e-4
pum_coil_outf_signflip = 1
pum_NpA = 0.02947
uim_driver_DC_trans_ApV = 6.1535e-4
uim_NpA = 1.634
'''
        self.sign_string = "darm_feedback_sign = -1"
        self.known_darm_uim = np.array(
            [-3.238927901844634e-11+1.4842248249648434e-10j,
             -2.1892938228443525e-13-1.2823546638408861e-13j,
             -8.235508683705688e-16+1.1171018557953846e-17j,
             -2.2721027742100763e-18+3.8079469914466563e-20j,
             -7.727346613339272e-21+2.8219414924360876e-22j,
             -3.07022010410702e-23+2.8033962875878643e-24j,
             -3.7049080828781866e-25+8.515053811571386e-26j,
             -5.6541859151817374e-27+2.7786427108167966e-27j,
             -1.5563418053688328e-31+2.6074253026280297e-32j,
             -9.10020413742017e-36-9.112459957053174e-38j])
        self.known_darm_pum = np.array(
            [-5.478095746328349e-13+1.455441816425798e-12j,
             6.167675927515008e-15+3.476345955497267e-16j,
             8.922276848356977e-17+2.2793664015837933e-20j,
             1.93246038703505e-18+1.0535918169326137e-22j,
             4.400980788166467e-20-6.018841093550202e-24j,
             1.0685506817059288e-21-5.042502461408688e-25j,
             4.0817828174035824e-23-6.304119517788214e-26j,
             -2.1494901791827377e-24+3.4968924666365354e-27j,
             -1.512228887834369e-24+1.3001133772698815e-24j,
             7.827471412730521e-30+6.02486971489429e-33j])
        self.known_darm_tst = np.array(
            [2.0597184624425995e-15+8.489735047270597e-15j,
             4.891873116712453e-16+2.492236617170203e-19j,
             6.918623785211078e-17-8.395825629537092e-21j,
             1.03379064938846e-17-5.105213618025428e-21j,
             1.5555470654579614e-18-2.0854170062766784e-21j,
             2.342445539745114e-19-8.1536988350230305e-22j,
             3.522752328873434e-20-3.1653333930430725e-22j,
             5.241125064242745e-21-1.2206599337631032e-22j,
             7.249945048080412e-22-4.5263355007569324e-23j,
             5.1451821428785154e-23-1.1567627817439817e-23j])
        signval = float(self.sign_string.split(' = ')[-1])
        self.known_long_uim = self.known_darm_uim / signval
        self.known_long_pum = self.known_darm_pum / signval
        self.known_long_tst = self.known_darm_tst / signval

    def tearDown(self):
        del self.frequencies
        del self.model_string
        del self.sign_string
        del self.known_darm_uim
        del self.known_darm_pum
        del self.known_darm_tst
        del self.known_long_uim
        del self.known_long_pum
        del self.known_long_tst

    def test_drivealign_out_to_darm_displacement(self):
        calcs = pydarm.calcs.CALCSModel(self.model_string + self.sign_string)
        test_val = calcs.drivealign_out_to_darm_displacement(
            self.frequencies, arm='x', stage='uim')
        for n in range(len(self.frequencies)):
            self.assertAlmostEqual(np.abs(test_val[n]) /
                                   np.abs(self.known_darm_uim[n]), 1)
            self.assertAlmostEqual(np.angle(test_val[n], deg=True),
                                   np.angle(self.known_darm_uim[n], deg=True))
        test_val = calcs.drivealign_out_to_darm_displacement(
            self.frequencies, arm='x', stage='pum')
        for n in range(len(self.frequencies)):
            self.assertAlmostEqual(np.abs(test_val[n]) /
                                   np.abs(self.known_darm_pum[n]), 1)
            self.assertAlmostEqual(np.angle(test_val[n], deg=True),
                                   np.angle(self.known_darm_pum[n], deg=True))
        test_val = calcs.drivealign_out_to_darm_displacement(
            self.frequencies, arm='x', stage='tst')
        for n in range(len(self.frequencies)):
            self.assertAlmostEqual(np.abs(test_val[n]) /
                                   np.abs(self.known_darm_tst[n]), 1)
            self.assertAlmostEqual(np.angle(test_val[n], deg=True),
                                   np.angle(self.known_darm_tst[n], deg=True))

    def test_drivealign_out_to_longitudinal_displacement(self):
        calcs = pydarm.calcs.CALCSModel(self.model_string)
        test_val = calcs.drivealign_out_to_longitudinal_displacement(
            self.frequencies, arm='x', stage='uim')
        for n in range(len(self.frequencies)):
            self.assertAlmostEqual(np.abs(test_val[n]) /
                                   np.abs(self.known_long_uim[n]), 1)
            self.assertAlmostEqual(np.angle(test_val[n], deg=True),
                                   np.angle(self.known_long_uim[n], deg=True))
        test_val = calcs.drivealign_out_to_longitudinal_displacement(
            self.frequencies, arm='x', stage='pum')
        for n in range(len(self.frequencies)):
            self.assertAlmostEqual(np.abs(test_val[n]) /
                                   np.abs(self.known_long_pum[n]), 1)
            self.assertAlmostEqual(np.angle(test_val[n], deg=True),
                                   np.angle(self.known_long_pum[n], deg=True))
        test_val = calcs.drivealign_out_to_longitudinal_displacement(
            self.frequencies, arm='x', stage='tst')
        for n in range(len(self.frequencies)):
            self.assertAlmostEqual(np.abs(test_val[n]) /
                                   np.abs(self.known_long_tst[n]), 1)
            self.assertAlmostEqual(np.angle(test_val[n], deg=True),
                                   np.angle(self.known_long_tst[n], deg=True))


class TestStageSuperActuator(unittest.TestCase):

    def setUp(self):
        self.frequencies = np.logspace(0, np.log10(5000.), 10)
        self.known_actuation = np.array(
            [-5.310569188975287e-15+7.256951812950946e-16j,
             2.373277011838796e-15+5.291008654481964e-16j,
             6.565119740746598e-16-1.9982361183467982e-15j,
             -2.2559506195176175e-16-4.466754954217274e-16j,
             -9.777506975890007e-17-5.640474139960699e-17j,
             -1.862001070553775e-17-2.5901317072945293e-18j,
             -2.5387144596970953e-18+2.087430071154024e-19j,
             -3.6579868747198944e-19+8.64886306967107e-20j,
             -3.031250280475011e-20+4.8441976904940323e-20j,
             -3.257386852647821e-21-2.3520741277934774e-21j])

    def tearDown(self):
        del self.frequencies

    def test_stage_super_actuator(self):
        calcs = pydarm.calcs.CALCSModel('''
[metadata]
[interferometer]
[sensing]
[digital]
[actuation]
darm_output_matrix = 1.0, -1.0, 0.0, 0.0
darm_feedback_x = OFF, OFF, OFF, ON
darm_feedback_y = OFF, OFF, OFF, ON
[actuation_x_arm]
darm_feedback_sign = -1
tst_NpV2 = 4.427e-11
linearization = OFF
actuation_esd_bias_voltage = -9.3
tst_driver_DC_gain_VpV_HV = 40
tst_driver_DC_gain_VpV_LV = 1.881
anti_imaging_rate_string = 16k
anti_imaging_method = biquad
analog_anti_imaging_file = test/H1aa.mat
dac_gain = 7.62939453125e-05
sus_filter_file = test/H1SUSETMX_1236641144.txt
tst_isc_inf_bank = ETMX_L3_ISCINF_L
tst_isc_inf_modules =
tst_isc_inf_gain = 1.0
tst_lock_bank = ETMX_L3_LOCK_L
tst_lock_modules = 5,8,9,10
tst_lock_gain = 1.0
tst_drive_align_bank = ETMX_L3_DRIVEALIGN_L2L
tst_drive_align_modules = 4,5
tst_drive_align_gain = -35.7
pum_lock_bank = ETMX_L2_LOCK_L
pum_lock_modules = 7
pum_lock_gain = 23.0
pum_drive_align_bank = ETMX_L2_DRIVEALIGN_L2L
pum_drive_align_modules = 6,7
pum_drive_align_gain = 1.0
uim_lock_bank = ETMX_L1_LOCK_L
uim_lock_modules = 10
uim_lock_gain = 1.06
uim_drive_align_bank = ETMX_L1_DRIVEALIGN_L2L
uim_drive_align_modules =
uim_drive_align_gain = 1.0
[actuation_y_arm]
darm_feedback_sign = 1
tst_NpV2 = 4.427e-11
linearization = OFF
actuation_esd_bias_voltage = -9.3
tst_driver_DC_gain_VpV_HV = 40
tst_driver_DC_gain_VpV_LV = 1.881
anti_imaging_rate_string = 16k
anti_imaging_method = biquad
analog_anti_imaging_file = test/H1aa.mat
dac_gain = 7.62939453125e-05
sus_filter_file = test/H1SUSETMX_1236641144.txt
tst_isc_inf_bank = ETMX_L3_ISCINF_L
tst_isc_inf_modules =
tst_isc_inf_gain = 1.0
tst_lock_bank = ETMX_L3_LOCK_L
tst_lock_modules = 5,8,9,10
tst_lock_gain = 1.0
tst_drive_align_bank = ETMX_L3_DRIVEALIGN_L2L
tst_drive_align_modules = 4,5
tst_drive_align_gain = -35.7
pum_lock_bank = ETMX_L2_LOCK_L
pum_lock_modules = 7
pum_lock_gain = 23.0
pum_drive_align_bank = ETMX_L2_DRIVEALIGN_L2L
pum_drive_align_modules = 6,7
pum_drive_align_gain = 1.0
uim_lock_bank = ETMX_L1_LOCK_L
uim_lock_modules = 10
uim_lock_gain = 1.06
uim_drive_align_bank = ETMX_L1_DRIVEALIGN_L2L
uim_drive_align_modules =
uim_drive_align_gain = 1.0
[calcs]
xarm_uim_analog = test/H1CALCS_ETMX_L1_ANALOG.txt
xarm_pum_analog = test/H1CALCS_ETMX_L2_ANALOG.txt
xarm_tst_analog = test/H1CALCS_ETMX_L3_ANALOG.txt
xarm_output_matrix = 0.0, -1.0, -1.0, -1.0
yarm_output_matrix = 0.0, -1.0, -1.0, -1.0
yarm_uim_analog = test/H1CALCS_ETMX_L1_ANALOG.txt
yarm_pum_analog = test/H1CALCS_ETMX_L2_ANALOG.txt
yarm_tst_analog = test/H1CALCS_ETMX_L3_ANALOG.txt
''')
        test_val = calcs.stage_super_actuator(self.frequencies)
        for n in range(len(self.frequencies)):
            self.assertAlmostEqual(np.abs(test_val[n]) /
                                   np.abs(self.known_actuation[n]), 1)
            self.assertAlmostEqual(np.angle(test_val[n], deg=True),
                                   np.angle(self.known_actuation[n], deg=True))


class TestGdsActuationCorrection(unittest.TestCase):

    def setUp(self):
        self.frequencies = np.logspace(0, np.log10(5000.), 10)
        self.known_gds_correction = np.array(
            [0.8404967514499294-0.02251279611738371j,
             0.9907095585751328+0.001962094231205677j,
             0.990763975573271+0.003815548705921684j,
             0.9906221600923891+0.009484886231351873j,
             0.9900442501120555+0.024330364567526422j,
             0.9862620650174786+0.06312091048110094j,
             0.962066130652169+0.17047900283578304j,
             0.8316201623443047+0.5299562916258533j,
             -1.1474171691614994-1.6791062999287774j,
             -1083.636852739504+5122.811137621163j])
        self.known_calcs_tst = np.array(
            [-2.6552845944876435e-15+3.628475906475473e-16j,
             1.186638505919398e-15+2.645504327240982e-16j,
             3.282559870373299e-16-9.991180591733991e-16j,
             -1.1279753097588087e-16-2.233377477108637e-16j,
             -4.8887534879450034e-17-2.8202370699803494e-17j,
             -9.310005352768874e-18-1.2950658536472646e-18j,
             -1.2693572298485476e-18+1.043715035577012e-19j,
             -1.8289934373599472e-19+4.324431534835535e-20j,
             -1.5156251402375056e-20+2.4220988452470162e-20j,
             -1.6286934263239104e-21-1.1760370638967387e-21j])
        self.model_string = '''
[metadata]
[interferometer]
[sensing]
[digital]
[actuation_x_arm]
darm_feedback_sign = -1
tst_NpV2 = 4.427e-11
linearization = OFF
actuation_esd_bias_voltage = -9.3
suspension_file = test/H1susdata_O3.mat
tst_driver_uncompensated_Z_UL = 129.7e3
tst_driver_uncompensated_Z_LL = 90.74e3
tst_driver_uncompensated_Z_UR = 93.52e3
tst_driver_uncompensated_Z_LR = 131.5e3
tst_driver_uncompensated_P_UL = 31.5e3
tst_driver_uncompensated_P_LL = 26.7e3
tst_driver_uncompensated_P_UR = 26.6e3
tst_driver_uncompensated_P_LR = 31.6e3
tst_driver_DC_gain_VpV_HV = 40
tst_driver_DC_gain_VpV_LV = 1.881
anti_imaging_rate_string = 16k
anti_imaging_method = biquad
analog_anti_imaging_file = test/H1aa.mat
dac_gain = 7.62939453125e-05
unknown_actuation_delay = 15e-6
pum_driver_DC_trans_ApV = 2.6847e-4
pum_coil_outf_signflip = 1
pum_NpA = 0.02947
uim_driver_DC_trans_ApV = 6.1535e-4
uim_NpA = 1.634
sus_filter_file = test/H1SUSETMX_1236641144.txt
tst_isc_inf_bank = ETMX_L3_ISCINF_L
tst_isc_inf_modules =
tst_isc_inf_gain = 1.0
tst_lock_bank = ETMX_L3_LOCK_L
tst_lock_modules = 5,8,9,10
tst_lock_gain = 1.0
tst_drive_align_bank = ETMX_L3_DRIVEALIGN_L2L
tst_drive_align_modules = 4,5
tst_drive_align_gain = -35.7
pum_lock_bank = ETMX_L2_LOCK_L
pum_lock_modules = 7
pum_lock_gain = 23.0
pum_drive_align_bank = ETMX_L2_DRIVEALIGN_L2L
pum_drive_align_modules = 6,7
pum_drive_align_gain = 1.0
uim_lock_bank = ETMX_L1_LOCK_L
uim_lock_modules = 10
uim_lock_gain = 1.06
uim_drive_align_bank = ETMX_L1_DRIVEALIGN_L2L
uim_drive_align_modules =
uim_drive_align_gain = 1.0
[actuation]
darm_output_matrix = 1.0, -1.0, 0.0, 0.0
darm_feedback_x = OFF, ON, ON, ON
darm_feedback_y = OFF, OFF, OFF, OFF
[calcs]
xarm_tst_analog = test/H1CALCS_ETMX_L3_ANALOG.txt
xarm_output_matrix = 0.0, 0.0, 0.0, -1.0
'''

    def tearDown(self):
        del self.frequencies
        del self.known_gds_correction
        del self.model_string
        del self.known_calcs_tst

    def test_gds_actuation_correction(self):
        calcs = pydarm.calcs.CALCSModel(self.model_string)
        gds_corr = calcs.gds_actuation_correction(self.frequencies,
                                                  stage='TST')
        for n in range(len(self.frequencies)):
            self.assertAlmostEqual(
                np.abs(gds_corr[n]) / np.abs(self.known_gds_correction[n]),
                1.0)
            self.assertAlmostEqual(
                np.angle(gds_corr[n], deg=True),
                np.angle(self.known_gds_correction[n], deg=True))

    def test_compute_actuation_single_stage(self):
        calcs = pydarm.calcs.CALCSModel(self.model_string)
        tst = calcs.compute_actuation_single_stage(self.frequencies,
                                                   arm='x',
                                                   stage='TST')
        for n in range(len(self.frequencies)):
            self.assertAlmostEqual(
                np.abs(tst[n]) / np.abs(self.known_calcs_tst[n]),
                1.0)
            self.assertAlmostEqual(
                np.angle(tst[n], deg=True),
                np.angle(self.known_calcs_tst[n], deg=True))


class TestCalcsDarmActuation(unittest.TestCase):

    def setUp(self):
        self.frequencies = np.logspace(0, np.log10(5000.), 10)
        self.model_string = '''
[metadata]
[interferometer]
[sensing]
[digital]
[actuation]
darm_output_matrix = 1.0, -1.0, 0.0, 0.0
darm_feedback_x = OFF, ON, ON, ON
darm_feedback_y = OFF, OFF, OFF, OFF
[actuation_x_arm]
darm_feedback_sign = -1
tst_NpV2 = 4.427e-11
linearization = OFF
actuation_esd_bias_voltage = -9.3
tst_driver_DC_gain_VpV_HV = 40
tst_driver_DC_gain_VpV_LV = 1.881
anti_imaging_rate_string = 16k
anti_imaging_method = biquad
analog_anti_imaging_file = test/H1aa.mat
dac_gain = 7.62939453125e-05
pum_driver_DC_trans_ApV = 2.6847e-4
pum_coil_outf_signflip = 1
pum_NpA = 0.02947
uim_driver_DC_trans_ApV = 6.1535e-4
uim_NpA = 1.634
sus_filter_file = test/H1SUSETMX_1236641144.txt
tst_isc_inf_bank = ETMX_L3_ISCINF_L
tst_isc_inf_modules =
tst_isc_inf_gain = 1.0
tst_lock_bank = ETMX_L3_LOCK_L
tst_lock_modules = 5,8,9,10
tst_lock_gain = 1.0
tst_drive_align_bank = ETMX_L3_DRIVEALIGN_L2L
tst_drive_align_modules = 4,5
tst_drive_align_gain = -35.7
pum_lock_bank = ETMX_L2_LOCK_L
pum_lock_modules = 7
pum_lock_gain = 23.0
pum_drive_align_bank = ETMX_L2_DRIVEALIGN_L2L
pum_drive_align_modules = 6,7
pum_drive_align_gain = 1.0
uim_lock_bank = ETMX_L1_LOCK_L
uim_lock_modules = 10
uim_lock_gain = 1.06
uim_drive_align_bank = ETMX_L1_DRIVEALIGN_L2L
uim_drive_align_modules =
uim_drive_align_gain = 1.0
[calcs]
xarm_uim_analog = test/H1CALCS_ETMX_L1_ANALOG.txt
xarm_pum_analog = test/H1CALCS_ETMX_L2_ANALOG.txt
xarm_tst_analog = test/H1CALCS_ETMX_L3_ANALOG.txt
xarm_output_matrix = 0.0, -1.0, -1.0, -1.0
'''
        self.known_actuation = np.array(
            [-4.517595087730189e-13-2.574036100879927e-13j,
             -1.588361922503374e-14+6.321091918942617e-15j,
             -2.010750482679724e-15+8.323452747346148e-16j,
             -3.003908484149924e-16+4.0189540926990994e-17j,
             -4.589254777634106e-17+1.7738463389039645e-18j,
             -7.164372681090654e-18-9.924814855271752e-19j,
             -1.2876117069737756e-18+9.59002289638503e-20j,
             -1.8304199780422068e-19+4.3641229060862356e-20j,
             -1.4943625550308623e-20+2.4185781589291237e-20j,
             -1.6286934512050932e-21-1.176037151353447e-21j])

    def tearDown(self):
        del self.frequencies
        del self.model_string
        del self.known_actuation

    def test_calcs_darm_actuation(self):
        calcs = pydarm.calcs.CALCSModel(self.model_string)
        test_actuation = calcs.calcs_darm_actuation(self.frequencies)
        for n in range(len(self.frequencies)):
            self.assertAlmostEqual(
                np.abs((test_actuation[n]) /
                        np.abs(self.known_actuation[n])), 1)
            self.assertAlmostEqual(
                np.angle(test_actuation[n], deg=True),
                np.angle(self.known_actuation[n], deg=True))

    def test_arm_super_actuator(self):
        calcs = pydarm.calcs.CALCSModel(self.model_string)
        test_actuation = calcs.arm_super_actuator(self.frequencies)
        for n in range(len(self.frequencies)):
            self.assertAlmostEqual(
                np.abs((test_actuation[n]) /
                        np.abs(self.known_actuation[n])), 1)
            self.assertAlmostEqual(
                np.angle(test_actuation[n], deg=True),
                np.angle(self.known_actuation[n], deg=True))


class TestACorr(unittest.TestCase):

    def setUp(self):
        self.frequencies = np.logspace(0, np.log10(5000.), 10)
        self.known_correction = np.array(
            [0.8256840102234249+0.040037550804620875j,
             1.0100908537872708-0.03431742186724575j,
             0.9938282915911524+0.0035596494716521737j,
             0.987085789996497+0.007169039492965028j,
             0.9892669716989076+0.02615913560670487j,
             0.9853591419850162+0.06159399166108731j,
             0.9616724418609144+0.17084142887447454j,
             0.8317978218032787+0.529870878348411j,
             -1.152159283662438-1.6878788665759379j,
             -1083.6927058686802+5122.867648656695j])

    def tearDown(self):
        del self.frequencies
        del self.known_correction

    def test_A_corr(self):
        calcs = pydarm.calcs.CALCSModel('''
[metadata]
[interferometer]
[sensing]
[digital]
[actuation]
darm_output_matrix = 1.0, -1.0, 0.0, 0.0
darm_feedback_x = OFF, ON, ON, ON
darm_feedback_y = OFF, OFF, OFF, OFF
[actuation_x_arm]
darm_feedback_sign = -1
tst_NpV2 = 4.427e-11
linearization = OFF
actuation_esd_bias_voltage = -9.3
suspension_file = test/H1susdata_O3.mat
tst_driver_uncompensated_Z_UL = 129.7e3
tst_driver_uncompensated_Z_LL = 90.74e3
tst_driver_uncompensated_Z_UR = 93.52e3
tst_driver_uncompensated_Z_LR = 131.5e3
tst_driver_uncompensated_P_UL = 31.5e3
tst_driver_uncompensated_P_LL = 26.7e3
tst_driver_uncompensated_P_UR = 26.6e3
tst_driver_uncompensated_P_LR = 31.6e3
tst_driver_DC_gain_VpV_HV = 40
tst_driver_DC_gain_VpV_LV = 1.881
anti_imaging_rate_string = 16k
anti_imaging_method = biquad
analog_anti_imaging_file = test/H1aa.mat
dac_gain = 7.62939453125e-05
unknown_actuation_delay = 15e-6
pum_driver_DC_trans_ApV = 2.6847e-4
pum_coil_outf_signflip = 1
pum_NpA = 0.02947
uim_driver_DC_trans_ApV = 6.1535e-4
uim_NpA = 1.634
sus_filter_file = test/H1SUSETMX_1236641144.txt
tst_isc_inf_bank = ETMX_L3_ISCINF_L
tst_isc_inf_modules =
tst_isc_inf_gain = 1.0
tst_lock_bank = ETMX_L3_LOCK_L
tst_lock_modules = 5,8,9,10
tst_lock_gain = 1.0
tst_drive_align_bank = ETMX_L3_DRIVEALIGN_L2L
tst_drive_align_modules = 4,5
tst_drive_align_gain = -35.7
pum_lock_bank = ETMX_L2_LOCK_L
pum_lock_modules = 7
pum_lock_gain = 23.0
pum_drive_align_bank = ETMX_L2_DRIVEALIGN_L2L
pum_drive_align_modules = 6,7
pum_drive_align_gain = 1.0
uim_lock_bank = ETMX_L1_LOCK_L
uim_lock_modules = 10
uim_lock_gain = 1.06
uim_drive_align_bank = ETMX_L1_DRIVEALIGN_L2L
uim_drive_align_modules =
uim_drive_align_gain = 1.0
[calcs]
xarm_uim_analog = test/H1CALCS_ETMX_L1_ANALOG.txt
xarm_pum_analog = test/H1CALCS_ETMX_L2_ANALOG.txt
xarm_tst_analog = test/H1CALCS_ETMX_L3_ANALOG.txt
xarm_output_matrix = 0.0, -1.0, -1.0, -1.0
''')
        test_corr = calcs.A_corr(self.frequencies)
        for n in range(len(self.frequencies)):
            self.assertAlmostEqual(
                np.abs((test_corr[n]) /
                        np.abs(self.known_correction[n])), 1)
            self.assertAlmostEqual(
                np.angle(test_corr[n], deg=True),
                np.angle(self.known_correction[n], deg=True))


class TestSensingActuationDelay(unittest.TestCase):

    def setUp(self):
        self.frequencies = np.logspace(0, np.log10(5000.), 10)
        self.known_delay = np.array(
            [-0.04037604748711977,
             -0.004241732151460522,
             0.0008245861775018065,
             0.00042427948404596266,
             0.0004030354338592999,
             0.0004137083970280847,
             0.0004113912830929018,
             0.0004118062637910283,
             -9.851958730979098e-05,
             4.472355469886113e-05])

    def tearDown(self):
        del self.frequencies

    def test_sensing_actuation_delay(self):
        calcs = pydarm.calcs.CALCSModel('''
[metadata]
[interferometer]
[sensing]
x_arm_length = 3994.4704
y_arm_length = 3994.4692
coupled_cavity_optical_gain = 3.22e6
coupled_cavity_pole_frequency = 410.6
detuned_spring_frequency = 4.468
detuned_spring_Q = 52.14
sensing_sign = 1
is_pro_spring = True
anti_aliasing_rate_string = 16k
anti_aliasing_method      = biquad
analog_anti_aliasing_file = test/H1aa.mat, test/H1aa.mat
omc_meas_p_trans_amplifier_uncompensated   = 13.7e3, 17.8e3: 13.7e3, 17.8e3
whitening_mode_names = test, test
omc_meas_p_whitening_uncompensated_test   = 11.346e3, 32.875e3, 32.875e3: 11.521e3, 32.863e3, 32.863e3
gain_ratio = 1, 1
balance_matrix = 1, 1
omc_path_names = A, B
single_pole_approximation_delay_correction = -12e-6
super_high_frequency_poles_apparent_delay = 0, 0
adc_gain = 1638.001638001638, 1638.001638001638
omc_filter_file = test/H1OMC_1239468752.txt
omc_filter_bank = OMC_DCPD_A, OMC_DCPD_B
omc_filter_noncompensating_modules = 4: 4
omc_filter_gain = 1, 1
omc_front_end_trans_amplifier_compensation = ON, ON
omc_front_end_whitening_compensation_test = ON, ON
[digital]
digital_filter_file = test/H1OMC_1239468752.txt
digital_filter_bank = LSC_DARM1, LSC_DARM2
digital_filter_modules = 1,2,3,4,7,9,10: 3,4,5,6,7
digital_filter_gain = 400,1
[actuation]
darm_output_matrix = 1.0, -1.0, 0.0, 0.0
darm_feedback_x = OFF, ON, ON, ON
darm_feedback_y = OFF, OFF, OFF, OFF
[actuation_x_arm]
darm_feedback_sign = -1
tst_NpV2 = 4.427e-11
linearization = OFF
actuation_esd_bias_voltage = -9.3
suspension_file = test/H1susdata_O3.mat
tst_driver_uncompensated_Z_UL = 129.7e3
tst_driver_uncompensated_Z_LL = 90.74e3
tst_driver_uncompensated_Z_UR = 93.52e3
tst_driver_uncompensated_Z_LR = 131.5e3
tst_driver_uncompensated_P_UL = 31.5e3
tst_driver_uncompensated_P_LL = 26.7e3
tst_driver_uncompensated_P_UR = 26.6e3
tst_driver_uncompensated_P_LR = 31.6e3
tst_driver_DC_gain_VpV_HV = 40
tst_driver_DC_gain_VpV_LV = 1.881
anti_imaging_rate_string = 16k
anti_imaging_method = biquad
analog_anti_imaging_file = test/H1aa.mat
dac_gain = 7.62939453125e-05
unknown_actuation_delay = 15e-6
pum_driver_DC_trans_ApV = 2.6847e-4
pum_coil_outf_signflip = 1
pum_NpA = 0.02947
uim_driver_DC_trans_ApV = 6.1535e-4
uim_NpA = 1.634
sus_filter_file = test/H1SUSETMX_1236641144.txt
tst_isc_inf_bank = ETMX_L3_ISCINF_L
tst_isc_inf_modules =
tst_isc_inf_gain = 1.0
tst_lock_bank = ETMX_L3_LOCK_L
tst_lock_modules = 5,8,9,10
tst_lock_gain = 1.0
tst_drive_align_bank = ETMX_L3_DRIVEALIGN_L2L
tst_drive_align_modules = 4,5
tst_drive_align_gain = -35.7
pum_lock_bank = ETMX_L2_LOCK_L
pum_lock_modules = 7
pum_lock_gain = 23.0
pum_drive_align_bank = ETMX_L2_DRIVEALIGN_L2L
pum_drive_align_modules = 6,7
pum_drive_align_gain = 1.0
uim_lock_bank = ETMX_L1_LOCK_L
uim_lock_modules = 10
uim_lock_gain = 1.06
uim_drive_align_bank = ETMX_L1_DRIVEALIGN_L2L
uim_drive_align_modules =
uim_drive_align_gain = 1.0
[calcs]
foton_invsensing_tf = \
  test/2019-04-04_H1CALCS_InverseSensingFunction_Foton_SRCD-2N_Gain_tf.txt
foton_deltal_whitening_tf = \
  test/H1CALCS_DELTAL_EXTERNAL_WHITENING_tf.txt
xarm_uim_analog = test/H1CALCS_ETMX_L1_ANALOG.txt
xarm_pum_analog = test/H1CALCS_ETMX_L2_ANALOG.txt
xarm_tst_analog = test/H1CALCS_ETMX_L3_ANALOG.txt
xarm_output_matrix = 0.0, -1.0, -1.0, -1.0
foton_delay_filter_tf = test/H1CALCS_8_CLK_DELAY.txt
''')
        delay = calcs.sensing_actuation_delay(self.frequencies)
        self.assertTrue(np.allclose(delay/self.known_delay,
                                    np.ones(len(self.frequencies))))


class TestDeltalExtWhitening(unittest.TestCase):

    def setUp(self):
        self.frequencies = np.logspace(0, np.log10(5000.), 10)
        self.known_tf = np.array(
            [653.22198+1645.6321j,
             -144501.22640332347+382419.13620180736j,
             690389.1200990456+102269154.46218154j,
             14723508812.673355-1068490289.9068925j,
             -293161382327.7433-125492534509.41472j,
             29690171524.466835+816147609224.8961j,
             796229614540.8058+552585560164.8594j,
             968079436179.5526+231562800339.5267j,
             995587610786.119+87377107517.47844j,
             999729543068.4756+23985416987.413254j])

    def tearDown(self):
        del self.frequencies
        del self.known_tf

    def test_deltal_ext_whitening(self):
        calcs = pydarm.calcs.CALCSModel('''
[metadata]
[interferometer]
[sensing]
[digital]
[actuation]
[actuation_x_arm]
[calcs]
foton_deltal_whitening_tf = \
  test/H1CALCS_DELTAL_EXTERNAL_WHITENING_tf.txt
''')
        whitening_tf = calcs.deltal_ext_whitening(self.frequencies)
        for n in range(len(self.frequencies)):
            self.assertAlmostEqual(
                np.abs(whitening_tf[n] / self.known_tf[n]), 1)
            self.assertAlmostEqual(
                np.angle(whitening_tf[n], deg=True),
                np.angle(self.known_tf[n], deg=True))


class TestCalcsDttCalibration(unittest.TestCase):

    def setUp(self):
        # Pre-computed values
        self.frequencies = np.logspace(0, np.log10(5000.), 10)
        self.model_string = '''
[metadata]
[interferometer]
[sensing]
x_arm_length = 3994.4704
y_arm_length = 3994.4692
coupled_cavity_optical_gain = 3.22e6
coupled_cavity_pole_frequency = 410.6
detuned_spring_frequency = 4.468
detuned_spring_Q = 52.14
sensing_sign = 1
is_pro_spring = True
anti_aliasing_rate_string = 16k
anti_aliasing_method      = biquad
analog_anti_aliasing_file = test/H1aa.mat, test/H1aa.mat
omc_meas_p_trans_amplifier_uncompensated   = 13.7e3, 17.8e3: 13.7e3, 17.8e3
whitening_mode_names = test, test
omc_meas_p_whitening_uncompensated_test   = 11.346e3, 32.875e3, 32.875e3: 11.521e3, 32.863e3, 32.863e3
gain_ratio = 1, 1
balance_matrix = 1, 1
omc_path_names = A, B
single_pole_approximation_delay_correction = -12e-6
super_high_frequency_poles_apparent_delay = 0, 0
adc_gain = 1638.001638001638, 1638.001638001638
omc_filter_file = test/H1OMC_1239468752.txt
omc_filter_bank = OMC_DCPD_A, OMC_DCPD_B
omc_filter_noncompensating_modules = 4: 4
omc_filter_gain = 1, 1
omc_front_end_trans_amplifier_compensation = ON, ON
omc_front_end_whitening_compensation_test = ON, ON
[digital]
digital_filter_file = test/H1OMC_1239468752.txt
digital_filter_bank = LSC_DARM1, LSC_DARM2
digital_filter_modules = 1,2,3,4,7,9,10: 3,4,5,6,7
digital_filter_gain = 400,1
[actuation]
darm_output_matrix = 1.0, -1.0, 0.0, 0.0
darm_feedback_x = OFF, ON, ON, ON
darm_feedback_y = OFF, OFF, OFF, OFF
[actuation_x_arm]
darm_feedback_sign = -1
tst_NpV2 = 4.427e-11
linearization = OFF
actuation_esd_bias_voltage = -9.3
suspension_file = test/H1susdata_O3.mat
tst_driver_uncompensated_Z_UL = 129.7e3
tst_driver_uncompensated_Z_LL = 90.74e3
tst_driver_uncompensated_Z_UR = 93.52e3
tst_driver_uncompensated_Z_LR = 131.5e3
tst_driver_uncompensated_P_UL = 31.5e3
tst_driver_uncompensated_P_LL = 26.7e3
tst_driver_uncompensated_P_UR = 26.6e3
tst_driver_uncompensated_P_LR = 31.6e3
tst_driver_DC_gain_VpV_HV = 40
tst_driver_DC_gain_VpV_LV = 1.881
anti_imaging_rate_string = 16k
anti_imaging_method = biquad
analog_anti_imaging_file = test/H1aa.mat
dac_gain = 7.62939453125e-05
unknown_actuation_delay = 15e-6
pum_driver_DC_trans_ApV = 2.6847e-4
pum_coil_outf_signflip = 1
pum_NpA = 0.02947
uim_driver_DC_trans_ApV = 6.1535e-4
uim_NpA = 1.634
sus_filter_file = test/H1SUSETMX_1236641144.txt
tst_isc_inf_bank = ETMX_L3_ISCINF_L
tst_isc_inf_modules =
tst_isc_inf_gain = 1.0
tst_lock_bank = ETMX_L3_LOCK_L
tst_lock_modules = 5,8,9,10
tst_lock_gain = 1.0
tst_drive_align_bank = ETMX_L3_DRIVEALIGN_L2L
tst_drive_align_modules = 4,5
tst_drive_align_gain = -35.7
pum_lock_bank = ETMX_L2_LOCK_L
pum_lock_modules = 7
pum_lock_gain = 23.0
pum_drive_align_bank = ETMX_L2_DRIVEALIGN_L2L
pum_drive_align_modules = 6,7
pum_drive_align_gain = 1.0
uim_lock_bank = ETMX_L1_LOCK_L
uim_lock_modules = 10
uim_lock_gain = 1.06
uim_drive_align_bank = ETMX_L1_DRIVEALIGN_L2L
uim_drive_align_modules =
uim_drive_align_gain = 1.0
[pcal]
pcal_dewhiten = 1.0, 1.0
ref_pcal_2_darm_act_sign = -1
analog_anti_aliasing_file = test/H1aa.mat
anti_aliasing_rate_string = 16k
anti_aliasing_method = biquad
[calcs]
foton_invsensing_tf = \
  test/2019-04-04_H1CALCS_InverseSensingFunction_Foton_SRCD-2N_Gain_tf.txt
foton_deltal_whitening_tf = \
  test/H1CALCS_DELTAL_EXTERNAL_WHITENING_tf.txt
xarm_uim_analog = test/H1CALCS_ETMX_L1_ANALOG.txt
xarm_pum_analog = test/H1CALCS_ETMX_L2_ANALOG.txt
xarm_tst_analog = test/H1CALCS_ETMX_L3_ANALOG.txt
xarm_output_matrix = 0.0, -1.0, -1.0, -1.0
foton_delay_filter_tf = test/H1CALCS_8_CLK_DELAY.txt
'''
        self.known_dtt_calibration = np.array(
            [0.00019356005813191712-0.00042488196251998944j,
             -9.451078100284736e-07-2.284431871622057e-06j,
             1.7790453057980935e-10-9.716717778553878e-09j,
             6.612312986720728e-11+6.670843982848847e-12j,
             -3.0625580407492805e-12+9.707481479785013e-13j,
             1.7153848960220716e-13-1.254844015881104e-12j,
             9.785864383613003e-13-2.354168502599546e-13j,
             7.738102950993615e-13+6.274479982018254e-13j,
             -6.479370603503953e-13+7.062109756021947e-13j,
             8.255633601165232e-13+3.1898890750452897e-13j])
        self.known_correction = np.array(
            [-0.0008501089862348232-0.0003863633736571571j,
             -1.7116997942422424e-05-7.969078324489177e-06j,
             -1.238116795723849e-07-4.199824052455882e-07j,
             1.9489520393474323e-08-6.143763314670491e-10j,
             -5.7662915446536716e-09+2.38094579579211e-09j,
             2.7970665627508423e-10-1.6315937801218042e-08j,
             7.545157306911198e-08-4.156187896590543e-08j,
             5.689969540529809e-07+3.095147054562399e-09j,
             3.203791528674027e-06+1.940085939941273e-06j,
            -1.7077191837064583e-06+2.1903105417274858e-05j])

    def tearDown(self):
        del self.frequencies
        del self.model_string
        del self.known_dtt_calibration
        del self.known_correction

    def test_calcs_dtt_calibration(self):
        calcs = pydarm.calcs.CALCSModel(self.model_string)
        calcs_dtt_calib = calcs.calcs_dtt_calibration(self.frequencies)
        for n in range(len(self.frequencies)):
            self.assertAlmostEqual(
                np.abs(calcs_dtt_calib[n] /
                       np.abs(self.known_dtt_calibration[n])), 1)
            self.assertAlmostEqual(
                np.angle(calcs_dtt_calib[n], deg=True),
                np.angle(self.known_dtt_calibration[n], deg=True))

    def test_deltal_ext_pcal_corrrection(self):
        calcs = pydarm.calcs.CALCSModel(self.model_string)
        deltal_ext_pcal = calcs.deltal_ext_pcal_correction(self.frequencies)
        for n in range(len(self.frequencies)):
            self.assertAlmostEqual(
                np.abs(deltal_ext_pcal[n] /
                       np.abs(self.known_correction[n])), 1)
            self.assertAlmostEqual(
                np.angle(deltal_ext_pcal[n], deg=True),
                np.angle(self.known_correction[n], deg=True))


class TestComputeEpicsRecords(unittest.TestCase):

    known_epics = {
            'CAL-CS_TDEP_PCAL_LINE1_CORRECTION_REAL': 0.003384106838174459,
            'CAL-CS_TDEP_PCAL_LINE1_CORRECTION_IMAG': 0.0004044180029064908,
            'CAL-CS_TDEP_SUS_LINE3_REF_INVA_TST_RESPRATIO_REAL': 1196925220371225.5,
            'CAL-CS_TDEP_SUS_LINE3_REF_INVA_TST_RESPRATIO_IMAG': -3841998698753872,
            'CAL-CS_TDEP_SUS_LINE2_REF_INVA_PUM_RESPRATIO_REAL': -4.90204412692278e+17,
            'CAL-CS_TDEP_SUS_LINE2_REF_INVA_PUM_RESPRATIO_IMAG': -1.9987201437993693e+17,
            'CAL-CS_TDEP_SUS_LINE1_REF_INVA_UIM_RESPRATIO_REAL': 2.643473241664109e+17,
            'CAL-CS_TDEP_SUS_LINE1_REF_INVA_UIM_RESPRATIO_IMAG': -1.2695297228124422e+17,
            'CAL-CS_TDEP_PCAL_LINE2_REF_C_NOCAVPOLE_REAL': 3052033.7355621597,
            'CAL-CS_TDEP_PCAL_LINE2_REF_C_NOCAVPOLE_IMAG': -1030751.4694586383,
            'CAL-CS_TDEP_PCAL_LINE2_REF_D_REAL': -243010006.4310854,
            'CAL-CS_TDEP_PCAL_LINE2_REF_D_IMAG': -1207741923.4087756,
            'CAL-CS_TDEP_PCAL_LINE2_REF_A_TST_REAL': -3.6301159301930236e-19,
            'CAL-CS_TDEP_PCAL_LINE2_REF_A_TST_IMAG': 5.17252131286287e-19,
            'CAL-CS_TDEP_PCAL_LINE2_REF_A_PUM_REAL': -3.486603813748813e-21,
            'CAL-CS_TDEP_PCAL_LINE2_REF_A_PUM_IMAG': 2.854144501791321e-21,
            'CAL-CS_TDEP_PCAL_LINE2_REF_A_UIM_REAL': 9.669640696236252e-23,
            'CAL-CS_TDEP_PCAL_LINE2_REF_A_UIM_IMAG': 1.0084874176645285e-22,
            'CAL-CS_TDEP_PCAL_LINE2_CORRECTION_REAL': 5.919275925544666e-06,
            'CAL-CS_TDEP_PCAL_LINE2_CORRECTION_IMAG': +3.317567316630787e-07,
            'CAL-CS_TDEP_PCAL_LINE1_REF_C_NOCAVPOLE_REAL': 3219708.6791652623,
            'CAL-CS_TDEP_PCAL_LINE1_REF_C_NOCAVPOLE_IMAG': -43662.16666949552,
            'CAL-CS_TDEP_PCAL_LINE1_REF_D_REAL': 3152795532.787565,
            'CAL-CS_TDEP_PCAL_LINE1_REF_D_IMAG': 60933868.87924543,
            'CAL-CS_TDEP_PCAL_LINE1_REF_A_TST_REAL': -1.1944749080760831e-16,
            'CAL-CS_TDEP_PCAL_LINE1_REF_A_TST_IMAG': -2.1720205784065532e-16,
            'CAL-CS_TDEP_PCAL_LINE1_REF_A_PUM_REAL': -2.1758869487866404e-16,
            'CAL-CS_TDEP_PCAL_LINE1_REF_A_PUM_IMAG': 2.620157641796169e-16,
            'CAL-CS_TDEP_PCAL_LINE1_REF_A_UIM_REAL': 4.078008711853952e-17,
            'CAL-CS_TDEP_PCAL_LINE1_REF_A_UIM_IMAG': 4.992745126138772e-18,
            'CAL-CS_TDEP_PCAL_LINE3_CORRECTION_REAL': 8.319363469674813e-07,
            'CAL-CS_TDEP_PCAL_LINE3_CORRECTION_IMAG': 1.1949591405958398e-07,
            'CAL-CS_TDEP_PCAL_X_COMPARE_CORRECTION_REAL': -3.978067573573798e-06,
            'CAL-CS_TDEP_PCAL_X_COMPARE_CORRECTION_IMAG': -2.6500091829175134e-07,
            'CAL-CS_TDEP_PCAL_Y_COMPARE_CORRECTION_REAL': 3.978067573573798e-06,
            'CAL-CS_TDEP_PCAL_Y_COMPARE_CORRECTION_IMAG': 2.6500091829175134e-07,
            'CAL-CS_TDEP_SUS_LINE1_SUS_DEMOD_PHASE': -0.3427734375,
            'CAL-CS_TDEP_SUS_LINE2_SUS_DEMOD_PHASE': -0.36035156249999994,
            'CAL-CS_TDEP_SUS_LINE3_SUS_DEMOD_PHASE': -0.38671875}

    model_string = '''
[metadata]
[interferometer]
[sensing]
x_arm_length = 3994.4704
y_arm_length = 3994.4692
coupled_cavity_optical_gain = 3.22e6
coupled_cavity_pole_frequency = 410.6
detuned_spring_frequency = 4.468
detuned_spring_Q = 52.14
sensing_sign = 1
is_pro_spring = True
anti_aliasing_rate_string = 16k
anti_aliasing_method      = biquad
analog_anti_aliasing_file = test/H1aa.mat, test/H1aa.mat
omc_meas_p_trans_amplifier_uncompensated   = 13.7e3, 17.8e3: 13.7e3, 17.8e3
whitening_mode_names = test, test
omc_meas_p_whitening_uncompensated_test   = 11.346e3, 32.875e3, 32.875e3: 11.521e3, 32.863e3, 32.863e3
super_high_frequency_poles_apparent_delay = 0, 0
gain_ratio = 1, 1
balance_matrix = 1, 1
omc_path_names = A, B
single_pole_approximation_delay_correction = -12e-6
adc_gain = 1, 1
omc_front_end_trans_amplifier_compensation = ON, ON
omc_front_end_whitening_compensation_test = ON, ON

[actuation_x_arm]
darm_feedback_sign = -1
tst_NpV2 = 4.427e-11
linearization = OFF
actuation_esd_bias_voltage = -9.3
suspension_file = test/H1susdata_O3.mat
tst_driver_uncompensated_Z_UL = 129.7e3
tst_driver_uncompensated_Z_LL = 90.74e3
tst_driver_uncompensated_Z_UR = 93.52e3
tst_driver_uncompensated_Z_LR = 131.5e3
tst_driver_uncompensated_P_UL = 3.213e3, 31.5e3
tst_driver_uncompensated_P_LL = 3.177e3, 26.7e3
tst_driver_uncompensated_P_UR = 3.279e3, 26.6e3
tst_driver_uncompensated_P_LR = 3.238e3, 31.6e3
tst_driver_DC_gain_VpV_HV = 40
tst_driver_DC_gain_VpV_LV = 1.881
anti_imaging_rate_string = 16k
anti_imaging_method = biquad
analog_anti_imaging_file = test/H1aa.mat
dac_gain = 7.62939453125e-05
unknown_actuation_delay = 15e-6
pum_driver_DC_trans_ApV = 2.6847e-4
pum_coil_outf_signflip = 1
pum_NpA = 0.02947
uim_driver_DC_trans_ApV = 6.1535e-4
uim_NpA = 1.634
sus_filter_file = test/H1SUSETMX_1236641144.txt
tst_isc_inf_bank = ETMX_L3_ISCINF_L
tst_isc_inf_modules =
tst_isc_inf_gain = 1.0
tst_lock_bank = ETMX_L3_LOCK_L
tst_lock_modules = 5,8,9,10
tst_lock_gain = 1.0
tst_drive_align_bank = ETMX_L3_DRIVEALIGN_L2L
tst_drive_align_modules = 4,5
tst_drive_align_gain = -35.7
pum_lock_bank = ETMX_L2_LOCK_L
pum_lock_modules = 7
pum_lock_gain = 23.0
pum_drive_align_bank = ETMX_L2_DRIVEALIGN_L2L
pum_drive_align_modules = 6,7
pum_drive_align_gain = 1.0
uim_lock_bank = ETMX_L1_LOCK_L
uim_lock_modules = 10
uim_lock_gain = 1.06
uim_drive_align_bank = ETMX_L1_DRIVEALIGN_L2L
uim_drive_align_modules =
uim_drive_align_gain = 1.0

[actuation]
darm_output_matrix = 1.0, -1.0, 0.0, 0.0
darm_feedback_x = OFF, ON, ON, ON
darm_feedback_y = OFF, OFF, OFF, OFF

[pcal]
pcal_dewhiten = 1.0, 1.0
ref_pcal_2_darm_act_sign = -1
analog_anti_aliasing_file = test/H1aa.mat
anti_aliasing_rate_string = 16k
anti_aliasing_method = biquad

[digital]
digital_filter_file = test/H1OMC_1239468752.txt
digital_filter_bank = LSC_DARM1, LSC_DARM2
digital_filter_modules = 1,2,3,4,7,9,10: 3,4,5,6,7
digital_filter_gain = 400,1

[calcs]
cal_line_sus_uim_frequency = 15.6
cal_line_sus_pum_frequency = 16.4
cal_line_sus_tst_frequency = 17.6
cal_line_sus_pcal_frequency = 17.1
cal_line_sens_pcal_frequency = 410.3
cal_line_high_pcal_frequency = 1083.7
cal_line_cmp_pcalx_frequency = 500.1
cal_line_cmp_pcaly_frequency = 500.1
'''

    def test_compute_epics_records(self):
        calcs = pydarm.calcs.CALCSModel(self.model_string)
        test_epics = calcs.compute_epics_records(endstation=True)
        for key, val in self.known_epics.items():
            # FIXME: is this enough precision?
            self.assertAlmostEqual(test_epics[key]/val, 1.0, places=6)

    def test_epics_write_to_file(self):
        calcs = pydarm.calcs.CALCSModel(self.model_string)
        test_epics = calcs.compute_epics_records(endstation=True)
        # FIXME: if we were using pytetst we could simply provide a
        # `tmp_file` argument to the test method to get a temporary
        # file from the test harness
        with tempfile.TemporaryDirectory() as d:
            save_file = os.path.join(d, 'test_epics_out')
            pydarm.utils.write_dict_epics(test_epics, dry_run=True, save_file=save_file)
            with open(save_file) as f:
                for line in f.readlines():
                    chan, val = line.strip().split()
                    self.assertAlmostEqual(self.known_epics[chan]/float(val), 1.0, places=6)

if __name__ == '__main__':
    unittest.main()
