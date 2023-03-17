#!/usr/bin/python3
"""
This module defines the City class.
"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State


Base = declarative_base()


class City(Base):
    """
    This class represents a city entity in the database.
    """

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
