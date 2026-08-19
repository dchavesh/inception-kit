"""Vocabulario de madurez y volatilidad que parsean los scripts.

**v0.1 — ESPAÑOL, a propósito.** El enum inglés
(`established / supported / plausible / speculative` ·
`high / medium / low`) está RATIFICADO (2026-08-18) pero entra **junto con la
spec v0.3**: parsers, plantillas y corpus migran a la vez, jamás a medias
(plan de mejoras §Fase 2.1). Cambiar esta lista suelta parte el corpus:
la migración la ejecuta `/migrate` con el bump de spec, no una edición aquí.

Por eso el enum vive en el kit y NO en `framework.config.yaml`: no es una
decisión por proyecto, es el contrato de la spec — un contrato, un lugar.
"""
from __future__ import annotations

import re

MATURITY_WORDS = ("establecido", "respaldado", "plausible", "especulativo")
VOLATILITY_WORDS = ("alta", "media", "baja")

#: Madurez que, por definición, puede ir sin fuente (spec §1.4).
SPECULATIVE = "especulativo"

MATURITY_RE = re.compile(rf"\b(?:{'|'.join(MATURITY_WORDS)})\b")
VOLATILITY_RE = re.compile(rf"\b({'|'.join(VOLATILITY_WORDS)})\b")

#: Anotación `(madurez · volatilidad · fecha)` de un hallazgo o afirmación.
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
