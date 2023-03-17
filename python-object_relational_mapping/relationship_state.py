#!/usr/bin/python3
"""class"""


from sqlalchemy import Column, Integer, String
from relationship_city import Base


class State(Base):
    """state class"""
    __tablename__ = 'states'
    id = Column(Integer, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
