#!/usr/bin/python3
"""
Adds the State "California" with the City "San Francisco" to the database hbtn_0e_100_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City, Base


if __name__ == "__main__":
    # Creates an instance of the engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create all tables in the engine
    Base.metadata.create_all(engine)

    # Creates a new session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State and City
    ca = State(name="California")
    sf = City(name="San Francisco", state=ca)

    # Adds new objects to the session
    session.add_all([ca, sf])

    # Commits the session to the database
    session.commit()
