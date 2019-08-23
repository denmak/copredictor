import numpy as np
import casv_predictor as cp

# set model parameters
arpu = 10.0
cohort_r = 100
activation_rates = np.array([0.26, 0.17, 0.12, 0.03, 0.01])
survival_rates = np.array([1.00,0.88,0.73,0.62,0.47,0.33,0.21,0.12,0.07,0.01])



CPs = cp.get_prediction_by(cohort = cohort_r,arpu = arpu,ARs = activation_rates, SRs = survival_rates)

print(CPs)