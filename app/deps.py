"""Utilite: dependances FastAPI; fonctionnement: expose settings et db via injection."""

from collections.abc import AsyncGenerator

from app.config import get_settings
from app.store.db import get_db


def provide_settings():
    return get_settings()


async def provide_db() -> AsyncGenerator:
    async for conn in get_db():
        yield conn
