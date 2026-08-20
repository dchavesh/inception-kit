"""Backstop por rutas: qué rutas son record, pase lo que pase (spec §4.4).

El enforcement por clase (frontmatter) **se suma** a este, no lo reemplaza: la
guarda por rutas protege `raw/`, reports, findings, sources, payloads sellados,
ADRs, la casa del bronze sin unidad y la de la documentación dura **aunque un
frontmatter mienta o falte**.

Un contrato, un lugar: la lista vive acá y la leen los dos que la necesitan —
la guarda de inmutabilidad (para rechazar el commit) y el flujo de normalización
(para no proponer jamás el borrado de un record).
"""
from __future__ import annotations

import re

from .config import Config


def patterns(config: Config) -> tuple:
    """Las casas REALES donde el material aterriza (spec §2.6, §4.4).

    Con el `inbox` fuera del contrato, lo que la guarda protegía en él lo
    protege ahora en el destino. Un `inbox/` legado sigue protegido mientras
    exista, declarado en `records.extra_immutable_paths`.
    """
    investigations = re.escape(config.data["paths"]["investigations"])
    decisions = re.escape(config.data["paths"]["decisions"])
    evidence = re.escape(config.data["paths"]["evidence"])
    hard_docs = re.escape(config.data["paths"]["hard_docs"])
    found = [
        rf"^{investigations}/[^/]+/raw/",
        rf"^{investigations}/[^/]+/0[123]-(?:report|findings|sources)(?:\.v\d+)?\.md$",
        rf"^{investigations}/[^/]+/payload\.md$",
        rf"^{decisions}/adr-.+\.md$",
        rf"^{evidence}/",
        rf"^{hard_docs}/",
    ]
    found.extend(rf"^{re.escape(str(extra).rstrip('/'))}(?:/|$)"
                 for extra in config.extra_immutable_paths)
    return tuple(found)


def is_record(relative: str, record_patterns: tuple) -> bool:
    return any(re.search(pattern, relative) for pattern in record_patterns)
