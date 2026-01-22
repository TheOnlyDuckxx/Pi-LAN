"""Utilite: endpoints diagnostics; fonctionnement: orchestre ping/scan et historique."""

from fastapi import APIRouter

from app.services.diagnostics import run_ping, run_ping_all, run_port_scan
from app.store.repo import get_diagnostics_history

router = APIRouter()


@router.post("/ping")
async def ping_one(payload: dict):
    ip = payload.get("ip")
    return await run_ping(ip)


@router.post("/ping_all")
async def ping_all():
    return await run_ping_all()


@router.post("/scan_ports")
async def scan_ports(payload: dict):
    ip = payload.get("ip")
    return await run_port_scan(ip)


@router.get("/history")
async def history(ip: str):
    return {"history": await get_diagnostics_history(ip)}
