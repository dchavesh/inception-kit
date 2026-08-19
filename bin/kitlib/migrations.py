"""Migraciones entre versiones del kit — el runner que consume `kit-init`.

Sintonía por migración (principio #7): al subir de versión, un repo puede y
debería migrar TODO a la versión vigente. Acá viven solo los pasos MECÁNICOS
que el runner puede aplicar sin juicio (config, derivados, estructura).

Lo que NO vive acá, a propósito:
  · el **verbatim bronze** (raw/, inbox/, payloads sellados) jamás se reescribe;
  · los **records de lectura** se migran por supersesión mecánica, con el diff
    como evidencia y opt-in humano — eso es `/migrate` (Fase 3.5), no esto.

Toda migración deja rastro: `kit-init` anota la entrada en el log de
migraciones del registry. En 0.1.0 no hay pasos: es la línea base.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Callable

SEMVER_RE = re.compile(r"^(\d+)\.(\d+)\.(\d+)")


@dataclass(frozen=True)
class Step:
    """Un paso mecánico: se aplica al subir A esta versión."""
    version: str
    description: str
    apply: Callable  # (config, installation, dry_run) -> list[str]


#: Ordenados por versión. 0.1.0 es la línea base — nada que migrar todavía.
STEPS: tuple[Step, ...] = ()


def parse_version(version: str) -> tuple:
    match = SEMVER_RE.match(str(version or "0.0.0"))
    if not match:
        return (0, 0, 0)
    return tuple(int(part) for part in match.groups())


def pending(installed: str | None, target: str) -> list[Step]:
    """Pasos con versión en (installed, target]."""
    if installed is None:
        return []  # instalación nueva: nace en la versión vigente
    low, high = parse_version(installed), parse_version(target)
    return [step for step in STEPS if low < parse_version(step.version) <= high]
