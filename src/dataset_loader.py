import os
import pandas as pd

class Dataset:
    @staticmethod
    def load_dataset(webpath: str) -> pd.DataFrame:
        """
        Load a dataset from a given web path.

        Args:
            webpath (str): The URL of the dataset to load.
        Returns:
            pd.DataFrame: The loaded dataset.
        """
        return pd.read_csv(webpath, header=None, encoding='utf-8')

