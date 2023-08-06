"""Miscellaneous functions used across the library that does not fit into other packages."""

from __future__ import annotations
import builtins

import numpy as np

from mydatapreprocessing import preprocessing

# Lazy imports
# import statsmodels.tsa.api as sm


class Global_vars:
    def __init__(self) -> None:
        self.JUPYTER: bool = True if hasattr(builtins, "__IPYTHON__") else False
        self.GUI: bool = False
        self.PLOTS_CONFIGURED: bool = False


GLOBAL_VARS = Global_vars()


def setup_plots() -> None:
    from pandas.plotting import register_matplotlib_converters

    register_matplotlib_converters()

    try:
        from IPython import get_ipython

        if GLOBAL_VARS.JUPYTER:
            get_ipython().run_line_magic("matplotlib", "inline")
    except Exception:
        pass

    GLOBAL_VARS.PLOTS_CONFIGURED = True


def confidence_interval(
    data: np.ndarray, predicts: int = 7, confidence: float = 0.1, p: int = 1, d: int = 0, q: int = 0
):
    """Function to find confidence interval of prediction for graph.

    Args:
        data (np.ndarray): Time series data
        predicts (int, optional): [description]. Defaults to 7.
        confidence (float, optional): [description]. Defaults to 0.1.
        p (int, optional): 1st order of ARIMA. Defaults to 1.
        d (int, optional): 2nd order of ARIMA. Defaults to 0.
        q (int, optional): 3rd order of ARIMA. Defaults to 0.

    Returns:
        list, list: Lower bound, upper bound.

    """

    import statsmodels.tsa.api as sm

    if len(data) <= 10:
        return

    order = (p, d, q)

    try:

        model = sm.ARIMA(data, order=order)
        model_fit = model.fit(disp=0)
        predictions = model_fit.forecast(steps=predicts, alpha=confidence)

        bounds = predictions[2].T
        lower_bound = bounds[0]
        upper_bound = bounds[1]

    except Exception:

        last_value = data[-1]
        data = preprocessing.do_difference(data)

        model = sm.ARIMA(data, order=order)
        model_fit = model.fit(disp=0)
        predictions = model_fit.forecast(steps=predicts, alpha=confidence)

        bounds = predictions[2].T
        lower_bound = preprocessing.inverse_difference(bounds[0], last_value)
        upper_bound = preprocessing.inverse_difference(bounds[1], last_value)

    return lower_bound, upper_bound


# def pickle_it(data_all_pickle_dict, folder_path):
#     """Pickle test data on disk for faster loading.

#     Args:
#         data_all_pickle_dict (Dict): Dictionary of file name and pickled object. E.g. {'file1.pickle': [1, 2, 3]}
#         folder_path (str): String path to folder where to save pickle.
#     """

#     data_folder = Path(folder_path)

#         with open(file_path, "wb") as output_file:
#             pickle.dump((j), output_file)


# def load_pickled(folder_path):
#     data_folder = Path(folder_path)

#     with open(file_path, "rb") as input_file:
#         Config['data_all'][i] = pickle.load(input_file)


# ## Pickle all the data in test data folder
# ## Pickle option was removed, add if you need it... it's from main, so it need to be updated

# if Config['pickleit']:
#     from predictit.test_data.pickle_test_data import pickle_data_all
#     import pickle
#     pickle_data_all(Config['data_all'], datalength=Config['datalength'])

# if Config['from_pickled']:

#     script_dir = Path(__file__).resolve().parent
#     data_folder = script_dir / "test_data" / "pickled"

#     for i, j in Config['data_all'].items():
#         file_name = i + '.pickle'
#         file_path = data_folder / file_name
#         try:
#             with open(file_path, "rb") as input_file:
#                 Config['data_all'][i] = pickle.load(input_file)
#         except Exception:
#             traceback_warning(f"Test data not loaded - First in Config['py'] pickleit = 1, that save the data on disk, then load from pickled.")
