"""Database manager class for handling all SQLite Operations"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .Models import Base, TrainingData, IdealFunctions, TestData

"""This class will manage the SQLite database operations."""
class DatabaseManager:
    
    def __init__(self, db_path="Ideal_Function_Mapping.db"):
        self.db_path = db_path
        self.engine = create_engine(f"sqlite:///{db_path}")
        self.Session = sessionmaker(bind=self.engine)

    """This will create tables in database"""
    def create_tables(self):
        Base.metadata.create_all(self.engine)
        print("Database tables created successfully")

    """This will create new database session"""
    def get_db_session(self):   
        return self.Session()

    """This will close database session"""
    def close_session(self, session):
        session.close()

    """This will save training data to database"""
    def save_training_data(self, data):
        session = self.get_db_session()
        try:
            for i in range(len(data["x"])):
                training_entry = TrainingData(
                    x=data["x"][i],
                    y1=data["y1"][i] if "y1" in data else None,
                    y2=data["y2"][i] if "y2" in data else None,
                    y3=data["y3"][i] if "y3" in data else None,
                    y4=data["y4"][i] if "y4" in data else None,
                )
                session.add(training_entry)
            session.commit()
            return True
        except Exception as e:
            session.rollback()
            print(f"Error saving training data: {e}")
            return False
        finally:
            self.close_session(session)

    """This will save ideal functions to database"""
    def save_ideal_functions(self, data):
        session = self.get_db_session()
        try:
            for i in range(len(data["x"])):
                ideal_entry = IdealFunctions(x=data["x"][i])
                for fun_num in range(1, 51):  # y1 to y50
                    y_key = f"y{fun_num}"
                    if y_key in data:
                        setattr(ideal_entry, y_key, data[y_key][i])
                session.add(ideal_entry)
            session.commit()
            return True
        except Exception as e:
            session.rollback()
            print(f"Error saving ideal functions: {e}")
            return False
        finally:
            self.close_session(session)

    """This will save test data with mapping results to database"""
    def save_test_data(self, mapping_results):
        session = self.get_db_session()
        try:
            for row in mapping_results:
                if not row or row.get("delta_y") is None or row.get("ideal_function_no") is None:
                    continue  
                test_entry = TestData(x=row["x"],y=row["y"],delta_y=row["delta_y"],ideal_function_no=row["ideal_function_no"],)
                session.add(test_entry)
            session.commit()
            return True
        except Exception as e:
            session.rollback()
            print(f"Error saving test data: {e}")
            return False
        finally:
            self.close_session(session)

    """This will fetch all training data"""
    def get_training_data(self):
        session = self.get_db_session()
        try:
            return session.query(TrainingData).all()
        finally:
            self.close_session(session)

    """this will fetch all the ideal functions data"""
    def get_ideal_functions_data(self):
        
        session = self.get_db_session()
        try:
            return session.query(IdealFunctions).all()
        finally:
            self.close_session(session)

    """this will fetch all test data"""
    def get_test_data(self):
        
        session = self.get_db_session()
        try:
            return session.query(TestData).all()
        finally:
            self.close_session(session)
