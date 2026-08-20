"""El índice puerta-de-entrada: la vista raíz generada (spec §1.2, §4.5).

Responde en UNA página, sin abrir nada: qué hay y en qué estado (tablero),
qué está decidido (ADRs vigentes), qué está en disputa (conflictos abiertos),
qué síntesis rige, y dónde vive cada clase de cosa.

**Es vista derivada, jamás una segunda casa** (§4.5, regla de entrada): todo lo
que muestra sale de la config, los protocols, los registries y los ADRs, y
ninguna regla vive acá — solo el atajo para encontrarla. Si se borra, no se
pierde nada más que el atajo. Por eso tampoco se edita a mano: se regenera.

La prosa va en el idioma que declare `language`; las columnas, los IDs y los
valores de enum, siempre en inglés (§1.8).
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from . import freshness
from . import registry as reg
from . import registrystore as store
from .config import CONFIG_NAME, Config
from .dates import today
from .md import parse_frontmatter
from .phrases import has_table, phrase, stamp
from .status import board_rows

INDEX_NAME = "INDEX.md"
COMMAND = "derive-index"
ADR_GLOB = "adr-*.md"
BOLD_LABEL_RE = re.compile(r"^\*\*[^*]+:\*\*\s*")
HEADING_RE = re.compile(r"^#\s+(.+)$", re.M)
OBJECTIVE_LIMIT = 140


@dataclass(frozen=True)
class Decision:
    id: str
    title: str
    date: str
    superseded_by: str | None


def index_path(config: Config) -> Path:
    return config.root / INDEX_NAME


# ——— insumos ———

def objective(protocol: Path) -> str:
    """El objetivo en una línea: el primer párrafo del cuerpo, sin su etiqueta.

    Se lee por ESTRUCTURA y no por palabra, porque la prosa del protocol está
    en el idioma del repo (§1.8): título, línea en blanco, objetivo.
    """
    _, body = parse_frontmatter(protocol.read_text(encoding="utf-8"))
    for block in re.split(r"\n\s*\n", body.strip()):
        text = block.strip()
        if not text or text.startswith("#") or text.startswith("<!--"):
            continue
        line = BOLD_LABEL_RE.sub("", " ".join(text.split()))
        return line[:OBJECTIVE_LIMIT] + ("…" if len(line) > OBJECTIVE_LIMIT else "")
    return "—"


def decisions(config: Config) -> tuple:
    """(ADRs vigentes, ADRs superados).

    Un ADR queda superado por tres vías, todas declaradas y ninguna inferida:
    una fila del registry de supersesiones, el `supersedes:` de otro ADR, o su
    propio `status:` MADR. Superado se marca, jamás se borra (§0.2 #2).
    """
    if not config.decisions.is_dir():
        return (), ()
    by_registry = {str(row.get("superseded", "")): str(row.get("superseded_by", ""))
                   for row in store.read(config, reg.SUPERSESSIONS)}

    parsed = []
    for path in sorted(config.decisions.glob(ADR_GLOB)):
        meta, body = parse_frontmatter(path.read_text(encoding="utf-8"))
        heading = HEADING_RE.search(body)
        parsed.append((path, meta,
                       str(meta.get("id") or path.stem),
                       str(meta.get("title") or (heading.group(1) if heading
                                                 else path.stem))))
    by_peer = {str(meta.get("supersedes")): identifier
               for _, meta, identifier, _ in parsed if meta.get("supersedes")}

    resolved = []
    for path, meta, identifier, title in parsed:
        keys = (identifier, path.stem, path.name)
        superseded_by = next((by_registry[key] for key in keys if key in by_registry),
                             None)
        superseded_by = superseded_by or next(
            (by_peer[key] for key in keys if key in by_peer), None)
        if not superseded_by and "superseded" in str(meta.get("status", "")).lower():
            superseded_by = str(meta.get("superseded-by")
                                or meta.get("superseded_by") or "—")
        resolved.append(Decision(identifier, title, str(meta.get("date") or "—"),
                                 superseded_by))
    return (tuple(d for d in resolved if not d.superseded_by),
            tuple(d for d in resolved if d.superseded_by))


def open_conflicts(config: Config) -> list:
    return [row for row in store.read(config, reg.CONFLICTS)
            if row.get("status") != reg.CONFLICT_RESOLVED]


def current_synthesis(config: Config) -> dict | None:
    """La última síntesis emitida = la última fila del gate `synthesis` (§11.1)."""
    rows = [row for row in store.read(config, reg.GATES)
            if reg.is_synthesis_gate(row.get("gate"))]
    return rows[-1] if rows else None


# ——— render ———

def build_index(config: Config) -> str:
    language = config.language
    lines = [f"# {phrase(language, 'index-title')}", ""]
    if not has_table(language):
        lines += ["> " + phrase(language, "language-fallback", language=language,
                                fallback="en"), ""]
    lines += [
        stamp(language, COMMAND, today(), phrase(language, "index-source")),
        "",
        phrase(language, "index-lead"),
        "",
    ]
    lines += board_section(config, language)
    lines += decisions_section(config, language)
    lines += conflicts_section(config, language)
    lines += synthesis_section(config, language)
    lines += freshness_section(config, language)
    lines += houses_section(config, language)
    return "\n".join(lines).rstrip("\n") + "\n"


def board_section(config: Config, language: str) -> list[str]:
    from .ids import load_units
    units = load_units(config)
    rows, _, _ = board_rows(config)
    lines = [f"## {phrase(language, 'index-board')}", "",
             "| Unit | Slug | Objective | Status | Ready |",
             "|---|---|---|---|---|"]
    for unit_id, status, _, ready, _ in rows:
        unit = units[unit_id]
        lines.append(f"| {unit_id} | {unit.slug} | "
                     f"{store.escape(objective(unit.path))} | {status} | {ready} |")
    if not rows:
        lines.append("| — | — | — | — | — |")
    lines.append("")
    return lines


def decisions_section(config: Config, language: str) -> list[str]:
    current, superseded = decisions(config)
    lines = [f"## {phrase(language, 'index-decisions')}", ""]
    if not current and not superseded:
        return lines + [phrase(language, "index-decisions-empty"), ""]
    lines += ["| ID | Title | Date |", "|---|---|---|"]
    for decision in current:
        lines.append(f"| {decision.id} | {store.escape(decision.title)} "
                     f"| {decision.date} |")
    if not current:
        lines.append("| — | — | — |")
    lines.append("")
    if superseded:
        lines.append("<details><summary>superseded ("
                     f"{len(superseded)})</summary>\n")
        lines += ["| ID | Superseded by |", "|---|---|"]
        lines += [f"| {d.id} | {d.superseded_by} |" for d in superseded]
        lines.append("\n</details>")
        lines.append("")
    return lines


def conflicts_section(config: Config, language: str) -> list[str]:
    rows = open_conflicts(config)
    lines = [f"## {phrase(language, 'index-conflicts')}", ""]
    if not rows:
        return lines + [phrase(language, "index-conflicts-empty"), ""]
    lines += ["| ID | Units | Description | Status |", "|---|---|---|---|"]
    for row in rows:
        lines.append(f"| {row.get('id')} | {store.escape(row.get('units'))} "
                     f"| {store.escape(row.get('description'))} "
                     f"| {row.get('status')} |")
    lines.append("")
    return lines


def synthesis_section(config: Config, language: str) -> list[str]:
    row = current_synthesis(config)
    lines = [f"## {phrase(language, 'index-synthesis')}", ""]
    if not row:
        return lines + [phrase(language, "index-synthesis-empty"), ""]
    lines += [f"- **{row.get('date')}** — {row.get('decision')}",
              f"- **Record out:** {row.get('record_out')}", ""]
    return lines


def freshness_section(config: Config, language: str) -> list[str]:
    expired = freshness.expired(freshness.expiries(config))
    due = freshness.expired(freshness.cadences(config))
    lines = [f"## {phrase(language, 'index-freshness')}", ""]
    if not expired and not due:
        return lines + [phrase(language, "index-freshness-ok"), ""]
    return lines + [phrase(language, "index-freshness-due", expired=len(expired),
                           refresh=len(due)), ""]


def houses_section(config: Config, language: str) -> list[str]:
    lines = [f"## {phrase(language, 'index-houses')}", "",
             phrase(language, "index-houses-lead"), "",
             f"| {phrase(language, 'index-column-what')} "
             f"| {phrase(language, 'index-column-where')} |",
             "|---|---|"]
    for name, value in config.data["paths"].items():
        lines.append(f"| `paths.{name}` | `{value}` |")
    registry = config.relative(config.registry)
    lines += [
        f"| contract & anchor | `{CONFIG_NAME}` |",
        f"| registries (data) | `{registry}/{reg.DATA_DIR}/*{reg.DATA_SUFFIX}` |",
        f"| registries (views) | `{registry}/*.md` |",
        f"| board | `{config.relative(config.registry_file('status'))}` |",
        f"| this index | `{INDEX_NAME}` |",
        f"| the spec | inception-kit `SPEC.md` (kit {config.kit_version}) |",
        "",
    ]
    return lines
