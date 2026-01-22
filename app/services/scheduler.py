"""Utilite: refresh periodique; fonctionnement: boucle simple pour discovery/ping light."""

import asyncio

from app.services.discovery import discover_clients


async def run_scheduler(interval_s: int = 30) -> None:
    while True:
        await discover_clients()
        await asyncio.sleep(interval_s)
