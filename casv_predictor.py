import numpy as np
from casv_utils import timethis

@timethis
def get_prediction_by(cohort, arpu, ARs, SRs):
    """
the function calculate revenue (value) prediction for a given cohort based on a vector of activation rates
and vector of survival rates (probabilities).
    :param cohort: size of cohort for which we aplly prediction
    :param arpu: average revenue by user (per day of activity )
    :param ARs: activation rates
    :param SRs: survival rates
    :return: cumulative value predicted for each day
    """
    print('Prediction parameters')
    print('given cohort size: ', cohort)
    print('given arpu: ',arpu)
    print('given Activation coefficients: ',ARs)
    print('given Survival coefficients: ',SRs)
    ARs = ARs.reshape((-1, 1))
    l_ARs = len(ARs)
    l_SRs = len(SRs)
    print('available prediction depth: ',l_SRs , ' days')
    if l_ARs>l_SRs:
        raise Exception('MODEL_ERROR', 'ARs array length cannot be bigger than SRs array length')

    # -- set formats for matrix output formatting
    float_formatter = lambda x: "%.2f" % x
    np.set_printoptions(formatter={'float_kind': float_formatter})
    # TO DO multiple cohort_r on matrix of conv ratios
    Mcv = ARs * cohort
    # TO DO multiply matrix
    Msv = Mcv * SRs
    Msv_predict = Msv * arpu

    print('')
    print('---- predicted active user from a given cohort')
    print(Msv)
    print('----- predicted revenue matrix for a given cohort')
    print(Msv_predict)
    print('----- predicted earnings from a given cohort on a given interval in future')
    print('TOTAL Earnings: ', Msv_predict.sum())
    cumulative_prediction_set = np.array([])
    for i in range(1, l_SRs + 1):
        if i <= l_ARs:
            print("Earnings on day [", i - 1, "] after registration ", Msv_predict[0:i, 0:i].sum())
            cumulative_prediction_set = np.append(cumulative_prediction_set, [Msv_predict[0:i, 0:i].sum()])
        else:
            print("Earnings on day [", i - 1, "] after registration ", Msv_predict[0:l_ARs, 0:i].sum())
            cumulative_prediction_set = np.append(cumulative_prediction_set, [Msv_predict[0:l_ARs, 0:i].sum()])
    return cumulative_prediction_set
