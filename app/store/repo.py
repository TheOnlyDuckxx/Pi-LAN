"""Utilite: CRUD SQLite; fonctionnement: operations clients/ping/ports."""

from datetime import datetime

from app.store.db import get_db


async def upsert_clients(entries: list[dict]) -> None:
    async for db in get_db():
        for e in entries:
            await db.execute(
                "INSERT INTO clients(ip, mac, alias, last_seen) VALUES(?, ?, ?, ?)",
                (e.get("ip"), e.get("mac"), None, datetime.utcnow().isoformat()),
            )
        await db.commit()


async def list_clients() -> list[dict]:
    async for db in get_db():
        cur = await db.execute("SELECT ip, mac, alias, last_seen FROM clients")
        rows = await cur.fetchall()
        return [{"ip": r[0], "mac": r[1], "alias": r[2], "last_seen": r[3]} for r in rows]
    return []


async def add_ping_result(ip: str, parsed: dict) -> None:
    # Placeholder: stocker ping_results.
    return None


async def add_port_scan(ip: str, open_ports: list[int]) -> None:
    # Placeholder: stocker port_scans.
    return None


async def get_diagnostics_history(ip: str) -> list[dict]:
    return []
