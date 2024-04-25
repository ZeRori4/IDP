from collections import namedtuple

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import host

Base = declarative_base()

Session = sessionmaker()
session = Session(autoflush=False, autocommit=False)


class EventLog(Base):
    __tablename__ = "event_log"
    id = sa.Column(sa.Integer, primary_key=True, nullable=False)
    event_type = sa.Column(sa.Integer, nullable=False)
    ts = sa.Column(sa.BigInteger, nullable=False)
    origin = sa.Column(sa.String(36), nullable=False)
    p1 = sa.Column(sa.Text, nullable=False)
    p2 = sa.Column(sa.Text, nullable=False)
    p3 = sa.Column(sa.Text, nullable=False)
    flags = sa.Column(sa.Integer, nullable=False)

    @classmethod
    def query(cls):
        return session.query(cls)


Database = namedtuple("DB", ["EventLog"])


def init_db(engine=None):
    global session

    if engine is None:
        engine = host.get_database_connection()

    Session.configure(bind=engine)
    session = Session(autocommit=False, autoflush=False)

    return Database(EventLog)
