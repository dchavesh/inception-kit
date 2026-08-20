"""Inventario documental de un repo existente — el insumo de `/normalize`.

Lee estado, jamás ideología: estructura, tamaños, duplicados, huérfanos y
familias de versiones. Nada de lo que hay acá decide: **describe**, y el flujo
lo pone frente al humano, que es quien adjudica (spec §0 — autoridad en los
gates humanos).

Alcance: los documentos markdown **trackeados** que viven FUERA de las casas
del framework. Las casas ya están normadas —§5 cierra las carpetas de unidad,
§12 G6 el registry, §2.2 el bronze— y `doctor` las verifica; lo que `/normalize`
inventaría es justamente lo que todavía no tiene casa.
"""
from __future__ import annotations

import os
import re
import subprocess
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path

from . import records
from .config import Config

#: Un monolito append-heavy es grande **y** muy tocado: el log gigante donde lo
#: corregido sigue presente por volumen (eco por frecuencia en su forma pura).
#: Grande-pero-quieto es un documento largo; chico-pero-muy-tocado es un
#: evergreen sano. Solo la conjunción describe la enfermedad.
MONOLITH_BYTES = 60_000
MONOLITH_COMMITS = 30

#: Sufijos de versión artesanal en el nombre del archivo. No son la supersesión
#: del framework (`.vN` + fila en el registry): son su síntoma.
VERSION_SUFFIX_RE = re.compile(
    r"[-.]?(v\d+([-.]\d+)*|final|borrador|draft|old|new|copia|copy|bak)$", re.I)

#: Salida de build trackeada: no es documentación y no la normaliza este flujo.
BUILD_OUTPUT_NAMES = ("coverage.xml", ".coverage", "coverage.json")
BUILD_OUTPUT_SUFFIXES = (".pyc", ".log", ".tmp")

LINK_RE = re.compile(r"\]\(([^)\s#]+)")


@dataclass(frozen=True)
class Document:
    path: Path
    relative: str
    size: int
    commits: int


def git_lines(root: Path, *args: str) -> list[str]:
    result = subprocess.run(["git", "-C", str(root), *args],
                            capture_output=True, text=True)
    if result.returncode != 0:
        return []
    return [line for line in result.stdout.splitlines() if line.strip()]


def tracked(root: Path) -> list[str]:
    return git_lines(root, "ls-files")


def commit_counts(root: Path) -> Counter:
    """Cuántos commits tocó cada ruta, en UNA sola pasada de git."""
    return Counter(git_lines(root, "log", "--pretty=format:", "--name-only"))


def framework_houses(config: Config) -> tuple:
    """Prefijos de ruta que este inventario NO revisa: ya tienen norma y guarda."""
    paths = config.data["paths"]
    houses = [paths[name] for name in
              ("investigations", "registry", "evidence", "hard_docs")]
    houses.extend([".inception-kit", ".claude", ".github", ".gitlab"])
    return tuple(f"{house.rstrip('/')}/" for house in houses)


def is_subject(relative: str, houses: tuple, covered: set, patterns: tuple) -> bool:
    """Un documento es sujeto de clasificación si nadie lo clasificó ya.

    Quedan fuera las casas del framework, lo que el roster §4.5 explica y **todo
    lo que ya es record** — incluido el legado congelado en su lugar por
    `normalize freeze`: su clase la fija la guarda, no el juicio de este flujo.
    """
    return (relative.endswith(".md") and not relative.startswith(houses)
            and relative not in covered
            and not records.is_record(relative, patterns))


def documents(config: Config, covered: set | None = None) -> list[Document]:
    """Los documentos que el flujo tiene que clasificar, de mayor a menor peso."""
    houses = framework_houses(config)
    patterns = records.patterns(config)
    counts = commit_counts(config.root)
    found = []
    for relative in tracked(config.root):
        if not is_subject(relative, houses, covered or set(), patterns):
            continue
        path = config.root / relative
        if not path.is_file():
            continue
        found.append(Document(path=path, relative=relative,
                              size=path.stat().st_size,
                              commits=counts.get(relative, 0)))
    return sorted(found, key=lambda doc: (-doc.size, doc.relative))


def monoliths(docs: list) -> list:
    """Grandes y append-heavy: el caso del log de decisiones que nadie puede no leer."""
    return [doc for doc in docs
            if doc.size >= MONOLITH_BYTES and doc.commits >= MONOLITH_COMMITS]


def duplicate_basenames(docs: list) -> dict:
    """Mismo nombre en carpetas distintas — el síntoma de «épocas como carpetas»."""
    groups = defaultdict(list)
    for doc in docs:
        groups[doc.path.name].append(doc.relative)
    return {name: sorted(paths) for name, paths in sorted(groups.items())
            if len(paths) > 1}


def version_stem(name: str) -> str:
    stem = Path(name).stem
    previous = None
    while previous != stem:
        previous = stem
        stem = VERSION_SUFFIX_RE.sub("", stem)
    return stem


def version_families(docs: list) -> dict:
    """Pares `x` / `x-v2` conviviendo: supersesión a medias, sin vigente declarado."""
    groups = defaultdict(list)
    for doc in docs:
        groups[(str(doc.path.parent), version_stem(doc.path.name))].append(doc.relative)
    return {stem: sorted(paths) for (_, stem), paths in sorted(groups.items())
            if len(paths) > 1}


def link_targets(config: Config) -> set:
    """Toda ruta a la que apunta algún markdown trackeado del repo.

    *Alcanzable* incluye findings y registry: un documento citado desde la
    memoria del programa no es huérfano aunque nadie más lo enlace.
    """
    targets: set = set()
    for relative in tracked(config.root):
        if not relative.endswith(".md"):
            continue
        path = config.root / relative
        if not path.is_file():
            continue
        base = str(Path(relative).parent)
        for link in LINK_RE.findall(path.read_text(encoding="utf-8", errors="replace")):
            if "://" in link:
                continue
            # `../` se resuelve acá: sin normalizar, `docs/a/../c.md` no calzaría
            # nunca contra `docs/c.md` y el documento parecería huérfano.
            candidate = link.lstrip("/") if link.startswith("/") else os.path.join(base, link)
            targets.add(os.path.normpath(candidate))
    return targets


def orphans(config: Config, docs: list) -> list:
    """Documentos que nadie enlaza — ni siquiera desde findings o registry."""
    targets = link_targets(config)
    return [doc for doc in docs if doc.relative not in targets]


def hygiene(config: Config) -> list[str]:
    """Higiene operativa: se flagea y queda FUERA del alcance documental."""
    notes: list[str] = []
    outputs = [relative for relative in tracked(config.root)
               if Path(relative).name in BUILD_OUTPUT_NAMES
               or Path(relative).suffix in BUILD_OUTPUT_SUFFIXES]
    if outputs:
        notes.append(f"{len(outputs)} archivo(s) de salida de build trackeados "
                     f"({', '.join(outputs[:5])}{'…' if len(outputs) > 5 else ''}) — "
                     "no son documentación: salen por `.gitignore`, no por este flujo")
    worktrees = [line for line in git_lines(config.root, "worktree", "list")]
    if len(worktrees) > 1:
        notes.append(f"{len(worktrees)} worktrees activos — higiene operativa local, "
                     "fuera del alcance documental de la normalización")
    branches = git_lines(config.root, "branch", "--format=%(refname:short)")
    if len(branches) > 10:
        notes.append(f"{len(branches)} ramas locales — ídem: se nombra, no se toca")
    return notes
