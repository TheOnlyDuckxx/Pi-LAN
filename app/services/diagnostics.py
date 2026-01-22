"""Utilite: orchestrer ping/ports; fonctionnement: compose les wrappers reseau et persiste."""

from app.net.ping import parse_ping
from app.net.ports import scan_ports
from app.store.repo import add_ping_result, add_port_scan
from app.util.shell import run_command


async def run_ping(ip: str | None) -> dict:
    if not ip:
        return {"error": "missing_ip"}
    result = run_command(["ping", "-c", "2", ip], timeout=3)
    parsed = parse_ping(result["stdout"])
    await add_ping_result(ip, parsed)
    return parsed


async def run_ping_all() -> dict:
    # Placeholder: appeller run_ping en parallele via liste clients.
    return {"status": "not_implemented"}


async def run_port_scan(ip: str | None) -> dict:
    if not ip:
        return {"error": "missing_ip"}
    open_ports = await scan_ports(ip, [80, 443])
    await add_port_scan(ip, open_ports)
    return {"ip": ip, "open_ports": open_ports}
