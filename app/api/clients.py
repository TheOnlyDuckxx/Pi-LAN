"""Utilite: endpoints clients; fonctionnement: expose liste/refresh/manuel via services discovery."""

from fastapi import APIRouter

from app.services.discovery import discover_clients
from app.store.repo import list_clients

router = APIRouter()


@router.get("")
async def get_clients():
    return {"clients": await list_clients()}


@router.post("/refresh")
async def refresh_clients():
    await discover_clients()
    return {"status": "ok"}


@router.post("/manual")
async def add_manual_client(payload: dict):
    # Placeholder: payload devrait contenir ip/mac/alias.
    return {"status": "accepted", "payload": payload}
