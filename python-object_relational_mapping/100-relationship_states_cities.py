#!/usr/bin/python3
"""
This script creates the State “California” with the City “San Francisco” from the database hbtn_0e_100_usa.

Usage: ./100-relationship_states_cities.py <mysql username> <mysql password> <database name>

The script connects to a MySQL server running on localhost at port 3306 and uses the SQLAlchemy module for the database operations.

"""

# import necessary modules
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City

if __name__ == "__main__":
    # create engine and session
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # create new State and City objects and add them to session
    new_state = State(name="California")
    new_city = City(name="San Francisco", state=new_state)
    session.add(new_state)
    session.add(new_city)
    session.commit()
