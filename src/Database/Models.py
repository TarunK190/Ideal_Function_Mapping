"""Database models using Sqlalchemy ORM"""
import os
import sys
from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

"SQLAlchemy model for Train data table"
class TrainingData(Base):
   __tablename__ = 'Train_Data'
   id = Column(Integer, primary_key=True)
   x  = Column(Float,nullable=False)
   y1 = Column(Float,nullable=False)
   y2 = Column(Float,nullable=False)
   y3 = Column(Float,nullable=False)
   y4 = Column(Float,nullable=False)

"Sqlalchemy model for Ideal Functions table"
class IdealFunctions(Base):
    __tablename__ = 'Ideal_Function_Data'
    id = Column(Integer, primary_key=True)
    x = Column(Float, nullable=False)
for i in range(1, 51):
    column_name = f'y{i}'
    column = Column(Float, nullable=False)
    setattr(IdealFunctions, column_name, column)

"Sqlalchemy model table for Test Data with mapping results"
class TestData(Base):
   __tablename__ = 'Test_Data'
   id = Column(Integer,primary_key=True)
   x = Column(Float,nullable=False)
   y = Column(Float,nullable=False)
   delta_y = Column(Float, nullable=False)  
   ideal_function_no = Column(String(10), nullable=False)  




