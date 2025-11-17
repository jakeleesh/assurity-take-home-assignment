from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from .database import Base

class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    url = Column(String)
    expected_version = Column(String)

class ServiceCheck(Base):
    __tablename__ = "service_checks"

    id = Column(Integer, primary_key=True)
    service_id = Column(Integer)
    status = Column(String)
    latency = Column(Float)
    version = Column(String)
    checked_at = Column(DateTime(timezone=True), server_default=func.now())
