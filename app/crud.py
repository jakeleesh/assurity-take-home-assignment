from sqlalchemy.orm import Session
from . import models, schemas

def get_services(db: Session):
    return db.query(models.Service).all()

def create_service(db: Session, service: schemas.ServiceCreate):
    db_service = models.Service(**service.dict())
    db.add(db_service)
    db.commit()
    db.refresh(db_service)
    return db_service

def create_service_check(db: Session, service_check: dict):
    record = models.ServiceCheck(**service_check)
    db.add(record)
    db.commit()
