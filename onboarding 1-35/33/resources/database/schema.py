import sqlalchemy as sa

from .base import Base

class AlchemyTest(Base):
    __tablename__ = 'alchemy_test'
    id = sa.Column(sa.Integer, primary_key=True, nullable=False)
    timestamp = sa.Column(sa.Integer, nullable=False)
    random_int = sa.Column(sa.Integer, nullable=False)
