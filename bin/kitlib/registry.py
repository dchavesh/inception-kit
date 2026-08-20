"""Los nueve registries: schema, régimen y casa. Datos, no markdown.

Desde el kit 0.3.0 **el registry es un archivo de datos** y el `.md` es su
**vista generada** (spec §12 G6 norma el *régimen*, no el formato — Preguntas
al final #2). Los datos viven en `<registry>/data/<name>.jsonl`: **JSON Lines**,
un objeto por línea.

Por qué JSONL y no YAML: append-only es literalmente *agregar una línea*, así
que el régimen se verifica byte a byte con una comparación de prefijo, sin
parser y sin ambigüedad de indentación — y `json` es stdlib, con lo que la
guarda sigue corriendo con git + Python estándar (spec §4.4).

Los tres regímenes de §12 G6 se hacen cumplir **sobre los datos**:

  · **append-only** — el contenido previo no se pisa: el archivo nuevo empieza
    con el viejo, exacto. Seis registries.
  · **markable** — la fila no se borra ni cambia lo que afirmó: solo mutan los
    campos declarados en `markable`. Dos registries.
  · **derived view** — `STATUS.md` no tiene datos propios: deriva de los
    protocols y se regenera.

Un contrato, un lugar: acá se declara cada registry UNA vez — `kit-init` lo
siembra, los scripts le agregan filas y las vistas se renderizan, todo desde
esta misma definición. Los nombres de campo y de columna van en inglés
(principio #6); la prosa de la vista, en `language` (§1.8).
"""
from __future__ import annotations

from dataclasses import dataclass, field as dataclass_field

from .config import REGISTRY_FILES, Config
from .report import REGISTRY_EXTRA_COLUMNS, REQ_COLUMNS

REGIME_APPEND_ONLY = "append-only"
REGIME_MARKABLE = "markable"
REGIME_DERIVED = "derived view"

DATA_DIR = "data"
DATA_SUFFIX = ".jsonl"

#: Valores del campo `Status` de la RTM (interfaz del kit, en inglés).
STATUS_NEW = "new"
STATUS_DUPLICATE = "duplicate"
STATUS_CONTRADICTS = "contradicts"
STATUS_SUPERSEDED = "SUPERSEDED by"
STATUS_INVALIDATED = "⚠ invalidated"

#: Estado de una fila de conflicto. La spec declara la COLUMNA (§12 G6: «la fila
#: evoluciona en sus columnas de resolución y status») y no su vocabulario; el
#: kit lo fija en inglés, como todo valor de enum (principio #6). `resolution`
#: queda para la prosa de la adjudicación.
CONFLICT_OPEN = "open"
CONFLICT_RESOLVED = "resolved"
CONFLICT_STATUSES = (CONFLICT_OPEN, CONFLICT_RESOLVED)

#: Dialecto histórico de esa columna, escrito por el kit 0.1.x–0.2.x. Se lee
#: para migrar la fila (§13.2); jamás se emite.
HISTORICAL_CONFLICT_STATUS = {"abierto": CONFLICT_OPEN, "resuelto": CONFLICT_RESOLVED}

KIND_TEXT, KIND_DATE, KIND_INT, KIND_LIST = "text", "date", "int", "list"


@dataclass(frozen=True)
class Field:
    key: str
    label: str
    kind: str = KIND_TEXT
    required: bool = True
    #: Set cerrado de valores admitidos, cuando la columna es un enum del
    #: framework. Vacío = texto libre (prosa, en `language`).
    choices: tuple = dataclass_field(default_factory=tuple)


@dataclass(frozen=True)
class Registry:
    """Un registry: dónde vive, bajo qué régimen y con qué campos."""
    name: str
    regime: str
    fields: tuple
    spec: str
    key: str | None = None
    markable: tuple = dataclass_field(default_factory=tuple)

    @property
    def view_name(self) -> str:
        return REGISTRY_FILES[self.name]

    @property
    def data_name(self) -> str:
        return self.view_name.removesuffix(".md") + DATA_SUFFIX

    @property
    def labels(self) -> tuple:
        return tuple(item.label for item in self.fields)

    @property
    def keys(self) -> tuple:
        return tuple(item.key for item in self.fields)

    def field(self, key: str) -> Field | None:
        return next((item for item in self.fields if item.key == key), None)


def _fields(*rows) -> tuple:
    return tuple(Field(*row) for row in rows)


METRICS_FIXED = _fields(("date", "Date", KIND_DATE), ("unit", "Unit"))

INGEST_LOG = Registry(
    name="ingest_log", regime=REGIME_APPEND_ONLY, spec="§2.6, §12 G6",
    fields=_fields(
        ("date", "Date", KIND_DATE),
        # Ruta destino real (unidad · `evidence/<class>/` · casa de `hard-doc`)
        # o el puntero externo de un hard-doc que vive afuera — no hay bandeja.
        ("destination", "Destination"),
        ("class", "Class"),
        ("sha256", "sha256"),
        ("origin", "Origin"),
        ("outcome", "Original"),
    ),
)

SUPERSESSIONS = Registry(
    name="supersessions", regime=REGIME_APPEND_ONLY, spec="§0.2 #2, §12 G6",
    fields=_fields(
        ("date", "Date", KIND_DATE),
        ("superseded", "Superseded record"),
        ("superseded_by", "Superseded by"),
        ("reason", "Reason"),
    ),
)

