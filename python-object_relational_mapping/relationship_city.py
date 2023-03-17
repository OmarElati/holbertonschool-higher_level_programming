#!/usr/bin/python3

"""
This module defines a City model that represents a city
for a MySQL database. The City model inherits from SQLAlchemy's
Base class and is linked to the MySQL table 'cities'.

Attributes:
    __tablename__ (str): The name of the MySQL table used for this model.
    id (sqlalchemy.Column): The city's id.
    name (sqlalchemy.Column): The city's name.
    state_id (sqlalchemy.Column): The city's state id.
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# create a declarative base instance
Base = declarative_base()


class City(Base):
    """
    Represents a city for a MySQL database.

    Attributes:
        id (sqlalchemy.Column): The city's id.
        name (sqlalchemy.Column): The city's name.
        state_id (sqlalchemy.Column): The city's state id.
    """
    # set the name of the MySQL table used for this model
    __tablename__ = "cities"

    # define columns for the cities table
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
