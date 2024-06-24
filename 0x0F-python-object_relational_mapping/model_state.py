#!/usr/bin/python3
"""
class definition of a State
contains the class definition of a State and an instance Base
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Represents a state for a MySQL database.

    __tablename__ (str): The name of the MySQL table.
    id (sqlalchemy.Integer): represents a column of an auto-generated
    name (sqlalchemy.String): represents a column of a string
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
