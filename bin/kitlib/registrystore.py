"""Lectura, escritura, validación y renderizado de los registries-como-datos.

El archivo de datos (`<registry>/data/<name>.jsonl`) es la fuente; el `.md` es
**vista generada** y jamás se edita a mano. Todo escritor del kit pasa por acá:
valida contra el schema, escribe la línea y re-renderiza la vista — un contrato,
un lugar, varios lectores.

Los tres regímenes de spec §12 G6 se verifican sobre los datos:
`append_only_violation` (el contenido previo no se pisa) y
`markable_violations` (la fila no se borra ni cambia lo que afirmó). La guarda
de integridad los consume tal cual, sin re-implementar nada.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

from . import registry as reg
from .config import Config
from .dates import today
from .errors import fail
from .phrases import has_table, phrase, stamp

ISO_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
CELL_BREAK = "<br>"


# ——— rutas ———

def data_dir(config: Config) -> Path:
    return config.registry / reg.DATA_DIR


def data_path(config: Config, schema: reg.Registry) -> Path:
    return data_dir(config) / schema.data_name


def view_path(config: Config, schema: reg.Registry) -> Path:
    return config.registry / schema.view_name


# ——— (de)serialización ———

def dump(schema: reg.Registry, rows: list) -> str:
    """JSON Lines determinista: una fila por línea, campos en orden de schema."""
    lines = []
    for row in rows:
        ordered = {key: row[key] for key in schema.keys if key in row}
        ordered.update({key: value for key, value in row.items() if key not in ordered})
        lines.append(json.dumps(ordered, ensure_ascii=False, sort_keys=False))
    return "".join(line + "\n" for line in lines)


def parse(text: str, schema: reg.Registry, source: str) -> tuple:
    """(filas, problemas). Una línea ilegible es un problema, jamás un descarte."""
    rows, problems = [], []
    for number, line in enumerate(text.splitlines(), start=1):
        if not line.strip():
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError as error:
            problems.append(f"{source}:{number}: JSON inválido — {error.msg}")
            continue
        if not isinstance(value, dict):
            problems.append(f"{source}:{number}: se esperaba un objeto JSON por línea")
            continue
        rows.append(value)
    return rows, problems


def read(config: Config, schema: reg.Registry) -> list:
    path = data_path(config, schema)
    if not path.is_file():
        return []
    rows, problems = parse(path.read_text(encoding="utf-8"), schema,
                           config.relative(path))
    if problems:
        fail(f"{config.relative(path)}: datos ilegibles\n  - " + "\n  - ".join(problems))
    return rows


# ——— validación contra schema ———

def validate(schema: reg.Registry, rows: list, source: str) -> list[str]:
    problems: list[str] = []
    declared = set(schema.keys)
    seen: dict = {}
    for number, row in enumerate(rows, start=1):
        label = f"{source}:{number}"
        unknown = sorted(set(row) - declared)
        if unknown:
            problems.append(f"{label}: campo(s) fuera del schema: {unknown} — "
                            f"el schema de `{schema.name}` es {list(schema.keys)}")
        for item in schema.fields:
            value = row.get(item.key)
            if value in (None, "") and item.required:
                problems.append(f"{label}: falta `{item.key}` (obligatorio)")
                continue
            if value in (None, ""):
                continue
            problems.extend(kind_problems(label, item, value))
        if schema.key:
            identifier = row.get(schema.key)
            if identifier in seen:
                problems.append(f"{label}: `{schema.key}` duplicado ({identifier}) — "
                                f"ya está en la línea {seen[identifier]}; los IDs son "
                                "permanentes y únicos")
            elif identifier:
                seen[identifier] = number
    return problems


def kind_problems(label: str, item: reg.Field, value) -> list[str]:
    if item.kind == reg.KIND_LIST:
        if not isinstance(value, list) or not all(isinstance(v, str) for v in value):
            return [f"{label}: `{item.key}` debe ser una lista de strings"]
        return []
    if item.kind == reg.KIND_INT:
        if isinstance(value, bool) or not isinstance(value, int):
            return [f"{label}: `{item.key}` debe ser un entero"]
        return []
    if not isinstance(value, str):
        return [f"{label}: `{item.key}` debe ser texto"]
    if item.kind == reg.KIND_DATE and not ISO_DATE_RE.match(value):
        return [f"{label}: `{item.key}` debe ser una fecha ISO YYYY-MM-DD, no '{value}'"]
    if item.choices and value not in item.choices:
        return [f"{label}: `{item.key}: {value}` fuera del set cerrado "
                f"{list(item.choices)} — los valores de enum van en inglés y sin "
                "dialecto (spec §0.1 #6)"]
    return []


# ——— regímenes (spec §12 G6), verificados sobre los datos ———

def append_only_violation(previous: str, current: str) -> str | None:
    """Append-only: el contenido previo no se pisa — el nuevo empieza con el viejo."""
    head = previous.rstrip("\n")
    if not head:
        return None
    if not current.startswith(head):
        return ("record append-only — el contenido previo no se pisa: se agrega al "
                "final (spec §12 G6)")
    return None


def markable_violations(schema: reg.Registry, previous: list, current: list) -> list[str]:
    """Markable: la fila jamás se borra y solo mutan los campos marcables."""
    problems = []
    index = {row.get(schema.key): row for row in current}
    for row in previous:
        identifier = row.get(schema.key)
        updated = index.get(identifier)
        if updated is None:
            problems.append(f"{identifier}: fila eliminada — un record marcable se "
                            "marca, jamás se borra (spec §12 G6)")
            continue
        changed = sorted(key for key in set(row) | set(updated)
                         if row.get(key) != updated.get(key))
        illegal = [key for key in changed if key not in schema.markable]
        if illegal:
            problems.append(f"{identifier}: campo(s) no marcable(s) modificado(s) "
                            f"{illegal} — marcables: {list(schema.markable)}; el ID y "
                            "lo que la fila afirmó no cambian (spec §12 G6)")
    return problems


# ——— vista generada ———

def escape(value) -> str:
    if isinstance(value, list):
        value = ", ".join(str(item) for item in value)
    text = "" if value is None else str(value)
    return text.replace("|", "\\|").replace("\n", CELL_BREAK) or "—"


def render(config: Config, schema: reg.Registry, rows: list, command: str) -> str:
    language = config.language
    data = f"{config.relative(config.registry)}/{reg.DATA_DIR}/{schema.data_name}"
    lines = [f"# Registry — {registry_title(schema)}", ""]
    if not has_table(language):
        lines += ["> " + phrase(language, "language-fallback", language=language,
                               fallback="en"), ""]
    lines += [
        stamp(language, command, today(), phrase(language, "registry-source", path=data)),
        "",
        f"**Regime:** `{schema.regime}` — spec {schema.spec}.",
        "",
    ]
    if schema.name == "metrics":
        lines += [f"<!-- metrics-version: {config.metrics_version} -->", ""]
    lines.append("| " + " | ".join(schema.labels) + " |")
    lines.append("|" + "|".join("---" for _ in schema.labels) + "|")
    for row in rows:
        lines.append("| " + " | ".join(escape(row.get(item.key))
                                       for item in schema.fields) + " |")
    return "\n".join(lines) + "\n"


def registry_title(schema: reg.Registry) -> str:
    """El nombre del registry es nombre de concepto: va en inglés (principio #6)."""
    return {
        "requirements": "Requirements (RTM)",
        "conflicts": "Conflicts",
        "metrics": "Metrics",
        "supersessions": "Supersessions",
        "ingest_log": "Ingest log",
        "migrations": "Migrations",
        "qa_audits": "QA audits",
        "gates": "Gates",
    }[schema.name]


# ——— escritura ———

def write(config: Config, schema: reg.Registry, rows: list, command: str) -> None:
    """Escribe los datos y re-renderiza la vista. Nadie escribe la vista a mano."""
    problems = validate(schema, rows, schema.data_name)
    if problems:
        fail(f"{schema.data_name}: filas fuera de schema\n  - " + "\n  - ".join(problems))
    path = data_path(config, schema)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(dump(schema, rows), encoding="utf-8")
    view = view_path(config, schema)
    view.parent.mkdir(parents=True, exist_ok=True)
    view.write_text(render(config, schema, rows, command), encoding="utf-8")


def append(config: Config, name: str, new_rows: list, command: str) -> list:
    schema = reg.schemas(config)[name]
    if schema.regime == reg.REGIME_DERIVED:
        fail(f"{name}: es vista derivada — no recibe filas (spec §12 G6)")
    rows = read(config, schema) + [dict(row) for row in new_rows]
    write(config, schema, rows, command)
    return rows


def mark(config: Config, name: str, identifier: str, updates: dict,
         command: str) -> dict:
    """Marca una fila de un registry marcable. Solo campos declarados `markable`."""
    schema = reg.schemas(config)[name]
    if schema.regime != reg.REGIME_MARKABLE:
        fail(f"{name}: régimen `{schema.regime}` — solo un record marcable se marca "
             "(spec §12 G6)")
    illegal = sorted(set(updates) - set(schema.markable))
    if illegal:
        fail(f"{name}: campo(s) no marcable(s) {illegal} — marcables: "
             f"{list(schema.markable)} (spec §12 G6)")
    rows = read(config, schema)
    target = next((row for row in rows if row.get(schema.key) == identifier), None)
    if target is None:
        fail(f"{name}: no hay fila con `{schema.key}: {identifier}`")
    target.update(updates)
    write(config, schema, rows, command)
    return target


def render_all(config: Config, command: str) -> list[str]:
    """Regenera todas las vistas de registry desde sus datos. Derivados (§9.1)."""
    written = []
    for schema in reg.data_registries(config):
        rows = read(config, schema)
        view = view_path(config, schema)
        content = render(config, schema, rows, command)
        if view.exists() and view.read_text(encoding="utf-8") == content:
            continue
        view.parent.mkdir(parents=True, exist_ok=True)
        view.write_text(content, encoding="utf-8")
        written.append(config.relative(view))
    return written


def seed(config: Config, command: str) -> list[str]:
    """Siembra los archivos de datos vacíos y sus vistas. Idempotente."""
    created = []
    for schema in reg.data_registries(config):
        path = data_path(config, schema)
        if path.exists():
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("", encoding="utf-8")
        created.append(config.relative(path))
    created.extend(render_all(config, command))
    return created
