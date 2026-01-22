"""Utilite: limiter les actions; fonctionnement: garde un timestamp par cle."""

import time

_LAST: dict[str, float] = {}


def allow(key: str, every_s: float) -> bool:
    now = time.time()
    last = _LAST.get(key, 0)
    if now - last < every_s:
        return False
    _LAST[key] = now
    return True
