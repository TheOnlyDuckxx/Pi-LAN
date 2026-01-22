"""Utilite: scan ports TCP; fonctionnement: tente des connexions async avec timeout."""

import asyncio


async def _check_port(ip: str, port: int, timeout: float = 0.5) -> bool:
    try:
        reader, writer = await asyncio.wait_for(asyncio.open_connection(ip, port), timeout=timeout)
        writer.close()
        await writer.wait_closed()
        return True
    except Exception:
        return False


async def scan_ports(ip: str, ports: list[int]) -> list[int]:
    open_ports: list[int] = []
    sem = asyncio.Semaphore(200)

    async def _guarded(port: int):
        async with sem:
            if await _check_port(ip, port):
                open_ports.append(port)

    await asyncio.gather(*[_guarded(p) for p in ports])
    return sorted(open_ports)
