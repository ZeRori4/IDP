
import sqlalchemy as sa

from .base import Base, Session

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
        return Session.query(cls)
