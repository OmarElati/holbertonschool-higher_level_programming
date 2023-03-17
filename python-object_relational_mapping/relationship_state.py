#!/usr/bin/python3
"""
State class that defines a State model.
Inherits from SQLAlchemy Base and links to the MySQL table states.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class State(Base):
    """
    Represents a state for a MySQL database.

    Attributes:
        id (sqlalchemy.Column): The state's id.
        name (sqlalchemy.Column): The state's name.
        cities (sqlalchemy.orm.relationship): The state's associated cities.

    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete')
