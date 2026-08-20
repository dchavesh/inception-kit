"""Migración 0.2 → 0.3: los registries pasan a datos, y su `.md` pasa a vista.

**Reubicar no es reescribir** (spec §9.1) aplicado a la capa de registry: cada
fila de la tabla markdown se mueve, celda por celda, al archivo de datos que
ahora es el registry; nada se reinterpreta y nada se pierde. El `.md` deja de
ser el record y pasa a ser su vista generada — el régimen de §12 G6 no cambia,
solo el formato (spec, Preguntas al final #2).

Lo único que se traduce es el **dialecto** que el propio kit escribió: el
`Status` de una fila de conflicto (`abierto` → `open`), porque los valores de
enum van en inglés (principio #6). La traducción queda declarada en el rastro.

Los registries de prosa libre (migrations, qa-audits del kit 0.1.x–0.2.x) no
tenían tabla: su contenido entra como **una fila por entrada, con el texto
legado íntegro** en su campo. Un record no se reescribe: se relocaliza.
"""
from __future__ import annotations

import re

from . import registry as reg
from . import registrystore as store
from .dates import today
from .md import is_separator_row, split_table_row

COMMAND = "kit-init"
LEGACY_ENTRY_RE = re.compile(r"^##\s+(.*)$", re.M)

#: Orden de columnas con que el kit 0.1.x–0.2.x escribió cada tabla. Se lee
#: posicionalmente: es exactamente lo que el archivo legado tiene.
LEGACY_COLUMNS = {
    "requirements": reg.REQUIREMENT_KEYS,
    "conflicts": ("id", "units", "records", "description", "evidence_weight",
                  "resolution", "status", "date"),
    "supersessions": ("superseded", "superseded_by", "date", "reason"),
    "ingest_log": ("date", "destination", "class", "sha256", "origin", "outcome"),
    "gates": ("date", "gate", "decision", "amends", "record_out"),
}
LIST_SEPARATOR_RE = re.compile(r"\s*,\s*")


def table_body_rows(text: str) -> list[list[str]]:
    """Filas de datos de la tabla del registry legado (sin encabezado ni separador)."""
    rows = [split_table_row(line) for line in text.splitlines()
            if line.strip().startswith("|")]
    rows = [row for row in rows if not is_separator_row(row)]
    return rows[1:] if rows else []


def cell(value: str) -> str:
    text = value.replace("\\|", "|").strip()
    return "" if text in ("—", "-") else text


def rows_from_table(name: str, schema: reg.Registry, text: str) -> list[dict]:
    columns = LEGACY_COLUMNS[name]
    out = []
    for row in table_body_rows(text):
        if len(row) != len(columns):
            continue  # una fila que no calza con el encabezado legado no es una fila
        entry: dict = {}
        for key, raw in zip(columns, row):
            item = schema.field(key)
            value = cell(raw)
            if item and item.kind == reg.KIND_LIST:
                entry[key] = [part for part in LIST_SEPARATOR_RE.split(value) if part]
            else:
                entry[key] = value
        out.append(entry)
    return out


def rows_from_metrics(schema: reg.Registry, text: str) -> list[dict]:
    """La tabla de métricas: `Date | Unit | <columnas de la config>`, posicional."""
    keys = schema.keys
    out = []
    for row in table_body_rows(text):
        if len(row) != len(keys):
            continue
        out.append({key: cell(raw) for key, raw in zip(keys, row)})
    return out


def rows_from_prose(name: str, text: str) -> list[dict]:
    """Registries que el kit viejo escribía como prosa: una fila por bloque `## …`."""
    entries = list(LEGACY_ENTRY_RE.finditer(text))
    out = []
    for index, match in enumerate(entries):
        end = entries[index + 1].start() if index + 1 < len(entries) else len(text)
        block = text[match.start():end].strip()
        heading = match.group(1).strip()
        date_match = re.search(r"\d{4}-\d{2}-\d{2}", heading)
        date = date_match.group(0) if date_match else today()
        if name == "migrations":
            detail = [line.strip().lstrip("-").strip()
                      for line in block.splitlines()[1:] if line.strip().startswith("-")]
            out.append({"date": date, "pass": "legacy", "from_version": "—",
                        "to_version": "—", "summary": heading, "changes": detail,
                        "verification": ("entrada legada del `.md`, movida a datos con "
                                         "su texto íntegro"),
                        "out_of_scope": ""})
        else:
            out.append({"date": date, "unit": "—", "method": "legacy",
                        "sample": "—", "result": heading, "notes": block})
    return out


def normalize_conflicts(rows: list[dict]) -> tuple[list[dict], list[str]]:
    """`abierto`/`resuelto` → `open`/`resolved` (principio #6). Relabel declarado."""
    changes = []
    for row in rows:
        raw = str(row.get("status", "")).strip().lower()
        canonical = reg.HISTORICAL_CONFLICT_STATUS.get(raw)
        if canonical:
            changes.append(f"{row.get('id')}: status `{raw}` → `{canonical}`")
            row["status"] = canonical
        elif raw not in reg.CONFLICT_STATUSES:
            changes.append(f"{row.get('id')}: status `{raw or '∅'}` no reconocido → "
                           f"`{reg.CONFLICT_OPEN}` (un conflicto sin resolución "
                           "declarada está abierto)")
            row["status"] = reg.CONFLICT_OPEN
    return rows, changes


def convert(config, installation, dry_run: bool) -> list[str]:
    """Convierte los ocho registries a datos + vista. Idempotente por archivo."""
    changes: list[str] = []
    for schema in reg.data_registries(config):
        data = store.data_path(config, schema)
        if data.exists():
            continue
        view = store.view_path(config, schema)
        legacy = view.read_text(encoding="utf-8") if view.exists() else ""
        if schema.name == "metrics":
            rows = rows_from_metrics(schema, legacy)
        elif schema.name in LEGACY_COLUMNS:
            rows = rows_from_table(schema.name, schema, legacy)
        else:
            rows = rows_from_prose(schema.name, legacy)
        if schema.name == "conflicts":
            rows, relabelled = normalize_conflicts(rows)
            changes.extend(relabelled)
        if dry_run:
            changes.append(f"{config.relative(data)}: {len(rows)} fila(s) desde la "
                           "tabla legada (dry-run)")
            continue
        store.write(config, schema, rows, COMMAND)
        changes.append(f"{config.relative(data)}: registry convertido a datos "
                       f"({len(rows)} fila(s)); `{config.relative(view)}` pasa a ser "
                       "su vista generada")
    return changes