MIGRATIONS = Registry(
    name="migrations", regime=REGIME_APPEND_ONLY, spec="§9.2, §12 G6",
    fields=_fields(
        ("date", "Date", KIND_DATE),
        ("pass", "Pass"),
        ("from_version", "From"),
        ("to_version", "To"),
        ("summary", "What changed"),
        ("changes", "Detail", KIND_LIST, False),
        ("verification", "Verification"),
        ("out_of_scope", "Out of scope, and why", KIND_TEXT, False),
    ),
)

QA_AUDITS = Registry(
    name="qa_audits", regime=REGIME_APPEND_ONLY, spec="§10.2, §12 G6",
    fields=_fields(
        ("date", "Date", KIND_DATE),
        ("unit", "Unit"),
        ("method", "Method"),
        ("sample", "Sample"),
        ("result", "Result"),
        ("notes", "Notes", KIND_TEXT, False),
    ),
)

#: Los gates que instancia el playbook de inception de la spec (§11.1). Son
#: **nombres canónicos recomendados**, no un enum cerrado del schema: §11.1 dice
#: que qué gates existen es un playbook por tipo de flujo, y el kit no congela
#: un playbook. Las skills escriben estos; una fila histórica con otro texto se
#: lee igual (§13.2) — el registry es append-only y no se reescribe.
GATE_KINDS = ("constitution-ratification", "map-ratification", "report-qa",
              "kill-criteria", "synthesis", "ratified-block-amendment")
SYNTHESIS_GATE = "synthesis"
#: Cómo se reconoce el gate de síntesis, incluido el dialecto con que pudo
#: haberse escrito antes de que existiera el nombre canónico.
SYNTHESIS_ALIASES = (SYNTHESIS_GATE, "sintesis", "síntesis")


def is_synthesis_gate(value) -> bool:
    text = str(value or "").strip().lower()
    return any(alias in text for alias in SYNTHESIS_ALIASES)


GATES = Registry(
    name="gates", regime=REGIME_APPEND_ONLY, spec="§7.4, §11.1, §12 G6",
    fields=_fields(
        ("date", "Date", KIND_DATE),
        ("gate", "Gate"),
        ("decision", "Decision"),
        ("amends", "Amends", KIND_TEXT, False),
        ("record_out", "Record out"),
    ),
)

CONFLICTS = Registry(
    name="conflicts", regime=REGIME_MARKABLE, spec="§1.5, §12 G6",
    key="id", markable=("evidence_weight", "resolution", "status"),
    fields=_fields(
        ("id", "ID"),
        ("units", "Units", KIND_LIST),
        ("records", "Records"),
        ("description", "Description"),
        ("evidence_weight", "Evidence weight", KIND_TEXT, False),
        ("resolution", "Resolution", KIND_TEXT, False),
        ("status", "Status", KIND_TEXT, True, CONFLICT_STATUSES),
        ("date", "Date", KIND_DATE),
    ),
)

#: Claves de la RTM, alineadas 1:1 con las columnas del report (`kitlib.report`)
#: más las dos que agrega el registry. Las etiquetas salen de ahí: un contrato,
#: un lugar.
REQUIREMENT_KEYS = ("id", "requirement", "why", "evidence", "scope", "area",
                    "status", "invalidation")

REQUIREMENTS = Registry(
    name="requirements", regime=REGIME_MARKABLE, spec="§10.2, §12 G6",
    key="id", markable=("status", "invalidation"),
    fields=tuple(
        Field(key, label, KIND_TEXT, key != "invalidation")
        for key, label in zip(REQUIREMENT_KEYS, REQ_COLUMNS + REGISTRY_EXTRA_COLUMNS)
    ),
)

STATUS = Registry(
    name="status", regime=REGIME_DERIVED, spec="§12 G6",
    fields=(),
)

#: Los registries con datos propios. `status` deriva de los protocols.
DATA_REGISTRIES = (INGEST_LOG, SUPERSESSIONS, MIGRATIONS, QA_AUDITS, GATES,
                   CONFLICTS, REQUIREMENTS)

#: Registries append-only (spec §12, G6). Lo declara la vista y lo hace cumplir
#: la guarda **sobre el archivo de datos**.
APPEND_ONLY = tuple(item.name for item in DATA_REGISTRIES
                    if item.regime == REGIME_APPEND_ONLY) + ("metrics",)
MARKABLE = tuple(item.name for item in DATA_REGISTRIES
                 if item.regime == REGIME_MARKABLE)


def metrics_registry(config: Config) -> Registry:
    """Las columnas de métricas las declara `metrics.columns` de la config."""
    columns = tuple(Field(column.key, column.label) for column in config.metric_columns)
    return Registry(name="metrics", regime=REGIME_APPEND_ONLY, spec="§10.2, §12 G6",
                    fields=METRICS_FIXED + columns)


def schemas(config: Config) -> dict:
    """nombre lógico → schema, con `metrics` resuelto contra la config."""
    everything = (*DATA_REGISTRIES, metrics_registry(config), STATUS)
    return {item.name: item for item in everything}


def data_registries(config: Config) -> tuple:
    """Los ocho con archivo de datos, en orden estable."""
    resolved = schemas(config)
    return tuple(resolved[name] for name in
                 ("requirements", "conflicts", "metrics", "supersessions",
                  "ingest_log", "migrations", "qa_audits", "gates"))
