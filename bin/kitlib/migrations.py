"""Migraciones entre versiones del kit — el runner que consume `kit-init`.

Sintonía por migración (spec §9, principio de diseño #7): al subir de versión,
un repo puede y debería migrar TODO a la versión vigente. Acá viven solo los
pasos **mecánicos** que el runner puede aplicar sin juicio: la config (que es
evergreen y se actualiza in-place, §9.1), la estructura y los derivados.

Lo que NO vive acá, a propósito:
  · el **verbatim bronze** (`raw/`, `evidence/`, la casa de `hard-doc`, los
    payloads sellados y los `inbox/` legados) jamás se reescribe;
  · los **records de lectura** se migran por supersesión mecánica, con el diff
    como evidencia y opt-in humano — eso es `/migrate` (Fase 3.5), no esto.

Toda migración deja rastro: `kit-init` anota la entrada en el log de
migraciones del registry, con lo que quedó fuera de alcance y por qué (§9.2).
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

from .config import CONFIG_NAME, DEFAULT_CONTEXT, DEFAULT_LANGUAGE, DEFAULT_PATHS
from .vocab import HISTORICAL_VOLATILITY

SEMVER_RE = re.compile(r"^(\d+)\.(\d+)\.(\d+)")
INLINE_LIST_RE = re.compile(r"^(?P<head>\s*extra_immutable_paths:\s*)\[(?P<items>.*)\]\s*$")


@dataclass(frozen=True)
class Step:
    """Un paso mecánico: se aplica al subir A esta versión."""
    version: str
    description: str
    apply: Callable  # (config, installation, dry_run) -> list[str]


# ——— utilidades de edición del texto de la config ———
# La config es evergreen: se edita in-place conservando comentarios y orden.

def block_bounds(lines: list[str], key: str) -> tuple[int, int] | None:
    """(inicio, fin) del bloque `key:` de nivel cero; el fin es exclusivo.

    Un escalar (`kit_version: 0.1.0`) es un bloque de una sola línea; un mapa
    (`paths:`) se extiende mientras las líneas siguientes estén indentadas.
    """
    for index, line in enumerate(lines):
        match = re.match(rf"^{re.escape(key)}:(?P<rest>.*)$", line)
        if not match:
            continue
        rest = match.group("rest").strip()
        if rest and not rest.startswith("#"):
            return index, index + 1
        end = index + 1
        while end < len(lines) and lines[end].startswith((" ", "\t")):
            end += 1
        return index, end
    return None


def drop_key(lines: list[str], block: str, key: str) -> tuple[list[str], str | None]:
    """Saca `key:` de un bloque y devuelve (líneas, valor que tenía)."""
    bounds = block_bounds(lines, block)
    if not bounds:
        return lines, None
    start, end = bounds
    for index in range(start + 1, end):
        match = re.match(rf"^\s+{re.escape(key)}:\s*(?P<value>.*?)\s*$", lines[index])
        if match:
            return lines[:index] + lines[index + 1:], match.group("value")
    return lines, None


def ensure_keys(lines: list[str], block: str, entries: dict) -> tuple[list[str], list[str]]:
    """Agrega al final del bloque las claves que falten, en el orden dado."""
    bounds = block_bounds(lines, block)
    if not bounds:
        return lines, []
    start, end = bounds
    body = lines[start + 1:end]
    indent = next((line[:len(line) - len(line.lstrip())] for line in body if line.strip()),
                  "  ")
    added = [key for key in entries
             if not any(re.match(rf"^\s+{re.escape(key)}:", line) for line in body)]
    new_lines = [f"{indent}{key}: {entries[key]}" for key in added]
    return lines[:end] + new_lines + lines[end:], added


def rename_keys(lines: list[str], block: str, mapping: dict) -> tuple[list[str], list[str]]:
    """Renombra claves dentro de un bloque, conservando valor y comentarios."""
    bounds = block_bounds(lines, block)
    if not bounds:
        return lines, []
    start, end = bounds
    renamed, out = [], list(lines)
    for index in range(start + 1, end):
        match = re.match(r"^(?P<indent>\s+)(?P<key>[^:#\s]+):(?P<rest>.*)$", out[index])
        if match and match.group("key") in mapping:
            new_key = mapping[match.group("key")]
            out[index] = f"{match.group('indent')}{new_key}:{match.group('rest')}"
            renamed.append(f"{match.group('key')}→{new_key}")
    return out, renamed


def append_block(lines: list[str], after: str, text: str) -> list[str]:
    """Agrega un bloque de nivel cero (con sus comentarios) después de `after`."""
    bounds = block_bounds(lines, after)
    insert_at = bounds[1] if bounds else len(lines)
    return lines[:insert_at] + ["", *text.splitlines()] + lines[insert_at:]


def add_immutable_path(lines: list[str], path: str) -> tuple[list[str], bool]:
    """Suma una ruta a `records.extra_immutable_paths` (lista inline)."""
    for index, line in enumerate(lines):
        match = INLINE_LIST_RE.match(line)
        if not match:
            continue
        items = [item.strip() for item in match.group("items").split(",") if item.strip()]
        if path in items:
            return lines, False
        joined = ", ".join([*items, path])
        return lines[:index] + [f"{match.group('head')}[{joined}]"] + lines[index + 1:], True
    return lines, False


CONTEXT_BLOCK = """# Postura de contexto por defecto, cuando el protocol de la unidad no declara
# `context:`. Es la segunda cara del sesgo: el eco por frecuencia.
#   scoped     — integración: preflight + briefing + findings vigentes de sus
#                `needs` + protocol.
#   clean-room — exploración y unidades sensibles a falsificación: preflight +
#                protocol, NADA MÁS. Exige `needs: []`.
context:
  default: scoped"""

LANGUAGE_BLOCK = """# Idioma de PROSA de este repo (ISO 639-1). El framework es inglés: nombres de
# skill y comando, campos de contrato, claves de config, valores de enum,
# etiquetas, marks y columnas de tabla van SIEMPRE en inglés. Lo que se escribe
# en este idioma es el cuerpo de protocols, reports, findings, sources y
# payloads, la constitution del proyecto y sus ADRs, y lo que las skills le
# dicen al humano. Cambiarlo tras el primer artefacto es MIGRACIÓN, no edición.
language: en"""


def migrate_config_to_0_2(config, installation, dry_run: bool) -> list[str]:
    """Config 0.1.x → 0.2.0: enum inglés en `horizons`, casas nuevas, `language`,
    `context`, y el `inbox` legado protegido como ruta inmutable declarada."""
    path = Path(config.root) / CONFIG_NAME
    original = path.read_text(encoding="utf-8")
    lines = original.splitlines()
    changes: list[str] = []

    lines, renamed = rename_keys(lines, "horizons", HISTORICAL_VOLATILITY)
    if renamed:
        changes.append(f"{CONFIG_NAME}: horizons {', '.join(renamed)} "
                       "(enum de volatilidad en inglés — spec §1.6)")

    lines, legacy_inbox = drop_key(lines, "paths", "inbox")
    if legacy_inbox is not None:
        changes.append(f"{CONFIG_NAME}: `paths.inbox` eliminado — el único staging "
                       "es externo al repo (spec §2.6)")
        if (Path(config.root) / legacy_inbox).is_dir():
            lines, added = add_immutable_path(lines, legacy_inbox)
            if added:
                changes.append(f"{CONFIG_NAME}: `{legacy_inbox}/` legado declarado en "
                               "`records.extra_immutable_paths` — bronze congelado: "
                               "sigue protegido, no recibe nada nuevo y lo reconcilia "
                               "`/migrate` (spec §2.6, §9.1)")

    lines, added = ensure_keys(lines, "paths", {
        "evidence": DEFAULT_PATHS["evidence"],
        "hard_docs": DEFAULT_PATHS["hard_docs"],
    })
    if added:
        changes.append(f"{CONFIG_NAME}: `paths` gana {', '.join(added)} — las casas "
                       "del bronze sin unidad y de la documentación dura (spec §5)")

    if not block_bounds(lines, "context"):
        lines = append_block(lines, "runs", CONTEXT_BLOCK)
        changes.append(f"{CONFIG_NAME}: `context.default: {DEFAULT_CONTEXT}` "
                       "(bloque ratificado — spec §8.1, §12 G4)")
    if not block_bounds(lines, "language"):
        lines = append_block(lines, "kit_version", LANGUAGE_BLOCK)
        changes.append(f"{CONFIG_NAME}: `language: {DEFAULT_LANGUAGE}` — confirmalo "
                       "con el equipo: es el idioma de la prosa del repo (spec §1.8)")

    updated = "\n".join(lines) + "\n"
    if updated != original and not dry_run:
        path.write_text(updated, encoding="utf-8")
    return changes


def migrate_registries_to_0_3(config, installation, dry_run: bool) -> list[str]:
    """Registries 0.2 → 0.3: la tabla markdown pasa a datos y el `.md` a vista."""
    from . import migrations03
    return migrations03.convert(config, installation, dry_run)


#: Ordenados por versión. 0.1.0 fue la línea base.
STEPS: tuple[Step, ...] = (
    Step(
        version="0.2.0",
        description=("activación de la spec v0.3: enum inglés, casas de `evidence` "
                     "y `hard_docs`, `language`, `context` y el `inbox` fuera del "
                     "contrato"),
        apply=migrate_config_to_0_2,
    ),
    Step(
        version="0.3.0",
        description=("registries como datos: cada tabla pasa a "
                     "`registry/data/*.jsonl` y su `.md` queda como vista generada; "
                     "el régimen de §12 G6 no cambia, solo el formato"),
        apply=migrate_registries_to_0_3,
    ),
)


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
