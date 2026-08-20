"""Supersesión mecánica de records de lectura: el pase, y su evidencia (spec §9.1).

Un record **jamás se edita**. Lo que este módulo hace es producir la versión
`.vN` de un record de lectura reemplazando **solo etiquetas de vocabulario
histórico** por su equivalente vigente (§13.2), y dejar la prueba de que **no
cambió ningún otro byte**.

**El diff es la evidencia, y el round-trip la hace verificable.** Cada
sustitución se registra con su posición en el texto nuevo; reconstruir el
original desde el texto nuevo y ese registro tiene que devolver los bytes
originales, exactos. Si no vuelve, el pase no es mecánico y se aborta.

Dos pases, y ninguno corre solo — los dos son **opt-in del humano** con el diff
a la vista:

  · `vocab` — el enum de madurez y volatilidad, **solo dentro de una anotación**
    (los paréntesis que contienen una etiqueta de madurez). Fuera de ahí,
    `alta` o `media` son prosa, y la prosa no se toca.
  · `runs`  — las etiquetas de corrida `C1`/`CN`/`PI` → `run-NN`. `S` no entra:
    no era una corrida sino una verificación (§13.2).

Un record ya canónico no produce sustituciones, y entonces **no se supersede**:
una migración jamás genera supersesiones vacías (§9.1).
"""
from __future__ import annotations

import re

from . import vocab

PARENTHESIS_RE = re.compile(r"\(([^()]*)\)")
FRONTMATTER_RE = re.compile(r"\A---\n(.*?\n)---\n", re.S)
PASSES = ("vocab", "runs")


def token_pattern() -> re.Pattern:
    words = sorted(vocab.HISTORICAL_TOKENS, key=len, reverse=True)
    return re.compile(r"\b(" + "|".join(words) + r")\b", re.I)


TOKEN_RE = token_pattern()


def is_annotation(inner: str) -> bool:
    """¿El paréntesis es una anotación de etiquetas y no prosa entre paréntesis?

    Lo es si menciona una madurez — vigente, histórica o abreviada. `(alta
    prioridad)` no menciona ninguna y por eso queda intacto.
    """
    low = inner.lower()
    if vocab.has_maturity(low):
        return True
    return any(re.search(rf"\b{word}\b", low)
               for word in (*vocab.HISTORICAL_MATURITY, *vocab.HISTORICAL_ABBREVIATIONS))


def vocab_substitutions(text: str) -> list[tuple]:
    """(inicio, fin, viejo, nuevo) de cada etiqueta histórica dentro de anotaciones."""
    found = []
    for parenthesis in PARENTHESIS_RE.finditer(text):
        inner = parenthesis.group(1)
        if not is_annotation(inner):
            continue
        offset = parenthesis.start(1)
        for token in TOKEN_RE.finditer(inner):
            old = token.group(1)
            new = vocab.HISTORICAL_TOKENS[old.lower()]
            if new == old:
                continue  # `plausible` es idéntico en ambos enums
            found.append((offset + token.start(1), offset + token.end(1), old, new))
    return found


def run_substitutions(text: str) -> list[tuple]:
    """(inicio, fin, viejo, nuevo) de cada etiqueta de corrida histórica."""
    return [(match.start(1), match.end(1), match.group(1),
             vocab.canonical_run_label(match.group(1)))
            for match in vocab.HISTORICAL_RUN_RE.finditer(text)]


def substitutions(text: str, pass_name: str) -> list[tuple]:
    if pass_name == "vocab":
        return vocab_substitutions(text)
    if pass_name == "runs":
        return run_substitutions(text)
    raise ValueError(f"pase desconocido: {pass_name} — los pases son {list(PASSES)}")


def apply_substitutions(text: str, found: list[tuple]) -> tuple[str, list[tuple]]:
    """Devuelve (texto nuevo, registro `(offset en el nuevo, viejo, nuevo)`)."""
    parts, cursor, length, log = [], 0, 0, []
    for start, end, old, new in sorted(found):
        parts.append(text[cursor:start])
        length += start - cursor
        log.append((length, old, new))
        parts.append(new)
        length += len(new)
        cursor = end
    parts.append(text[cursor:])
    return "".join(parts), log


def round_trip(new_text: str, log: list[tuple]) -> str:
    """Reconstruye el original desde el texto nuevo y el registro de sustituciones."""
    parts, cursor = [], 0
    for offset, old, new in log:
        if new_text[offset:offset + len(new)] != new:
            raise ValueError("el registro de sustituciones no calza con el texto nuevo")
        parts.append(new_text[cursor:offset])
        parts.append(old)
        cursor = offset + len(new)
    parts.append(new_text[cursor:])
    return "".join(parts)


def verify(original: str, new_text: str, log: list[tuple]) -> bool:
    """El round-trip: si vuelve byte a byte, el diff es exactamente el declarado."""
    try:
        return round_trip(new_text, log) == original
    except ValueError:
        return False


def with_supersedes(text: str, superseded_name: str) -> str:
    """Sella `supersedes:` en el frontmatter del `.vN`. Es la única línea agregada."""
    match = FRONTMATTER_RE.match(text)
    if not match:
        return (f"---\nsupersedes: {superseded_name}\n---\n\n" + text)
    block = match.group(1)
    updated, count = re.subn(r"^supersedes:.*$", f"supersedes: {superseded_name}",
                             block, count=1, flags=re.M)
    if not count:
        updated = block.rstrip("\n") + f"\nsupersedes: {superseded_name}\n"
    return f"---\n{updated}---\n" + text[match.end():]
