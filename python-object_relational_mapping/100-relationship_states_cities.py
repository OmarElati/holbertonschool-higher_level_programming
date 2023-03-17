#!/usr/bin/python3
"""Adds the State California with the City San Francisco to a MySQL database"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City, Base


if __name__ == "__main__":
    # Set up SQLAlchemy engine and session
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(user, password, db_name), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create the State "California" and the City "San Francisco"
    ca = State(name="California", cities=[City(name="San Francisco")])
    session.add(ca)
    session.commit()
    session.close()
