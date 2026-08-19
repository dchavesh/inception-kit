"""Contrato del `01-report` — las 7 secciones y sus tablas.

Vive en el kit (no en `framework.config.yaml`) porque no es una decisión por
proyecto: es la plantilla de la spec. La misma definición la consumen
`validate-report`, `extract-registry`, `claim-audit-sample` y la plantilla que
la skill `/launch` manda a la sesión — un contrato, un lugar, varios lectores.

Si esto cambia, cambia la spec: el enum de madurez/volatilidad que aparece en
las columnas migra al inglés JUNTO con la spec v0.3 (ver `vocab`).
"""
from __future__ import annotations

#: `## N. …` → palabra que el encabezado debe mencionar.
SECTION_KEYWORDS = {
    1: "Resumen",
    2: "Hallazgos",
    3: "Fuentes",
    4: "Contradicciones",
    5: "Implicaciones",
    6: "Huecos",
    7: "Tabla",
}

CLAIMS_SECTION = 2
SOURCES_SECTION = 3
REQUIREMENTS_SECTION = 7

REQ_COLUMNS = ("ID", "Requirement", "Why", "Evidence & maturity",
               "Core or Playbook", "Area")
SOURCE_COLUMNS = ("ID", "Título", "Autor/Org", "Fecha", "Tipo", "Calidad", "Volatilidad")

#: Rúbrica de calidad de fuente (Bloque Común).
QUALITY_GRADES = "ABCD"

#: Columnas que `extract-registry` agrega a la RTM sobre las del report.
#: En inglés, como las seis del report (principio #6): los nombres de campo del
#: contrato son inglés; la prosa del corpus sigue siendo español.
REGISTRY_EXTRA_COLUMNS = ("Status", "Invalidation")
