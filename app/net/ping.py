"""Utilite: parse ping; fonctionnement: extrait pertes et stats rtt/jitter."""

import re


def parse_ping(text: str) -> dict:
    loss = None
    m = re.search(r"(\d+)%\s+packet loss", text)
    if m:
        loss = float(m.group(1))

    rtt = None
    m = re.search(r"rtt min/avg/max/mdev = ([\d\.]+)/([\d\.]+)/([\d\.]+)/([\d\.]+)", text)
    if m:
        rtt = {
            "min": float(m.group(1)),
            "avg": float(m.group(2)),
            "max": float(m.group(3)),
            "jitter": float(m.group(4)),
        }

    return {"loss_pct": loss, "rtt": rtt}
