"""Utilite: parse ip neigh; fonctionnement: normalise IP/MAC/etat/interface."""

from __future__ import annotations


def parse_ip_neigh(text: str) -> list[dict]:
    entries: list[dict] = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) < 4:
            continue
        ip = parts[0]
        iface = parts[2] if len(parts) > 2 else None
        mac = None
        state = parts[-1]
        if "lladdr" in parts:
            idx = parts.index("lladdr")
            if idx + 1 < len(parts):
                mac = parts[idx + 1]
        entries.append({"ip": ip, "mac": mac, "state": state, "iface": iface})
    return entries
