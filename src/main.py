"""Main application for python Ideal Function Mapping"""
import os
import sys
from Database.Manager import DatabaseManager
from Data_Processor.Data_Loader import DataLoader
from Data_Processor.Function_Selector import FunctionSelector
from Data_Processor.Test_Mapper import TestMapper
from Data_Processor.plot_generator import PlotGenerator
from Data_Processor.Exceptions import DataLoadingError, FunctionSelectionError, TestMappingError, DatabaseError, VisualizationError
 
class DataAnalysisApplication:
    def __init__(self, data_dir="Dataset", db_path="Ideal_Function_Mapping.db"):
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.data_dir = os.path.join(project_root, data_dir)
        self.db_path = db_path
        self.db_manager = DatabaseManager(db_path)
        self.data_loader = DataLoader(self.data_dir)

    """Run the application"""
    def run(self): 
       try:
            print("Starting data analysis application")
            print("Creating database tables")
            self.db_manager.create_tables()

            print("Loading training data")
            Train_Data = self.data_loader.load_training_data()
            
            print("Loading ideal functions")
            Ideal_Function_Data = self.data_loader.load_ideal_functions()

            print("Loading test data")
            Test_Data = self.data_loader.load_test_data()
            
            print("Saving training data to database")
            if not self.db_manager.save_training_data(Train_Data):
                raise DatabaseError("Failed to save training data to database.")
            
            print("Saving ideal functions to database")
            if not self.db_manager.save_ideal_functions(Ideal_Function_Data):
                raise DatabaseError("Failed to save ideal functions to database")
       
            print("Selecting best Ideal functions")
            function_selector= FunctionSelector(Train_Data,Ideal_Function_Data)
            selected_functions=function_selector.select_best_ideal_function()
            max_deviations=function_selector.get_max_deviations()

            print("Mapping test data")
            test_mapper=TestMapper(Test_Data,Ideal_Function_Data,selected_functions,max_deviations)
            mapping_results=test_mapper.map_test_data()

            print("saving mapping results to database")
            if not self.db_manager.save_test_data(mapping_results):
                raise DatabaseError("Failed to save test data to database")

            print("Generating visualization")
            plot_generator = PlotGenerator(self.db_manager)
            plot_generator.generate_visualization(selected_functions)
       except DataLoadingError as e:
            print(f"Data loading error: {str(e)}")
            sys.exit(1)
   
if __name__ == "__main__":
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(project_root,"Dataset")
    if not os.path.exists(data_path):
        print(f"Error: Data directory '{data_path}' not found.")
        sys.exit(1)
    app = DataAnalysisApplication(data_dir=data_path)
    app.run()