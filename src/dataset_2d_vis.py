import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class Dataset2DVisualizer:
    """
    General Class for visualizing 2D datasets. This class provides methods to visualize datasets in two dimensions, 
    allowing for easy exploration and analysis of the data.

    Attributes:
        dataset (pd.DataFrame) (optional): The dataset to visualize.
        title (str) (optional): The title of the plot.
        xlabel (str) (optional): The label for the x-axis.
        ylabel (str) (optional): The label for the y-axis.
        y_values (np.ndarray) (optional): The target values (labels) of the dataset.
        X_values (np.ndarray) (optional): The feature values of the dataset.
    """
    def __init__(self, 
                 dataset: pd.DataFrame | None,
                 title: str | None = None,
                 xlabel: str | None = None,
                 ylabel: str | None = None,
                 y_values: np.ndarray | None = None,
                 X_values: np.ndarray | None = None):
        if dataset is not None:
            self._y = dataset.iloc[:, -1].values
            self._X = dataset.iloc[:, :-1].values
        else:
            self._y = y_values
            self._X = X_values
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if not isinstance(value, np.ndarray):
            raise ValueError("y must be a numpy array.")
        self._y = value

    @property
    def X(self):
        return self._X

    @X.setter
    def X(self, value):
        if not isinstance(value, np.ndarray):
            raise ValueError("X must be a numpy array.")
        self._X = value