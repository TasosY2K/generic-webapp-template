from sqlalchemy import Column, Integer, Float, String, TIMESTAMP, create_engine
from sqlalchemy.types import Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class PowerMeasurement(Base):
    __tablename__ = "PowerMeasurement"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(Integer)
    source = Column(String)
    value = Column(Float)