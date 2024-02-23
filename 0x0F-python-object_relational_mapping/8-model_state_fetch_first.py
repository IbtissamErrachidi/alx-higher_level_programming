#!/usr/bin/python3
"""
A script that prints the first State object from the database..
"""

from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    connection_string = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                    mysql_username, mysql_password, database_name)

    engine = create_engine(connection_string, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).order_by(State.id).first()

    if state:
        print('{}: {}'.format(state.id, state.name))
    else:
        print('Nothing')

    session.close()
