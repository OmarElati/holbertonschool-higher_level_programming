#!/usr/bin/python3
"""
Lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == '__main__':
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Creating engine and binding it to metadata
    engine = create_engine(f'mysql+mysqldb://{user}:{password}@localhost:3306/{db_name}')
    Base.metadata.create_all(engine)

    # Creating a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Creating a Session object
    session = Session()

    # Querying the database to retrieve all State objects and their City objects
    result = session.query(State).order_by(State.id).all()

    # Printing the results
    for state in result:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")
