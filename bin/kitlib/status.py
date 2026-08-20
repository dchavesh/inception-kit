"""Tablero derivado del estado de las unidades — el noveno registry (spec §12 G6).

Vista derivada: se regenera, jamás se edita a mano. Vive acá — y no dentro de
`derive-status` — porque `doctor` y el índice la recomputan sin escribir nada:
un contrato, un lugar, varios lectores.

Las **columnas van en inglés** (§1.8: columnas de tabla, siempre); la **prosa**
de las celdas y del encabezado, en el idioma que declare `language`.
"""
from __future__ import annotations

from .config import Config
from .dates import today
from .ids import is_ready, load_units
from .phrases import has_table, phrase, stamp

COLUMNS = ("Unit", "Status", "Needs", "Ready", "Note")


def board_rows(config: Config) -> tuple:
    """(filas, lanzables ahora, ready tras freeze) — el cálculo, sin markdown."""
    units = load_units(config)
    language = config.language
    rows, ready_now, ready_after_freeze = [], [], []
    for unit in units.values():
        ready = is_ready(unit, units)
        needs = ", ".join(unit.needs) if unit.needs else "—"
        if unit.status == "done":
            ready_cell, note = "—", phrase(language, "board-closed")
        elif ready and unit.status == "frozen":
            ready_cell, note = "sí", phrase(language, "board-launchable")
            ready_now.append(unit.id)
        elif ready:
            ready_cell, note = "sí", phrase(language, "board-needs-freeze")
            ready_after_freeze.append(unit.id)
        else:
            pending = [need for need in unit.needs
                       if units.get(need) is None or units[need].status != "done"]
            ready_cell = "no"
            note = phrase(language, "board-waiting", units=", ".join(pending))
        rows.append((unit.id, unit.status, needs, ready_cell, note))
    return rows, ready_now, ready_after_freeze


def build_board(config: Config) -> str:
    language = config.language
    rows, ready_now, ready_after_freeze = board_rows(config)
    lines = [f"# {phrase(language, 'board-title')}", ""]
    if not has_table(language):
        lines += ["> " + phrase(language, "language-fallback", language=language,
                                fallback="en"), ""]
    lines += [
        stamp(language, "derive-status", today(), phrase(language, "board-source")),
        "",
        "| " + " | ".join(COLUMNS) + " |",
        "|" + "|".join("---" for _ in COLUMNS) + "|",
    ]
    lines.extend("| " + " | ".join(row) + " |" for row in rows)

    lines.append("")
    if ready_now:
        lines.append(f"{phrase(language, 'board-launchable-now')} {', '.join(ready_now)}")
    if ready_after_freeze:
        lines.append(f"{phrase(language, 'board-ready-after-freeze')} "
                     f"{', '.join(ready_after_freeze)}")
    if not ready_now and not ready_after_freeze:
        lines.append(phrase(language, "board-nothing-ready"))
    lines.append("")
    return "\n".join(lines)
