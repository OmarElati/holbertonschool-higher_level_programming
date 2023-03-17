#!/usr/bin/python3
"""
    Script that lists all State objects that contain
    the letter a from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    # Get command line arguments
    mysql_user = sys.argv[1]
    mysql_pwd = sys.argv[2]
    db_name = sys.argv[3]

    # Create connection to database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(mysql_user, mysql_pwd, db_name),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query database for states containing letter "a"
    query = session.query(State).filter(State.name.like('%a%')).\
        order_by(State.id)
    result = query.all()

    # Print results
    for state in result:
        print('{}: {}'.format(state.id, state.name))

    # Close session
    session.close()
