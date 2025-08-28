"""Test mapping class for mapping test data to ideal functions"""

import math
from .Exceptions import TestMappingError

class TestMapper:
    __test__ =  False 
    def __init__(self, Test_Data, Ideal_Function_Data, selected_functions, max_deviations):
        self.Test_Data = Test_Data
        self.Ideal_Functions_Data = Ideal_Function_Data
        self.selected_functions = selected_functions
        self.max_deviations = max_deviations
        self.mapping_results = []

    """This will map test data to selected ideal functions"""
    def map_test_data(self):
     try:
        for i in range(len(self.Test_Data['x'])):
            x = self.Test_Data['x'][i]
            y = self.Test_Data['y'][i]
            best_match = None
            min_deviation = float('inf')
            for train_func, ideal_func in self.selected_functions.items():
                x_values = self.Ideal_Functions_Data['x']
                indx = min(range(len(x_values)), key=lambda j: abs(x_values[j] - x))
                ideal_y = self.Ideal_Functions_Data[ideal_func][indx]
                deviation = abs(y - ideal_y)
                max_deviation_allowed = self.max_deviations[train_func] * math.sqrt(2)
                if deviation <= max_deviation_allowed and deviation < min_deviation:
                    min_deviation = deviation
                    best_match = {
                        'x': x,
                        'y': y,
                        'delta_y': deviation,
                        'ideal_function_no': ideal_func.upper()
                    }
            if best_match is not None:
                self.mapping_results.append(best_match)
        return self.mapping_results
     except Exception as e:
        raise TestMappingError(f"Failed to map test data: {str(e)}")

