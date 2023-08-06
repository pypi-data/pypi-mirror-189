"""Module with function compare_predicted_to_test that Compare tested model with reality. It return some error
criterion based on config """

from __future__ import annotations
import importlib.util

import numpy as np

import mylogging

from predictit import misc

# Lazy imports
# from IPython import get_ipython
# import matplotlib
# import matplotlib.pyplot as plt
# from sklearn.metrics import mean_squared_error
# from dtaidistance import dtw


def compare_predicted_to_test(
    predicted: np.ndarray,
    test: np.ndarray,
    error_criterion: str = "mape",
    plot: bool = False,
    model_name: str = "Model",
    data_name: str = "Data",
):
    """Compare tested model with reality.

    Args:
        predicted (np.ndarray): Model output.
        test (np.ndarray): Correct values or output from data_pre funcs.
        error_criterion (str, optional): 'mape' or 'rmse'. Defaults to 'mape'.
        plot (bool, optional): Whether create plot. Defaults to False.
        model_name (str, optional): Model name for plot. Defaults to "Model".
        data_name (str, optional): Data name for plot. Defaults to "Data".

    Returns:
        float: Error criterion value (mape or rmse). If configured, plot of results as well.
    """

    predicts = len(predicted)

    if predicts != len(test):
        print("Test and predicted length not equal")
        return np.nan

    if predicted is not None:
        if plot:

            if not misc.GLOBAL_VARS.PLOTS_CONFIGURED:
                misc.setup_plots()

            import matplotlib.pyplot as plt

            plt.figure(figsize=(10, 6))
            plt.plot(test, label="Reality")
            plt.plot(predicted, label="Prediction")
            plt.legend(loc="upper right")
            plt.xlabel("t")
            plt.ylabel("Predicted value")
            plt.title("Prediction with \n {} with data {}".format(model_name, data_name))
            plt.show()

        error = np.array(predicted) - np.array(test)

        """
        abs_error = [abs(i) for i in error]
        sum_abs_error = sum(abs_error)
        mae = sum_abs_error / predicts
        """

        if error_criterion == "mse" or error_criterion == "mse_sklearn":
            from sklearn.metrics import mean_squared_error

            criterion_value = mean_squared_error(test, predicted)

        elif error_criterion == "max_error":
            from sklearn.metrics import max_error

            criterion_value = max_error(test, predicted)

        elif error_criterion == "rmse":
            rmseerror = error ** 2
            criterion_value = (sum(rmseerror) / predicts) ** (1 / 2)

        elif error_criterion == "mape":
            no_zero_test = np.where(abs(test) >= 1, test, 1)
            criterion_value = np.mean(np.abs((test - predicted) / no_zero_test)) * 100

        elif error_criterion == "dtw":

            if not importlib.util.find_spec("dtaidistance"):
                raise ImportError(
                    mylogging.return_str(
                        "Library dtaidistance necessary for configured dtw (dynamic time warping) "
                        "error criterion is not installed! Install it via \n\npip install dtaidistance"
                    )
                )

            from dtaidistance import dtw

            criterion_value = dtw.distance_fast(predicted.astype("double"), test.astype("double"))

        else:
            raise KeyError(
                mylogging.return_str(
                    f"bad 'error_criterion' in config - '{error_criterion}'. Use some from options from config "
                    "comment... "
                )
            )

        return criterion_value
