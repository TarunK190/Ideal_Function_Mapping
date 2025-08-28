"""Data loader class for reading CSV files"""

import pandas as pd
import os
from .Exceptions import DataLoadingError


class DataLoader:
    def __init__(self, data_dir="Dataset"):
        self.data_dir = data_dir

    "Loading training data from the dataset"
    def load_training_data(self):
      try:
        file_path = os.path.join(self.data_dir, 'train.csv')
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Training file {file_path} not found")
        df = pd.read_csv(file_path)
        training_data = {}
        for col in df.columns:
            training_data[col.lower()] = df[col].tolist()
        return training_data
      except Exception as e:
        raise DataLoadingError(f"Failed to load Training data: {str(e)}")
      
    "Loading ideal function dataset"
    def load_ideal_functions(self):
        try:
            file_path = os.path.join(self.data_dir, 'ideal.csv')
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"Ideal functions file {file_path} not found")
            df = pd.read_csv(file_path)
            ideal_data = {'x': df['x'].tolist()}
            for col in df.columns:
                if col.startswith('y'):
                    ideal_data[col.lower()] = df[col].tolist()
            return ideal_data
        except Exception as e:
            raise DataLoadingError(f"Failed to load ideal functions: {str(e)}")
        
    "Loading test dataset"
    def load_test_data(self):
        try:
            file_path = os.path.join(self.data_dir, 'test.csv')
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"Test file {file_path} not found.")
            df = pd.read_csv(file_path)
            return {
                'x': df['x'].tolist(),
                'y': df['y'].tolist()
            }
        except Exception as e:
            raise DataLoadingError(f"Failed to load test data: {str(e)}")
