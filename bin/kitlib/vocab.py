"""Vocabulario de la spec que parsean los scripts: madurez, volatilidad y clases de fuente.

**v0.2 — INGLÉS.** El enum quedó ratificado el 2026-08-18 y entra en vigor con
la spec v0.3 (`status: ratified`, 2026-08-19) y este kit 0.2.0, que lo migra en
un solo bump y de forma indivisible (spec §1.6, §9.4): parsers, plantillas,
claves de `horizons` y corpus nuevo, juntos — jamás a medias.

El corpus histórico NO se reescribe: se lee con el glosario de spec §13.2 y se
migra, si se migra, por las reglas de §9 (`/migrate`, Fase 3.5). Por eso los
parsers hablan SOLO el enum vigente: leer dialecto viejo acá sería lavar la
diferencia que el glosario existe para conservar.

El enum vive en el kit y NO en `framework.config.yaml`: no es una decisión por
proyecto, es contrato de la spec — un contrato, un lugar (spec §1.6).
"""
from __future__ import annotations

import re

MATURITY_WORDS = ("established", "supported", "plausible", "speculative")
VOLATILITY_WORDS = ("high", "medium", "low")

#: Madurez que, por definición, puede ir sin fuente (spec §1.6).
SPECULATIVE = "speculative"

#: Las seis clases de fuente de evidencia (spec §2.1). Set cerrado de la spec.
#: `hard-doc` tiene casa especial (`paths.hard_docs`) y jamás se borra (§2.3).
SOURCE_CLASSES = ("research-run", "field-interview", "form-batch",
                  "document-drop", "media", "hard-doc")
HARD_DOC_CLASS = "hard-doc"
RESEARCH_RUN_CLASS = "research-run"

#: Clases con casa en `<research>/evidence/<class>/` cuando no pertenecen a una
#: unidad (spec §2.6). `evidence/misc/` y equivalentes están prohibidos.
EVIDENCE_CLASSES = tuple(c for c in SOURCE_CLASSES if c != HARD_DOC_CLASS)

#: Glosario de lectura del dialecto español de volatilidad (spec §13.2). Se usa
#: SOLO para migrar las claves de `horizons` de una config 0.1.x — que es
#: evergreen, y por eso se actualiza in-place (§9.1). Jamás para parsear corpus.
HISTORICAL_VOLATILITY = {"alta": "high", "media": "medium", "baja": "low"}

#: Ídem para madurez, y **solo para diagnosticar**: cuando un record trae el
#: dialecto viejo, el chequeo de integridad lo nombra en vez de decir «no
#: parseable». Reconocerlo no es aceptarlo: el record sigue sin validar, y su
#: migración es supersesión mecánica con opt-in humano (`/migrate`, §9.1).
HISTORICAL_MATURITY = {"establecido": "established", "respaldado": "supported",
                       "plausible": "plausible", "especulativo": "speculative"}
HISTORICAL_RE = re.compile(
    r"\b(" + "|".join([*HISTORICAL_MATURITY, *HISTORICAL_VOLATILITY]) + r")\b"
)


def historical_dialect(text: str) -> set[str]:
    """Términos del vocabulario histórico presentes en el texto (spec §13.2)."""
    found = set(HISTORICAL_RE.findall(text.lower()))
    return found - set(MATURITY_WORDS)  # `plausible` es idéntico en ambos

MATURITY_RE = re.compile(rf"\b(?:{'|'.join(MATURITY_WORDS)})\b")
VOLATILITY_RE = re.compile(rf"\b({'|'.join(VOLATILITY_WORDS)})\b")

#: Anotación `(maturity · volatility · fecha)` de un hallazgo o afirmación.
ANNOTATION_RE = re.compile(
    rf"\(([^()]*\b(?:{'|'.join(MATURITY_WORDS)})\b[^()]*)\)"
)

#: Etiqueta de corrida canónica (`run-01`…). "C1/C2" es vocabulario histórico.
RUN_LABEL_RE = re.compile(r"\brun-\d{2,}\b")


def has_maturity(text: str) -> bool:
    return bool(MATURITY_RE.search(text.lower()))


def has_volatility(text: str) -> bool:
    return bool(VOLATILITY_RE.search(text.lower()))


def mentioned_volatilities(text: str) -> set[str]:
    return set(VOLATILITY_RE.findall(text.lower()))


def canonical_volatility(word: str) -> str:
    """Clave de volatilidad vigente; traduce el dialecto histórico (§13.2)."""
    return HISTORICAL_VOLATILITY.get(str(word).strip().lower(), str(word).strip())
