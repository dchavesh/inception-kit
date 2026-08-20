"""Destilación declarada (spec §2.4) — qué bronze tiene silver y qué es deuda.

Toda clase declara su flujo bronze → silver → gold. **Material cargado sin
destilación declarada es deuda**: entra al repo, queda registrado (su fila del
ingest-log) y aparece como pendiente. No se prohíbe cargar sin destilar; se
prohíbe olvidarlo — y «aparecer como pendiente» es literalmente esto.

Dónde se busca: la casa del bronze sin unidad (`<research>/evidence/<class>/`) y
el `raw/` de cada unidad. Dos exenciones, las dos de la spec:

  · la **documentación dura** no tiene obligación de silver ni de gold (§2.3):
    es fuente de record, y su casa ni se recorre;
  · el **verbatim de una corrida** (`raw/run-NN.md`) no lleva sidecar de
    procedencia porque su destilación es el ciclo normal —report y findings— y
    la hace `/close`. No aparece acá porque no hay sidecar que lo declare.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from . import sidecar
from .config import Config
from .vocab import HARD_DOC_CLASS


@dataclass(frozen=True)
class Bronze:
    path: Path
    relative: str
    source_class: str
    origin: str
    date: str
    distillations: tuple

    @property
    def is_distilled(self) -> bool:
        return bool(self.distillations)


def sidecar_files(config: Config) -> list:
    """Los sidecares de procedencia del repo, sin la casa de la hard-doc."""
    found = []
    if config.evidence.is_dir():
        found.extend(config.evidence.rglob(f"*{sidecar.SUFFIX}"))
    if config.investigations.is_dir():
        found.extend(config.investigations.glob(f"*/raw/*{sidecar.SUFFIX}"))
    return sorted(found)


def bronzes(config: Config) -> list:
    """El bronze con procedencia declarada, con su estado de destilación."""
    found = []
    for note in sidecar_files(config):
        record = Path(str(note)[: -len(sidecar.SUFFIX)])
        header, annotations = sidecar.read(note.read_text(encoding="utf-8"))
        if header.get("class") == HARD_DOC_CLASS:
            continue
        found.append(Bronze(
            path=record,
            relative=config.relative(record),
            source_class=header.get("class", "?"),
            origin=header.get("origin", "?"),
            date=header.get("date", "?"),
            distillations=tuple(entry for entry in annotations
                                if entry.get("pass") == sidecar.DISTILL_PASS),
        ))
    return found


def pending(config: Config) -> list:
    """La deuda: bronze cargado sin destilación declarada (spec §2.4)."""
    return [item for item in bronzes(config) if not item.is_distilled]
