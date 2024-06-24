#!/usr/bin/python3
"""
contains the class definition of a City
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Represents a city for a MySQL database.

    Attributes:
        id (str): represents a column of an auto-generated
        name (sqlalchemy.Integer): represents a column of a string
        state_id (sqlalchemy.String): represents a column of an integer,
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
