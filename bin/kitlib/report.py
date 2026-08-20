"""Contrato del `01-report` — las 7 secciones y sus tablas.

Vive en el kit (no en `framework.config.yaml`) porque no es una decisión por
proyecto: es la plantilla de la spec. La misma definición la consumen
`validate-report`, `extract-registry`, `claim-audit-sample` y la plantilla que
la skill `/launch` manda a la sesión — un contrato, un lugar, varios lectores.

**Los nombres de sección y de columna van en inglés, siempre** (spec §0.1 #6,
§1.1, §1.8): son nombres de concepto del framework y anclas deterministas del
validador, no prosa. Lo que la sesión escribe DEBAJO de cada encabezado es
prosa, y se redacta en el idioma que declare `language` (§1.8).
"""
from __future__ import annotations

#: `## N. …` → palabra que el encabezado debe mencionar.
SECTION_KEYWORDS = {
    1: "Summary",
    2: "Findings",
    3: "Sources",
    4: "Contradictions",
    5: "Implications",
    6: "Gaps",
    7: "Requirements",
}

CLAIMS_SECTION = 2
SOURCES_SECTION = 3
REQUIREMENTS_SECTION = 7

REQ_COLUMNS = ("ID", "Requirement", "Why", "Evidence & maturity",
               "Core or Playbook", "Area")
SOURCE_COLUMNS = ("ID", "Title", "Author/Org", "Date", "Type", "Quality", "Volatility")

#: Rúbrica de calidad de fuente (spec §2.5), columna `Quality`.
QUALITY_GRADES = "ABCD"

#: Columnas que `extract-registry` agrega a la RTM sobre las del report.
REGISTRY_EXTRA_COLUMNS = ("Status", "Invalidation")
