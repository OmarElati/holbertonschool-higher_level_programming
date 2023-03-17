#!/usr/bin/python3
"""Defines the State class with a relationship to the City class
    using SQLAlchemy"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    """Represents a state for a MySQL database using SQLAlchemy"""
    __tablename__ = 'states'
    id = Column(Integer,
                autoincrement=True,
                nullable=False,
                primary_key=True)
    name = Column(String(128),
                  nullable=False)
    cities = relationship("City",
                          backref="state",
                          cascade="all, delete")
