"""Salida de error uniforme para todo script del kit.

Un solo lugar decide cómo se ve un fallo: `ERROR: …` a stderr y exit 1.
Los scripts nunca `print` un error a mano.
"""
from __future__ import annotations

import sys


def fail(msg: str) -> None:
    """Aborta con mensaje a stderr. Jamás vuelve."""
    print(f"ERROR: {msg}", file=sys.stderr)
    raise SystemExit(1)
