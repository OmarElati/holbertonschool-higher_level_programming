#!/usr/bin/python3
"""
    Defines the City class with a relationship
    to the State class using SQLAlchemy
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State


class City(Base):
    """Represents a city for a MySQL database using SQLAlchemy"""
    __tablename__ = 'cities'
    id = Column(Integer,
                autoincrement=True,
                nullable=False,
                primary_key=True)
    name = Column(String(128),
                  nullable=False)
    state_id = Column(Integer,
                      ForeignKey('states.id'),
                      nullable=False)
