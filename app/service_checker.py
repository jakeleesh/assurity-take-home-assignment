import asyncio
import httpx
from sqlalchemy.orm import Session
from .database import SessionLocal
from . import crud

async def check_services():
    while True:
        db: Session = SessionLocal()
        services = crud.get_services(db)
        for svc in services:
            try:
                async with httpx.AsyncClient(timeout=5) as client:
                    resp = await client.get(svc.url)
                    latency = resp.elapsed.total_seconds() if hasattr(resp, 'elapsed') else None
                    version = resp.headers.get("X-Service-Version")
                    status = "up" if resp.status_code == 200 else "down"
            except Exception:
                latency = None
                version = None
                status = "down"

            crud.create_service_check(db, {
                "service_id": svc.id,
                "status": status,
                "latency": latency,
                "version": version
            })
        db.close()
        await asyncio.sleep(30)  # repeat every 30 seconds

def start_scheduler():
    asyncio.create_task(check_services())
