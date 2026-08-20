"""El sidecar de procedencia y su anotación de migración (spec §2.2, §9.2).

**La incisión va SIEMPRE al sidecar, jamás dentro del verbatim**: un byte
añadido al record rompe la cadena `sha256` que hace auditable cada afirmación
que lo cita. Por eso una migración que toca un record deja su marca acá al lado.

El sidecar es **append-only**: lo que ya declaró no se pisa; una anotación nueva
se agrega al final con su número. Si el record no tenía sidecar —el caso de un
`01-report` o un `02-findings`, que no son binarios— se crea con la anotación
como primera entrada.
"""
from __future__ import annotations

import re
from pathlib import Path

from .dates import today

SUFFIX = ".meta.yaml"
ANNOTATION_RE = re.compile(r"^annotation_(\d+):", re.M)
FIELD_RE = re.compile(r"^(\s*)([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$")
HEADER = ("# Sidecar de procedencia — inception-kit (spec §2.2, §9.2).\n"
          "# Append-only: acá se AGREGA, nunca se pisa. El record de al lado no se\n"
          "# edita jamás — la incisión de una migración vive en este archivo.\n")

#: Nombre del pase con el que `/distill` declara la destilación de un bronze
#: (spec §2.4). Material cargado sin destilación declarada es **deuda**: no se
#: prohíbe cargar sin destilar, se prohíbe olvidarlo — y esta anotación es la
#: forma en que deja de estar olvidado.
DISTILL_PASS = "distill"


def path_for(record: Path) -> Path:
    return Path(f"{record}{SUFFIX}")


def next_number(text: str) -> int:
    numbers = [int(number) for number in ANNOTATION_RE.findall(text)]
    return max(numbers, default=0) + 1


def annotate(record: Path, note: str, pass_name: str,
             superseded_by: str | None = None, date: str | None = None,
             extra: dict | None = None) -> Path:
    """Agrega una anotación al sidecar del record. Lo crea si falta."""
    target = path_for(record)
    existing = target.read_text(encoding="utf-8") if target.exists() else HEADER
    number = next_number(existing)
    block = [f"annotation_{number}:",
             f"  date: {date or today()}",
             f"  pass: {pass_name}",
             f"  note: {note}"]
    if superseded_by:
        block.append(f"  superseded_by: {superseded_by}")
    block.extend(f"  {key}: {value}" for key, value in (extra or {}).items())
    target.write_text(existing.rstrip("\n") + "\n" + "\n".join(block) + "\n",
                      encoding="utf-8")
    return target


def read(text: str) -> tuple[dict, list]:
    """(cabecera, anotaciones) de un sidecar. Lector propio: jamás falla.

    Se lee con un parser mínimo y no con el de la config a propósito: un scan
    recorre todos los sidecares del repo, y un sidecar raro tiene que salir
    reportado, no tumbar la corrida.
    """
    header: dict = {}
    annotations: list = []
    current: dict | None = None
    for line in text.splitlines():
        match = FIELD_RE.match(line)
        if not match:
            continue
        indent, key, value = match.group(1), match.group(2), match.group(3).strip()
        if not indent:
            current = {} if ANNOTATION_RE.match(f"{key}:") else None
            if current is not None:
                annotations.append(current)
            else:
                header[key] = value
        elif current is not None:
            current[key] = value
    return header, annotations


def load(record: Path) -> tuple[dict, list]:
    target = path_for(record)
    if not target.is_file():
        return {}, []
    return read(target.read_text(encoding="utf-8"))


def distillations(record: Path) -> list:
    """Las destilaciones ya declaradas para este bronze (spec §2.4)."""
    _, annotations = load(record)
    return [entry for entry in annotations if entry.get("pass") == DISTILL_PASS]


def provenance(origin: str, source_class: str, digest: str, note: str,
               kit_version: str, date: str | None = None) -> str:
    """Sidecar de un bronze reubicado: de dónde venía, qué es y su hash verificado."""
    return HEADER + "\n".join([
        f"class: {source_class}",
        f"origin: {origin}",
        f"date: {date or today()}",
        "method: migrate relocate",
        f"sha256: {digest}",
        f"note: {note}",
        f"kit_version: {kit_version}",
    ]) + "\n"
