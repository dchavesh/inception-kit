"""Los registries: encabezados, columnas y semillas.

Cada registry se define UNA vez acá: `kit-init` lo siembra desde esta
definición y los scripts que le agregan filas usan las mismas columnas. Nadie
copia un encabezado a mano — un contrato, un lugar, varios lectores.

Los nombres de columna van en inglés (principio #6); la prosa del corpus, no.
"""
from __future__ import annotations

from .config import Config
from .report import REGISTRY_EXTRA_COLUMNS, REQ_COLUMNS

CONFLICT_COLUMNS = ("ID", "Units", "Records", "Description", "Evidence weight",
                    "Resolution", "Status", "Date")
INGEST_COLUMNS = ("Date", "File in inbox", "sha256 (12)", "Origin", "Original")
SUPERSESSION_COLUMNS = ("Superseded record", "Superseded by", "Date", "Reason")
METRICS_FIXED_COLUMNS = ("Date", "Unit")

#: Valores del campo `Status` de la RTM (interfaz del kit, en inglés).
STATUS_NEW = "new"
STATUS_DUPLICATE = "duplicate"
STATUS_CONTRADICTS = "contradicts"
STATUS_SUPERSEDED = "SUPERSEDED by"
STATUS_INVALIDATED = "⚠ invalidated"


def table(columns) -> str:
    return ("| " + " | ".join(columns) + " |\n"
            + "|" + "|".join("---" for _ in columns) + "|\n")


def requirements_seed(config: Config) -> str:
    return (
        "# Registry — Requirements (RTM)\n\n"
        "*Agregada en cada close por `extract-registry`. Las filas jamás se borran: "
        "una fila superada se marca `SUPERSEDED by <id>`; una enmienda a un record "
        "citado propaga marca en `Invalidation`.*\n\n"
        + table(REQ_COLUMNS + REGISTRY_EXTRA_COLUMNS)
    )


def conflicts_seed(config: Config) -> str:
    return (
        "# Registry — Conflicts\n\n"
        "*Contradicciones entre corridas y entre unidades. Solo se anotan acá: se "
        "resuelven en la síntesis o en el gate que cada fila asigne. IDs `con-NN`, "
        "permanentes, jamás reutilizados.*\n\n"
        + table(CONFLICT_COLUMNS)
    )


def metrics_seed(config: Config) -> str:
    columns = METRICS_FIXED_COLUMNS + tuple(c.label for c in config.metric_columns)
    return (
        "# Registry — Metrics\n\n"
        f"<!-- metrics-version: {config.metrics_version} -->\n\n"
        "*Record append-only: una fila por close, vía `append-metrics`. QA que no mide "
        "nada es ceremonia. Las columnas las define `metrics.columns` de "
        "`framework.config.yaml`; cambiar la definición sube `metrics.version` y lo "
        "ejecuta `/migrate`, jamás una edición a mano.*\n\n"
        + table(columns)
    )


def supersessions_seed(config: Config) -> str:
    return (
        "# Registry — Supersessions\n\n"
        "*Record append-only. La supersesión es una operación, no una convención "
        "(spec §1.2): el record superado JAMÁS se borra ni se edita — queda marcado "
        "acá, y los scripts resuelven siempre a la versión vigente (mayor "
        "`NN-kind.vN.md`, o la base). Consumidor: la síntesis y cualquier lector de un "
        "record superado; momento: antes de citar.*\n\n"
        + table(SUPERSESSION_COLUMNS)
    )


def ingest_log_seed(config: Config) -> str:
    return (
        "# Registry — Ingest log\n\n"
        "*Record append-only: una fila por archivo ingerido vía `ingest`. La "
        "procedencia de lo que entra al repo se registra acá; el original se borra "
        "solo tras verificar la copia contra el remoto.*\n\n"
        + table(INGEST_COLUMNS)
    )


def migrations_seed(config: Config) -> str:
    return (
        "# Registry — Migrations\n\n"
        "*Record append-only (principio #7 — sintonía por migración): una entrada por "
        "pase de migración, con qué cambió, cuándo, a qué versión y cómo se verificó. "
        "La incisión de vocabulario va al sidecar del record migrado, jamás dentro del "
        "verbatim: un byte añadido rompe la cadena sha256 que lo hace auditable. "
        "Consumidor: quien lea un record superado o audite una migración; momento: "
        "antes de citar vocabulario.*\n"
    )


def qa_audits_seed(config: Config) -> str:
    return (
        "# Registry — QA Audits\n\n"
        "*Record append-only: el rastro reproducible de la auditoría de afirmaciones "
        "de cada `/close` (spec §5 — toda verificación deja rastro como record). El "
        "resumen cuantitativo vive en `metrics.md`; acá vive el detalle de qué se "
        "probó, cómo y con qué resultado. Consumidor: la síntesis y el humano al "
        "ponderar la madurez de una unidad.*\n"
    )


#: Registries append-only: su propio encabezado lo declara, y el hook lo hace
#: cumplir. `requirements` y `conflicts` NO están: sus filas se marcan (fila
#: superada, conflicto resuelto) sin borrarse — se editan por diseño.
APPEND_ONLY = ("metrics", "ingest_log", "supersessions", "migrations", "qa_audits")

#: nombre lógico → función que lo siembra
SEEDS = {
    "requirements": requirements_seed,
    "conflicts": conflicts_seed,
    "metrics": metrics_seed,
    "supersessions": supersessions_seed,
    "ingest_log": ingest_log_seed,
    "migrations": migrations_seed,
    "qa_audits": qa_audits_seed,
}
