"""Aritmética de fechas ISO sin dependencias.

`review_by` jamás se almacena (spec §6.1): se deriva de la fecha del record
más el horizonte de su volatilidad. Este módulo es toda la matemática que
esa derivación necesita.
"""
from __future__ import annotations

import datetime
import re

DAYS_IN_MONTH = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)


def today() -> str:
    return datetime.date.today().isoformat()


def is_leap(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year: int, month: int) -> int:
    if month == 2 and is_leap(year):
        return 29
    return DAYS_IN_MONTH[month - 1]


def add_months(iso_date: str, months: int) -> str:
    """`2026-01-31` + 1 mes → `2026-02-28` (el día se recorta, nunca desborda)."""
    year, month, day = (int(part) for part in iso_date.split("-"))
    total = (month - 1) + months
    year, month = year + total // 12, total % 12 + 1
    return f"{year:04d}-{month:02d}-{min(day, days_in_month(year, month)):02d}"


def add_weeks(iso_date: str, weeks: int) -> str:
    base = datetime.date.fromisoformat(iso_date)
    return (base + datetime.timedelta(weeks=weeks)).isoformat()


#: Gramática de la cadencia de `refresh:` (spec §6.2): `<N><w|m|y>`. La cadencia
#: se declara; la FECHA se deriva de ella más el último cierre — un valor
#: derivado almacenado se pudre (principio de operación #1).
CADENCE_RE = re.compile(r"^(\d+)([wmy])$")


def parse_cadence(raw: str) -> tuple[int, str] | None:
    match = CADENCE_RE.match(str(raw or "").strip().lower())
    return (int(match.group(1)), match.group(2)) if match else None


def add_cadence(iso_date: str, cadence: str) -> str | None:
    parsed = parse_cadence(cadence)
    if not parsed:
        return None
    amount, unit = parsed
    if unit == "w":
        return add_weeks(iso_date, amount)
    return add_months(iso_date, amount * (12 if unit == "y" else 1))
