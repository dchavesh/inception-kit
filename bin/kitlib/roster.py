"""El roster de archivos repo-level (spec §4.5) y la prueba del puntero delgado.

**Por qué acá y no en `doctor`.** El chequeo de integridad censa solo el
registry por adjudicación explícita del gate (2026-08-19): censar la raíz lo
obligaría a asumir filas que la tabla §4.5 no declara, y `doctor` corre en cada
push — no puede fallar sobre algo que necesita juicio. El enforcement del roster
vive acá y lo consume `/normalize`, que **propone y pide gate humano**.

Dos cosas verifica esta casa, las dos de §4.5:

  · **taxonomía cerrada** — la tabla es el set completo; un archivo repo-level
    que no esté en ella no es «una excepción», es una violación. Desde la spec
    v0.4 la tabla declara también el **documento de plan** (Δ18) y los archivos
    que **exige el ecosistema** (Δ17): están en el roster, no fuera de él;
  · **la prueba del puntero delgado** — «si se borra un archivo de entrada, no
    se pierde ninguna regla, solo el atajo para encontrarla». Un archivo de
    entrada que repite una regla, aunque sea «resumida», está albergando
    conocimiento de otra casa.

El segundo chequeo se hace **midiendo, no juzgando**: una línea del archivo de
entrada que aparece casi igual en la constitution, en la config o en otro
documento repo-level es una **segunda casa** — y un resumen es una copia que
deriva en silencio (principio de diseño #4).
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from .config import CONFIG_NAME, Config
from .md import parse_frontmatter

#: Los archivos de entrada de §4.5: punteros delgados o vistas generadas.
ENTRY_FILES = ("README.md", "CLAUDE.md", "INDEX.md")

#: Fila del roster para cada archivo de raíz que la tabla §4.5 declara.
ROOT_ROSTER = {
    "README.md": "qué es este repo y dónde está cada cosa — evergreen, puntero delgado",
    "CLAUDE.md": "cómo se opera este repo — evergreen, puntero delgado",
    "INDEX.md": "índice puerta-de-entrada — vista derivada generada (`derive-index`)",
    CONFIG_NAME: "el contrato del repo con el kit y su ancla — evergreen con bloque ratificado",
}

#: Los archivos que **exige el ecosistema** y no el framework (§4.5, spec v0.4
#: Δ17). Ocupan fila: existen legítimamente y están **fuera del KB**.
#:
#: La fila la define un **criterio** —exigido por el mundo donde el repo vive,
#: sin regla del framework adentro—, y su lista es *ilustrativa, no exhaustiva*.
#: Por eso el censo reconoce los nombres de la convención y nada más: una
#: convención nueva (`SECURITY.md`, `CODEOWNERS`…) sale como fuera del roster y
#: la adjudica el humano en el gate de `/normalize`, que es donde vive el juicio.
#: Un archivo que entra por esta puerta portando reglas del repo no es del
#: ecosistema: es una segunda casa con disfraz, y eso también lo juzga el humano.
ECOSYSTEM_STEMS = ("LICENSE", "LICENCE", "COPYING", "NOTICE")
ECOSYSTEM_NAMES = ("CITATION.cff",)
ECOSYSTEM_DETAIL = (
    "archivo que **exige el ecosistema**, no el framework (§4.5): términos de "
    "uso, atribución o forma de citar. Evergreen **fuera del KB** — no es record, "
    "no se cita como evidencia y el ciclo de borrado no lo alcanza. Su dueño está "
    "afuera; si portara reglas del repo no entraría por esta puerta")

#: Fila del documento de plan (§4.5, spec v0.4 Δ18). Lo identifica el `plan:` de
#: un protocol, no su nombre ni su carpeta: por eso la misma fila sirve en la
#: raíz y en `<research>/`.
PLAN_DETAIL = (
    "documento de plan (§4.5, apuntado por el `plan:` de un protocol, §12 G1) — "
    "**record**: mapa + briefing + una sección por unidad. Fechado y no editable; "
    "comisionar de nuevo es un plan nuevo que supersede, jamás una edición")

#: Maquinaria versionada por el kit o por el harness: §4.5 la deja fuera de la
#: taxonomía a propósito («no aloja reglas, se reemplaza en cada bump»).
TOOLING_NAMES = (".gitignore", ".gitattributes", ".gitmodules", ".editorconfig",
                 ".pre-commit-config.yaml")

#: Un puntero delgado que pasa de acá dejó de ser un atajo. No es un veredicto:
#: es el umbral a partir del cual el flujo lo pone frente al humano.
THIN_POINTER_MAX_LINES = 120

#: Una línea corta ("## Instalación") coincide entre documentos sin ser una
#: regla duplicada. Solo las líneas con cuerpo cuentan como segunda casa.
DUPLICATED_MIN_CHARS = 40

ROSTER, TOOLING, OFF_ROSTER = "roster", "tooling", "off-roster"

DECORATION_RE = re.compile(r"^[\s>*\-+#|]+|[\s|]+$")
WHITESPACE_RE = re.compile(r"\s+")
EMPHASIS_RE = re.compile(r"[*`_]")


@dataclass(frozen=True)
class Finding:
    """Un archivo repo-level y su veredicto contra la tabla §4.5."""
    path: str
    verdict: str
    detail: str


def plan_documents(config: Config) -> set[Path]:
    """Los documentos de plan, resueltos por el campo `plan:` de los protocols.

    §12 G1 hace del `plan:` un contrato: el briefing vive en la Parte II del
    documento que apunta. Ese puntero es también la forma **determinista** de
    saber qué archivo de `<research>/` es un plan — sin adivinar por nombre.

    La tabla §4.5 le declara fila desde la spec v0.4 (Δ18): son **roster**, con
    clase record. Un plan no apuntado por ningún `plan:` no es un plan: es un
    documento suelto, y el censo lo trata como tal.
    """
    documents: set[Path] = set()
    if not config.investigations.is_dir():
        return documents
    for protocol in config.investigations.glob("*/00-protocol.md"):
        meta, _ = parse_frontmatter(protocol.read_text(encoding="utf-8"))
        pointer = str(meta.get("plan") or "").strip()
        if pointer and pointer not in ("null", "~"):
            documents.add((config.root / pointer).resolve())
    return documents


def declared_directories(config: Config) -> set[Path]:
    """Las casas que declara `paths` — §5 las cierra, esta casa no las revisa."""
    return {config.path(name).resolve()
            for name in config.data["paths"] if name != "constitution"}


def census(config: Config) -> list[Finding]:
    """Censo de la raíz y de `<research>/` contra la tabla §4.5."""
    findings: list[Finding] = []
    plans = plan_documents(config)
    declared = declared_directories(config)

    for entry in sorted(config.root.iterdir(), key=lambda path: path.name):
        if entry.name.startswith(".") or entry.name in TOOLING_NAMES:
            continue
        if entry.is_dir():
            continue
        findings.append(root_finding(config, entry, plans))

    research = config.research
    if research.is_dir():
        for entry in sorted(research.iterdir(), key=lambda path: path.name):
            if entry.is_dir() or entry.name.startswith("."):
                continue
            if entry.resolve() in declared or entry.resolve() == config.constitution.resolve():
                continue
            findings.append(research_finding(config, entry, plans))
    return findings


def is_ecosystem(name: str) -> bool:
    """¿Es uno de los archivos que exige el ecosistema (§4.5)?

    Reconoce la convención por su nombre, con o sin extensión (`LICENSE`,
    `LICENSE.md`, `LICENSE.txt`). El criterio de la fila es más ancho que esta
    lista a propósito: lo que no reconoce, lo adjudica el humano en el gate.
    """
    if name in ECOSYSTEM_NAMES:
        return True
    stem, _, extension = name.partition(".")
    return stem in ECOSYSTEM_STEMS and extension in ("", "md", "txt")


def root_finding(config: Config, entry: Path, plans: set[Path]) -> Finding:
    relative = config.relative(entry)
    if entry.name in ROOT_ROSTER:
        return Finding(relative, ROSTER, ROOT_ROSTER[entry.name])
    if is_ecosystem(entry.name):
        return Finding(relative, ROSTER, ECOSYSTEM_DETAIL)
    if entry.name == "SPEC.md":
        return Finding(relative, OFF_ROSTER,
                       "la spec **vive en el kit y en ningún repo consumidor** "
                       "(§4.5): una copia acá es una segunda casa de la norma que "
                       "deriva al primer bump. Un repo la referencia por el "
                       "`kit_version` que declara su config")
    if entry.name == "AGENTS.md":
        return Finding(relative, OFF_ROSTER,
                       "`AGENTS.md` no es parte del framework (§4.5): ninguna fila "
                       "lo declara y ninguna regla vive ahí. Si un harness externo "
                       "lo exige, se **genera** desde la misma fuente que "
                       "`CLAUDE.md` — jamás se redacta aparte")
    if entry.resolve() in plans:
        return Finding(relative, ROSTER, PLAN_DETAIL)
    return Finding(relative, OFF_ROSTER,
                   "archivo repo-level fuera de la tabla §4.5 — la taxonomía es "
                   "**cerrada**: o se mueve a la casa que le corresponde, o entra "
                   "por enmienda de la spec con su fila declarada")


def research_finding(config: Config, entry: Path, plans: set[Path]) -> Finding:
    relative = config.relative(entry)
    if entry.resolve() in plans:
        return Finding(relative, ROSTER, PLAN_DETAIL)
    return Finding(relative, OFF_ROSTER,
                   f"documento suelto en `{config.relative(config.research)}/` sin "
                   "fila en §4.5 — clasificarlo (record · evergreen · efímero · "
                   "hard-doc) y darle su casa, o no existe como archivo")


def covered(config: Config, findings: list) -> set:
    """Rutas que el roster ya explica: no son sujeto de clasificación ni huérfanas.

    Son las filas de §4.5 que este repo tiene —incluidos los documentos de plan
    y los archivos del ecosistema— más la constitution, que §4.5 declara por su
    casa y por eso el censo no la recorre.
    """
    paths = {item.path for item in findings if item.verdict != OFF_ROSTER}
    if config.constitution.is_file():
        paths.add(config.relative(config.constitution))
    return paths


def normalized(line: str) -> str:
    """Una línea, sin decoración markdown, comparable entre documentos."""
    text = EMPHASIS_RE.sub("", DECORATION_RE.sub("", line))
    return WHITESPACE_RE.sub(" ", text).strip().lower()


def content_lines(text: str) -> dict:
    """normalizado → original, solo las líneas con cuerpo suficiente."""
    out = {}
    for line in text.splitlines():
        key = normalized(line)
        if len(key) >= DUPLICATED_MIN_CHARS and " " in key:
            out.setdefault(key, line.strip())
    return out


def houses(config: Config) -> dict:
    """Dónde viven las reglas que un archivo de entrada solo debería apuntar."""
    candidates = {config.constitution: config.relative(config.constitution),
                  config.root / CONFIG_NAME: CONFIG_NAME}
    return {label: path.read_text(encoding="utf-8")
            for path, label in candidates.items() if path.is_file()}


def entry_texts(config: Config) -> dict:
    """Los archivos de entrada que existen, por nombre."""
    return {name: (config.root / name).read_text(encoding="utf-8")
            for name in ENTRY_FILES if (config.root / name).is_file()}


def second_houses(name: str, text: str, others: dict) -> list[str]:
    """Líneas del archivo de entrada que también viven en otra casa."""
    own = content_lines(text)
    problems = []
    for label, other in others.items():
        for key in sorted(set(own) & set(content_lines(other))):
            problems.append(
                f"{name}: línea que también vive en `{label}` — «{own[key][:80]}» · "
                "la regla vive UNA vez y el archivo de entrada la apunta; un resumen "
                "es una copia que deriva en silencio (§4.5)")
    return problems


def thin_pointer_problems(config: Config) -> list[str]:
    """La prueba de §4.5, medida: tamaño y reglas que viven dos veces."""
    problems: list[str] = []
    entries = entry_texts(config)
    rule_houses = houses(config)

    for name, text in entries.items():
        lines = len(text.splitlines())
        if lines > THIN_POINTER_MAX_LINES:
            problems.append(
                f"{name}: {lines} líneas (umbral {THIN_POINTER_MAX_LINES}) — un "
                "archivo de entrada engordado deja de ser un atajo. Revisar qué "
                "conocimiento le pertenece a otra casa (§4.5)")
        others = {**rule_houses,
                  **{other: entries[other] for other in entries if other != name}}
        problems.extend(second_houses(name, text, others))
    return problems
