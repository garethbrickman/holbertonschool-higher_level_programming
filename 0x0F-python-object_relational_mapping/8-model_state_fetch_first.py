#!/usr/bin/python3
"""Prints first State object from database hbtn_0e_6_usa, "Nothing" if none
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """ Engine connection
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    """ Session handling
    """

    Session = sessionmaker(bind=engine)
    session = Session()

    """ Query
    """

    query = session.query(State).filter(State.id).first()
    if not query:
        print("Nothing")
        print()
    else:
        print("{}: {}".format(query.id, query.name))

    session.close()
