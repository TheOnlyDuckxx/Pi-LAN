"""Utilite: decouverte clients; fonctionnement: lit ip neigh et stocke en base."""

from app.net.neigh import parse_ip_neigh
from app.store.repo import upsert_clients
from app.util.shell import run_command


async def discover_clients() -> list[dict]:
    result = run_command(["ip", "neigh"], timeout=2)
    entries = parse_ip_neigh(result["stdout"])
    await upsert_clients(entries)
    return entries
