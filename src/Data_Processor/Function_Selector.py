"""Function selector class for choosing best ideal functions"""

import numpy as np
from Data_Processor.Exceptions import FunctionSelectionError

class FunctionSelector:
    def __init__(self, Train_Data, Ideal_Function_Data):
        self.Train_Data = Train_Data
        self.Ideal_Function_Data = Ideal_Function_Data
        self.selected_functions = {}
        self.max_deviations = {}

    """this will calculate sum of squared deviations between training data and ideal function data"""
    def calculate_sum_squares(self, train_y, ideal_y):
        deviations = [train_y[i] - ideal_y[i] for i in range(len(train_y))]
        return sum(dev**2 for dev in deviations)

    """This will calculate maximum deviation between training data and ideal functions data"""
    def calculate_max_deviation(self, train_y, ideal_y):
        deviations = [abs(train_y[i] - ideal_y[i]) for i in range(len(train_y))]
        return max(deviations)

    """this will Select the best matching ideal function for each training data."""
    def select_best_ideal_function(self):  
        try:
            for train_func in [col for col in self.Train_Data if col != 'x']:
                min_sum_squares = float('inf')
                best_ideal_func = None
                for ideal_func in [col for col in self.Ideal_Function_Data if col != 'x']:
                    sum_squares = self.calculate_sum_squares(self.Train_Data[train_func],self.Ideal_Function_Data[ideal_func])
                    if sum_squares < min_sum_squares:
                        min_sum_squares = sum_squares
                        best_ideal_func = ideal_func     
                if best_ideal_func:
                    self.selected_functions[train_func] = best_ideal_func
                    self.max_deviations[train_func] = self.calculate_max_deviation(
                        self.Train_Data[train_func],
                        self.Ideal_Function_Data[best_ideal_func]
                    )
            return self.selected_functions
        except Exception as e:
            raise FunctionSelectionError(f"Failed to select best Ideal Function: {str(e)}")

    """this will get the maximum deviations for each selected function pair."""
    def get_max_deviations(self):  
        return self.max_deviations

        


                    

                
         
            



        

          











        



   