#!/usr/bin/python3
"""
This script adds the State California with the City
San Francisco to the database hbtn_0e_100_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City
from model_state import Base

if __name__ == "__main__":
    if len(sys.argv) == 4:
        # get username, password, and db_name from command line arguments
        username = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]

        # set up engine
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                               .format(username, password, db_name),
                               pool_pre_ping=True)

        # create all tables in the database
        Base.metadata.create_all(engine)

        # create a new session
        Session = sessionmaker(bind=engine)
        session = Session()

        # create California and San Francisco
        ca = State(name="California")
        sf = City(name="San Francisco")
        ca.cities.append(sf)

        # add California and San Francisco to the session
        session.add_all([ca, sf])

        # commit the session to the database
        session.commit()

        # close the session
        session.close()
    else:
        # print usage instructions if the script not given correct arguments
        print("Usage: {} <username> <password> <database name>".format
              (sys.argv[0]))
