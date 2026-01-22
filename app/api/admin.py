"""Utilite: endpoints admin; fonctionnement: operations tournoi (alias, equipes, exports)."""

from fastapi import APIRouter

router = APIRouter()


@router.post("/alias")
async def set_alias(payload: dict):
    return {"status": "accepted", "payload": payload}
