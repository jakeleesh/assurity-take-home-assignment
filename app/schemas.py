from pydantic import BaseModel
from datetime import datetime

class ServiceBase(BaseModel):
    name: str
    url: str
    expected_version: str

class ServiceCreate(ServiceBase):
    pass

class ServiceOut(ServiceBase):
    id: int

    class Config:
        orm_mode = True

class ServiceCheckOut(BaseModel):
    service_id: int
    status: str
    latency: float | None
    version: str | None
    checked_at: datetime

    class Config:
        orm_mode = True
