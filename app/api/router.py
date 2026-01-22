"""Utilite: assembler les sous-routeurs API; fonctionnement: inclut clients/diagnostics/games."""

from fastapi import APIRouter

from app.api import clients, diagnostics, games

api_router = APIRouter()
api_router.include_router(clients.router, prefix="/clients", tags=["clients"])
api_router.include_router(diagnostics.router, prefix="/diagnostics", tags=["diagnostics"])
api_router.include_router(games.router, prefix="/games", tags=["games"])
