#!/usr/bin/python3
"""
This module defines the State class which represents a state in a MySQL database. It inherits from SQLAlchemy Base and links to the MySQL table states. It also represents a relationship with the class City.

Classes:

    State: Represents a state in a MySQL database.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    """
        Attributes:
            __tablename__ (str): The name of the MySQL table to store States.
            id (sqlalchemy.Integer): The state's id.
            name (sqlalchemy.String): The state's name.
            cities (sqlalchemy.orm.relationship): The State-City relationship.
            If the State object is deleted, all linked City objects will be automatically deleted.
            Also, the reference from a City object to its State will be named state.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state", cascade="all, delete")
