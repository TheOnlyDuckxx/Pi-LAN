"""Utilite: init SQLite; fonctionnement: ouvre une connexion aiosqlite si async."""

import aiosqlite
from collections.abc import AsyncGenerator


_DB_PATH: str | None = None


async def init_db(path: str) -> None:
    global _DB_PATH
    _DB_PATH = path
    async with aiosqlite.connect(path) as db:
        await db.execute(
            "CREATE TABLE IF NOT EXISTS clients (id INTEGER PRIMARY KEY, ip TEXT, mac TEXT, alias TEXT, last_seen TEXT)"
        )
        await db.commit()


async def get_db() -> AsyncGenerator:
    if not _DB_PATH:
        raise RuntimeError("DB non initialisee")
    async with aiosqlite.connect(_DB_PATH) as db:
        yield db
