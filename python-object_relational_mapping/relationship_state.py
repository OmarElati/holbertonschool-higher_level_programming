#!/usr/bin/python3
"""class"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """state class"""
    __tablename__ = 'states'
    id = Column(Integer, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")

    def __init__(self, name):
        self.name = name
        self.cities = []
