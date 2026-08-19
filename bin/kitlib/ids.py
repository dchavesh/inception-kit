"""Gramática de IDs y carga de unidades.

El ID es **llave estable y tonta**: `<prefijo><NN>[letra]` + slug. El
significado vive en el slug y el índice, jamás dentro del ID (los smart codes
se rechazan: el significado embebido se pudre y los IDs nunca se renombran).

Dos reglas duras del plan viven acá:
  · `id_width` es el ancho **mínimo**: al desbordar, el ancho crece
    (`r99` → `r100`) y NADA se renumera;
  · el orden es **SIEMPRE numérico**, jamás lexicográfico — por eso nadie
    ordena con `sorted(glob(...))`, sino con `unit_sort_key`.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from .config import STATUS_ORDER, Config
from .errors import fail
from .md import parse_frontmatter

UNIT_PARTS_RE = re.compile(r"^([a-z]+)(\d+)([a-z]?)$")
VERSIONED_RE = re.compile(r"\.v(\d+)\.md$")


def unit_pattern(config: Config) -> re.Pattern:
    prefixes = "|".join(sorted(config.id_classes, key=len, reverse=True))
    return re.compile(rf"^(?:{prefixes})\d{{{config.id_width},}}[a-z]?$")


def sub_id_pattern(config: Config, kind: str, unit_id: str | None = None) -> re.Pattern:
    """`rNN-srcNN` / `rNN-reqNN` / `rNN-conNN` — un solo esquema de namespacing."""
    prefixes = "|".join(sorted(config.id_classes, key=len, reverse=True))
    unit = re.escape(unit_id) if unit_id else rf"(?:{prefixes})\d{{{config.id_width},}}[a-z]?"
    return re.compile(rf"{unit}-{kind}\d{{{config.id_width},}}")


def registry_id_pattern(config: Config, kind: str) -> re.Pattern:
    """IDs centrales del registry (`con-NN`) — sin namespace de unidad."""
    return re.compile(rf"^{kind}-\d{{{config.id_width},}}$")


def unit_sort_key(unit_id: str) -> tuple:
    """Orden SIEMPRE numérico: `r9` < `r10` < `r100`; `r00a` < `r00b`."""
    match = UNIT_PARTS_RE.match(unit_id)
    if not match:
        return (unit_id, 0, "")
    return (match.group(1), int(match.group(2)), match.group(3))


def is_valid_unit_id(config: Config, unit_id: str) -> bool:
    return bool(unit_id and unit_pattern(config).match(unit_id))


@dataclass(frozen=True)
class Unit:
    id: str
    slug: str
    status: str
    needs: tuple
    inputs: tuple
    constitution: str | None
    session: str | None
    runs: int
    mode: str
    path: Path

    @property
    def dir(self) -> Path:
        return self.path.parent

    @property
    def run_labels(self) -> tuple:
        return tuple(f"run-{index:02d}" for index in range(1, self.runs + 1))


def load_units(config: Config) -> dict[str, Unit]:
    """Todas las unidades del repo, en orden numérico."""
    pattern = unit_pattern(config)
    units: dict[str, Unit] = {}
    if not config.investigations.is_dir():
        return units
    for protocol in config.investigations.glob("*/00-protocol.md"):
        meta, _ = parse_frontmatter(protocol.read_text(encoding="utf-8"))
        unit_id = meta.get("id")
        if not unit_id or not pattern.match(str(unit_id)):
            fail(f"{config.relative(protocol)}: frontmatter sin id válido "
                 f"(gramática: {pattern.pattern})")
        if meta.get("status") not in STATUS_ORDER:
            fail(f"{config.relative(protocol)}: status inválido: {meta.get('status')}")
        units[unit_id] = Unit(
            id=unit_id,
            slug=meta.get("slug") or protocol.parent.name.split("-", 1)[-1],
            status=meta["status"],
            needs=tuple(meta.get("needs") or []),
            inputs=tuple(meta.get("inputs") or []),
            constitution=meta.get("constitution"),
            session=meta.get("session"),
            runs=parse_runs(config, meta, protocol),
            mode=parse_mode(config, meta, protocol),
            path=protocol,
        )
    return {unit_id: units[unit_id] for unit_id in sorted(units, key=unit_sort_key)}


def parse_runs(config: Config, meta: dict, protocol: Path) -> int:
    raw = meta.get("runs")
    if raw is None:
        return config.runs_default
    try:
        runs = int(str(raw))
    except ValueError:
        fail(f"{config.relative(protocol)}: `runs: {raw}` no es un entero")
    if runs < 1:
        fail(f"{config.relative(protocol)}: `runs: {runs}` — mínimo 1")
    return runs


def parse_mode(config: Config, meta: dict, protocol: Path) -> str:
    from .config import RUN_MODES
    mode = meta.get("mode") or config.runs_default_mode
    if mode not in RUN_MODES:
        fail(f"{config.relative(protocol)}: `mode: {mode}` — uno de {list(RUN_MODES)}")
    return mode


def find_unit_dir(config: Config, unit_id: str) -> Path:
    matches = sorted(config.investigations.glob(f"{unit_id}-*"))
    if len(matches) != 1:
        fail(f"unidad {unit_id}: esperaba exactamente un directorio en "
             f"{config.relative(config.investigations)}, hay {len(matches)}")
    return matches[0]


def unit_dirs(config: Config) -> list[Path]:
    """Directorios de unidad en orden numérico (jamás lexicográfico)."""
    if not config.investigations.is_dir():
        return []
    dirs = [path for path in config.investigations.iterdir()
            if path.is_dir() and (path / "00-protocol.md").exists()]
    return sorted(dirs, key=lambda path: unit_sort_key(path.name.split("-", 1)[0]))


def latest_artifact(unit_dir: Path, stem: str) -> Path:
    """Versión vigente de un artefacto: mayor `NN-kind.vN.md`, o la base.

    Supersesión (spec §1.2): las versiones anteriores nunca se borran; quedan
    marcadas en `registry/supersessions.md`. Los scripts operan sobre la vigente.
    """
    versioned = []
    for path in unit_dir.glob(f"{stem}.v*.md"):
        match = VERSIONED_RE.search(path.name)
        if match:
            versioned.append((int(match.group(1)), path))
    if versioned:
        return max(versioned)[1]
    return unit_dir / f"{stem}.md"


def is_ready(unit: Unit, units: dict[str, Unit]) -> bool:
    return all(need in units and units[need].status == "done" for need in unit.needs)
