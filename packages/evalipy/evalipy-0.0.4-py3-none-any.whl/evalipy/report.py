import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from .metrics import Metrics
from .model import Model


class Report:
    def __init__(self, model: Model, actual_data: np.ndarray, predicted_data: np.ndarray, model_identifier='model 1'):
        self.model = model
        self.actual_data = actual_data
        self.predicted_data = predicted_data
        self.model_identifier = model_identifier
        self.report = self.__generate_report()

    def __generate_report(self):
        return pd.DataFrame.from_dict(
            {"Mean Squared Error(MSE)": Metrics.MSE(self.actual_data, self.predicted_data),
             "Mean Absolute Error(MAE)": Metrics.MAE(self.actual_data, self.predicted_data),
             "R-Squared(R2)": Metrics.R2(self.actual_data, self.predicted_data),
             "Root Mean Square Error(RMSE)": Metrics.RMSE(self.actual_data, self.predicted_data),
             "Root Relative Squared Error(RRSE)": Metrics.RRSE(self.actual_data, self.predicted_data),
             "Relative Absolute Error(RAE)": Metrics.RAE(self.actual_data, self.predicted_data),
             }, orient='index', columns=[f'{self.model_identifier}'])

    def __str__(self) -> str:
        return self.report.__repr__()

    def __repr__(self) -> pd.DataFrame:
        return self.report
