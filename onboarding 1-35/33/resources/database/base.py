# -*- coding: utf-8 -*-
from collections import namedtuple
from contextlib import contextmanager

import sqlalchemy as sa
import sqlalchemy.orm as so
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base

import host


metadata = sa.MetaData()
Session = so.scoped_session(so.sessionmaker())
Session_reader = so.scoped_session(so.sessionmaker())

Base = declarative_base(metadata=metadata)

@contextmanager
def session(close=True, remove=False, **kwargs):
    """Provide a transactional scope around a series of operations."""
    new_session = Session(**kwargs)
    try:
        yield new_session
        new_session.commit()
    except SQLAlchemyError as err:
        new_session.rollback()
        raise err
    finally:
        if close:
            new_session.close()
        if remove:
            Session.remove()


Database = namedtuple(
    "DB", ["AlchemyTest", "session", "session_query"]
)


def init_db(engine=None, config=None):
    if engine is None:
        engine = host.get_database_connection()

    from .schema import AlchemyTest

    AlchemyTest.config = config
    Session.configure(bind=engine)
    Session_reader.configure(bind=engine)
    metadata.bind = engine
    session_query = Session_reader()
    metadata.create_all()

    return Database(AlchemyTest, session, session_query)
