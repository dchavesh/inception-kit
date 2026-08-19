"""Tablero derivado del estado de las unidades.

Vista derivada: se regenera, jamás se edita a mano. Vive acá — y no dentro de
`derive-status` — porque `doctor` la recomputa para detectar staleness sin
escribir nada: un contrato, un lugar, dos lectores.
"""
from __future__ import annotations

from .config import Config
from .dates import today
from .ids import is_ready, load_units

GENERATED_PREFIX = "*Generado"


def build_board(config: Config) -> str:
    units = load_units(config)
    lines = [
        "# STATUS — tablero derivado",
        "",
        f"{GENERATED_PREFIX} por `derive-status` el {today()}. Jamás editar a mano: "
        "regenerar. Fuente de verdad: frontmatter de cada `00-protocol.md`.*",
        "",
        "| Unidad | Status | Needs | Ready | Nota |",
        "|---|---|---|---|---|",
    ]
    ready_now, ready_after_freeze = [], []
    for unit in units.values():
        ready = is_ready(unit, units)
        needs = ", ".join(unit.needs) if unit.needs else "—"
        if unit.status == "done":
            ready_cell, note = "—", "cerrada"
        elif ready and unit.status == "frozen":
            ready_cell, note = "sí", "**lanzable** (`/launch`)"
            ready_now.append(unit.id)
        elif ready:
            ready_cell, note = "sí", "ready — falta freeze (gate humano)"
            ready_after_freeze.append(unit.id)
        else:
            pending = [need for need in unit.needs
                       if units.get(need) is None or units[need].status != "done"]
            ready_cell, note = "no", f"espera a {', '.join(pending)}"
        lines.append(f"| {unit.id} | {unit.status} | {needs} | {ready_cell} | {note} |")

    lines.append("")
    if ready_now:
        lines.append(f"**Lanzables ahora:** {', '.join(ready_now)}")
    if ready_after_freeze:
        lines.append(f"**Ready tras freeze:** {', '.join(ready_after_freeze)}")
    if not ready_now and not ready_after_freeze:
        lines.append("**Nada ready.**")
    lines.append("")
    return "\n".join(lines)


def without_timestamp(text: str) -> str:
    """El tablero menos su línea de generación — para comparar sin ruido de fecha."""
    return "\n".join(line for line in text.splitlines()
                     if not line.startswith(GENERATED_PREFIX)).strip()
