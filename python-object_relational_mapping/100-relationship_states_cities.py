#!/usr/bin/python3
"""
This script creates a State "California" with a City "San Francisco"
in the hbtn_0e_100_usa database using SQLAlchemy.
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base
from relationship_city import City


if __name__ == "__main__":
    # Create engine to connect to the database
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create tables if they don't exist
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create the State "California" and the City "San Francisco"
    california = State(name="California")
    san_francisco = City(name="San Francisco", state=california)
    session.add_all([california, san_francisco])
    session.commit()

    # Close the session
    session.close()
