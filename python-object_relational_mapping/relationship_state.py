#!/usr/bin/python3
"""
This module defines the State class.
"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from relationship_city import Base, City


Base = declarative_base()


class State(Base):
    """
    This class represents a state entity in the database.
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City",
        backref="state",
        cascade="all, delete-orphan"
        )
