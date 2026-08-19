"""Parsing de los markdown del framework: frontmatter, secciones y tablas.

Sin juicio: reconoce estructura, no interpreta contenido. Todo script que
lea un record pasa por acá — un solo parser, varios lectores.
"""
from __future__ import annotations

import re

FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n?", re.S)
YAML_BLOCK_RE = re.compile(r"\A(?:#[^\n]*\n+)?```yaml\n(.*?)\n```\n?", re.S)
SECTION_RE = re.compile(r"^##\s*(\d+)\.\s*(.+)$", re.M)
LIST_ITEM_RE = re.compile(r"^\s*(?:[-*]|\d+\.)\s+\S")
NUMBERED_FINDING_RE = re.compile(r"^(\d+)\.\s+\*\*", re.M)
NUMBERED_FINDING_TITLE_RE = re.compile(r"^(\d+)\.\s+\*\*(.+?)\*\*", re.M)


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Frontmatter `---`-delimitado o bloque ```yaml inicial (tras un H1).

    Devuelve (dict, cuerpo). Subconjunto YAML: escalares y listas inline —
    es lo único que un frontmatter de record usa.
    """
    match = FRONTMATTER_RE.match(text) or YAML_BLOCK_RE.match(text)
    if not match:
        return {}, text
    data = {}
    for line in match.group(1).splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        key, _, value = stripped.partition(":")
        data[key.strip()] = parse_scalar(value.strip())
    return data, text[match.end():]


def parse_scalar(value: str):
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        return [v.strip() for v in inner.split(",") if v.strip()] if inner else []
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    if value in ("null", "~", ""):
        return None
    return value


def split_sections(body: str) -> dict[int, str]:
    """`## N. Título` → {N: texto de la sección}."""
    sections = {}
    matches = list(SECTION_RE.finditer(body))
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
        sections[int(match.group(1))] = body[match.start():end]
    return sections


def section(body: str, number: int) -> str | None:
    return split_sections(body).get(number)


def split_table_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def is_separator_row(cells: list[str]) -> bool:
    return all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells if cell)


def table_rows(text: str) -> list[list[str]]:
    """Filas de la primera tabla del texto, sin separadores (encabezado incluido)."""
    rows = [split_table_row(line) for line in text.splitlines()
            if line.strip().startswith("|")]
    return [row for row in rows if not is_separator_row(row)]


def list_items(text: str) -> list[str]:
    return [line.strip() for line in text.splitlines() if LIST_ITEM_RE.match(line)]


def numbered_findings(body: str) -> list[tuple[str, str, str]]:
    """(número, título, segmento completo) por hallazgo `N. **Título.** …`."""
    out = []
    for match in NUMBERED_FINDING_TITLE_RE.finditer(body):
        number, title = match.group(1), match.group(2).rstrip(".")
        end = body.find(f"\n{int(number) + 1}. ", match.start())
        segment = body[match.start(): end if end != -1 else len(body)]
        out.append((number, title, segment))
    return out
