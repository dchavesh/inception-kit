"""Lector de un SUBCONJUNTO de YAML — solo lo que usa `framework.config.yaml`.

Se usa cuando PyYAML no está instalado: el hook de un repo consumidor tiene
que correr sin instalar nada. Cubre mapas anidados por indentación, listas
(en bloque e inline), escalares y comentarios; **falla fuerte** ante cualquier
otra construcción (tabs, anclas, escalares multilínea). Un parse silencioso y
equivocado del contrato del repo es peor que un error claro.
"""
from __future__ import annotations

import re

from .errors import fail

INLINE_LIST_RE = re.compile(r"^\[(.*)\]$")
UNSUPPORTED = ("|", ">", "&", "*", "!", "%", "?")


def load(text: str, source: str = "config") -> dict:
    lines = significant_lines(text, source)
    if not lines:
        return {}
    value, index = parse_block(lines, 0, lines[0][0], source)
    if index != len(lines):
        fail(f"{source}:{lines[index][2]}: indentación inesperada")
    return value


def significant_lines(text: str, source: str) -> list[tuple[int, str, int]]:
    """(indent, contenido sin comentario, número de línea) — sin blancos."""
    out = []
    for number, raw in enumerate(text.splitlines(), start=1):
        if "\t" in raw[: len(raw) - len(raw.lstrip())]:
            fail(f"{source}:{number}: indentación con tab — usá espacios")
        content = strip_comment(raw).rstrip()
        if not content.strip():
            continue
        out.append((len(content) - len(content.lstrip()), content.strip(), number))
    return out


def strip_comment(line: str) -> str:
    quote = None
    for index, char in enumerate(line):
        if quote:
            if char == quote:
                quote = None
        elif char in "\"'":
            quote = char
        elif char == "#" and (index == 0 or line[index - 1] in " \t"):
            return line[:index]
    return line


def parse_block(lines, index: int, indent: int, source: str):
    if lines[index][1].startswith("- "):
        return parse_list(lines, index, indent, source)
    return parse_map(lines, index, indent, source)


def parse_map(lines, index: int, indent: int, source: str):
    result: dict = {}
    while index < len(lines):
        line_indent, content, number = lines[index]
        if line_indent < indent:
            break
        if line_indent > indent:
            fail(f"{source}:{number}: indentación inesperada")
        key, separator, raw = content.partition(":")
        if not separator:
            fail(f"{source}:{number}: se esperaba `clave: valor` — «{content}»")
        key, raw = key.strip(), raw.strip()
        if raw:
            result[key] = scalar(raw, source, number)
            index += 1
            continue
        index += 1
        if index < len(lines) and lines[index][0] > indent:
            result[key], index = parse_block(lines, index, lines[index][0], source)
        elif index < len(lines) and lines[index][1].startswith("- ") and lines[index][0] == indent:
            result[key], index = parse_list(lines, index, indent, source)
        else:
            result[key] = None
    return result, index


def parse_list(lines, index: int, indent: int, source: str):
    result: list = []
    while index < len(lines):
        line_indent, content, number = lines[index]
        if line_indent < indent or not content.startswith("- "):
            break
        if line_indent > indent:
            fail(f"{source}:{number}: indentación inesperada en lista")
        item = content[2:].strip()
        if ":" in item and not INLINE_LIST_RE.match(item):
            # `- clave: valor` — mapa dentro de lista: su indentación efectiva
            # es la del guion más los dos caracteres del marcador.
            inner_indent = line_indent + 2
            rewritten = [(inner_indent, item, number)]
            index += 1
            while index < len(lines) and lines[index][0] >= inner_indent:
                rewritten.append(lines[index])
                index += 1
            entry, consumed = parse_map(rewritten, 0, inner_indent, source)
            if consumed != len(rewritten):
                fail(f"{source}:{number}: no puedo parsear el ítem de lista")
            result.append(entry)
            continue
        result.append(scalar(item, source, number))
        index += 1
    return result, index


def scalar(raw: str, source: str, number: int):
    if raw[:1] in UNSUPPORTED:
        fail(f"{source}:{number}: construcción YAML no soportada por el lector mínimo "
             f"(«{raw[:1]}») — instalá PyYAML o simplificá el valor")
    inline = INLINE_LIST_RE.match(raw)
    if inline:
        inner = inline.group(1).strip()
        return [scalar(part.strip(), source, number) for part in inner.split(",") if part.strip()]
    if len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in "\"'":
        return raw[1:-1]
    if raw in ("null", "~"):
        return None
    if raw in ("true", "True", "yes"):
        return True
    if raw in ("false", "False", "no"):
        return False
    if re.fullmatch(r"-?\d+", raw):
        return int(raw)
    if re.fullmatch(r"-?\d+\.\d+", raw):
        return float(raw)
    return raw
