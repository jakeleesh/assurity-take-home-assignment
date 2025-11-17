from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import Base, engine, get_db
from . import crud, schemas
from .service_checker import start_scheduler

app = FastAPI(title="Service Reliability Monitor")

# Create tables at startup
Base.metadata.create_all(bind=engine)

@app.on_event("startup")
async def startup_event():
    start_scheduler()

@app.get("/services", response_model=list[schemas.ServiceOut])
def list_services(db: Session = Depends(get_db)):
    return crud.get_services(db)

@app.post("/services", response_model=schemas.ServiceOut)
def create_service(service: schemas.ServiceCreate, db: Session = Depends(get_db)):
    return crud.create_service(db, service)
