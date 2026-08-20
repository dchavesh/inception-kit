"""Mecánica común de los pases que ESCRIBEN: git, `--apply` y rastro.

Los flujos que tocan el repo —migración y normalización— comparten la misma
disciplina y por eso comparten esta casa (principio de diseño #4):

  · **nada se escribe sin `--apply`**, y el `--apply` se pide después de mostrar
    el inventario o el diff (spec §9.1: el opt-in es del humano);
  · **un pase no arrastra trabajo ajeno**: el índice tiene que estar limpio,
    porque el pase commitea su propio rastro;
  · **todo pase deja su entrada en el registry de migraciones** (§9.2), con lo
    que quedó fuera de alcance y por qué.
"""
from __future__ import annotations

import hashlib
import subprocess
from pathlib import Path

from . import registrystore as store
from .dates import today
from .errors import fail

CHUNK = 1 << 20


class Git:
    """git acotado a un repo, que falla fuerte y sin adivinar."""

    def __init__(self, root: Path):
        self.root = root

    def __call__(self, *args: str, check: bool = True) -> subprocess.CompletedProcess:
        result = subprocess.run(["git", "-C", str(self.root), *args],
                                capture_output=True, text=True)
        if check and result.returncode != 0:
            fail(f"git {' '.join(args[:2])}…: "
                 f"{result.stderr.strip() or result.stdout.strip()}")
        return result

    def require_clean_index(self) -> None:
        if self("diff", "--cached", "--name-only").stdout.strip():
            fail("hay cambios ya staged — un pase escribe su propio rastro y no "
                 "arrastra trabajo ajeno. Commiteá o reseteá primero.")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(CHUNK), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_flags(argv: list[str], known: dict, usage: str,
                switches: tuple = ("--apply",)) -> tuple[list[str], dict]:
    """`--flag VALOR` y switches booleanos; lo demás, posicional."""
    values, positional, index = dict(known), [], 0
    while index < len(argv):
        arg = argv[index]
        if arg in switches:
            values[arg] = True
        elif arg in values:
            if index + 1 >= len(argv):
                fail(f"{arg} requiere valor\n{usage}")
            values[arg] = argv[index + 1]
            index += 1
        elif arg.startswith("--"):
            fail(f"flag desconocida: {arg}\n{usage}")
        else:
            positional.append(arg)
        index += 1
    return positional, values


def record_pass(config, writer: str, name: str, summary: str, changes: list,
                verification: str, out_of_scope: str, to_version: str) -> None:
    """El rastro obligatorio de §9.2, mitad registry."""
    store.append(config, "migrations", [{
        "date": today(), "pass": name,
        "from_version": config.kit_version, "to_version": to_version,
        "summary": summary, "changes": list(changes),
        "verification": verification, "out_of_scope": out_of_scope,
    }], writer)


def commit(git: Git, paths: list, subject: str) -> None:
    git("add", "--", *paths)
    if not git("diff", "--cached", "--name-only").stdout.strip():
        print("nada que commitear.")
        return
    git("commit", "-m", subject)
    print(f"commit: {subject}")
