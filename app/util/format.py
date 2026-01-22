"""Utilite: formatage; fonctionnement: helpers pour ms/dates lisibles."""

from datetime import datetime


def fmt_ms(value: float | None) -> str:
    if value is None:
        return "-"
    return f"{value:.1f} ms"


def fmt_dt(value: str | None) -> str:
    if not value:
        return "-"
    try:
        return datetime.fromisoformat(value).strftime("%Y-%m-%d %H:%M:%S")
    except ValueError:
        return value
