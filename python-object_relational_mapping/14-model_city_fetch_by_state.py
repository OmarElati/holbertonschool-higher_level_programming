#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    # Get command line arguments
    mysql_user = sys.argv[1]
    mysql_pwd = sys.argv[2]
    db_name = sys.argv[3]

    # Create connection to database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(mysql_user, mysql_pwd, db_name),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all the cities and states from the database
    query = session.query(City, State).filter(City.state_id == State.id)\
        .order_by(City.id)

    # Print the query results
    for city, state in query:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
