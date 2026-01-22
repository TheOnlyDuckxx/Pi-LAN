"""Utilite: endpoints jeux; fonctionnement: expose catalogue et details depuis l'indexer."""

from fastapi import APIRouter

from app.games.indexer import build_catalog

router = APIRouter()


@router.get("")
async def list_games():
    return {"games": build_catalog()}


@router.get("/{name}")
async def game_detail(name: str):
    catalog = build_catalog()
    for game in catalog:
        if game.get("name") == name:
            return game
    return {"error": "not_found"}


@router.get("/{name}/checksums")
async def game_checksums(name: str):
    return {"name": name, "checksums": []}
