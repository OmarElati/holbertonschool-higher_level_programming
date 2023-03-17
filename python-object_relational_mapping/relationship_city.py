#!/usr/bin/python3
"""
This module defines the City class which represents a city in a MySQL database. It inherits from SQLAlchemy Base and links to the MySQL table cities.

Classes:

    City: Represents a city in a MySQL database.
Attributes:
        id (sqlalchemy.Column): The city's id.
        name (sqlalchemy.Column): The city's name.
        state_id (sqlalchemy.Column): The city's state id.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import Base, State


class City(Base):
    """
    City class for database
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
    state = relationship("State", back_populates="cities")
