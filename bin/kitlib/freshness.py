"""Las dos capas de UN mecanismo de frescura (spec §6), derivadas — jamás almacenadas.

  · **capa pasiva** `review_by` = fecha del record + horizonte(volatility).
    Vencido sin re-verificar ⇒ baja un nivel de madurez: se refresca o entra
    degradado, jamás lavado (§6.1).
  · **capa activa** `refresh:` = cadencia declarada en el protocol. Al vencer,
    se programa la re-ejecución: **una versión nueva que supersede a la
    vencida, jamás una edición** (§6.2).

Ambas resuelven a una fecha y ninguna edita nada. Este módulo solo las calcula;
proponer los relanzamientos es de `check-recurrence`, y **ejecutar** es del
humano — los gates no se automatizan.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from . import vocab
from .config import Config
from .dates import add_cadence, add_months, today
from .errors import fail
from .ids import latest_artifact, load_units, unit_dirs
from .md import numbered_findings, parse_frontmatter

STATE_CURRENT = "current"
STATE_EXPIRED = "expired"
STATE_UNLABELLED = "unlabelled"


@dataclass(frozen=True)
class Expiry:
    """Un hallazgo con su `review_by` derivado."""
    unit: str
    number: str
    title: str
    date: str
    review_by: str | None
    state: str


@dataclass(frozen=True)
class Cadence:
    """Una unidad con `refresh:` declarado y su próxima re-ejecución derivada."""
    unit: str
    cadence: str
    last_close: str | None
    due: str | None
    state: str


def shortest_horizon(annotation: str, horizons: dict) -> int | None:
    mentioned = vocab.mentioned_volatilities(annotation)
    if not mentioned:
        return None
    return min(horizons[word] for word in mentioned)


def scan_findings(path: Path, horizons: dict, now: str, relative: str) -> list[Expiry]:
    meta, body = parse_frontmatter(path.read_text(encoding="utf-8"))
    date = meta.get("date")
    if not date:
        fail(f"{relative}: frontmatter sin date — no puedo derivar review_by")
    rows = []
    for number, title, segment in numbered_findings(body):
        horizon = None
        for annotation in vocab.ANNOTATION_RE.findall(segment):
            months = shortest_horizon(annotation, horizons)
            if months is not None:
                horizon = months if horizon is None else min(horizon, months)
        unit = str(meta.get("unit", "?"))
        if horizon is None:
            rows.append(Expiry(unit, number, title, str(date), None, STATE_UNLABELLED))
            continue
        review_by = add_months(str(date), horizon)
        rows.append(Expiry(unit, number, title, str(date), review_by,
                           STATE_EXPIRED if review_by < now else STATE_CURRENT))
    return rows


def expiries(config: Config, now: str | None = None) -> list[Expiry]:
    """`review_by` de cada hallazgo vigente del repo (spec §6.1)."""
    now = now or today()
    rows: list[Expiry] = []
    for unit_dir in unit_dirs(config):
        findings = latest_artifact(unit_dir, "02-findings")
        if findings.exists():
            rows.extend(scan_findings(findings, config.horizons, now,
                                      config.relative(findings)))
    return rows


def close_date(config: Config, unit) -> str | None:
    """La fecha del último cierre: el `date` del `02-findings` vigente."""
    findings = latest_artifact(unit.dir, "02-findings")
    if not findings.exists():
        return None
    meta, _ = parse_frontmatter(findings.read_text(encoding="utf-8"))
    return str(meta["date"]) if meta.get("date") else None


def cadences(config: Config, now: str | None = None) -> list[Cadence]:
    """Unidades con `refresh:` y su próxima re-ejecución derivada (spec §6.2)."""
    now = now or today()
    rows = []
    for unit in load_units(config).values():
        if not unit.refresh:
            continue
        if unit.status != "done":
            rows.append(Cadence(unit.id, unit.refresh, None, None, "not-closed"))
            continue
        last = close_date(config, unit)
        if not last:
            rows.append(Cadence(unit.id, unit.refresh, None, None, "no-close-date"))
            continue
        due = add_cadence(last, unit.refresh)
        rows.append(Cadence(unit.id, unit.refresh, last, due,
                            STATE_EXPIRED if due and due <= now else STATE_CURRENT))
    return rows


def expired(rows) -> list:
    return [row for row in rows if row.state == STATE_EXPIRED]


def unlabelled(rows) -> list:
    return [row for row in rows if row.state == STATE_UNLABELLED]
