"""`framework.config.yaml` — el contrato del repo consumidor.

Un contrato, un lugar: rutas, gramática de IDs, contrato de corridas,
horizontes de caducidad y definiciones versionadas de métricas viven acá y
en ningún otro lado. Los scripts de `bin/` y el hook lo leen; nadie hardcodea.

El archivo es además el **ancla del repo**: los scripts del kit corren desde
el caché del plugin, así que la raíz NO se deriva de `__file__` — se busca
subiendo desde el directorio de trabajo hasta encontrar este archivo.
"""
from __future__ import annotations

import os
import re
from dataclasses import dataclass
from pathlib import Path

from . import yamlmin
from .errors import fail
from .vocab import VOLATILITY_WORDS

CONFIG_NAME = "framework.config.yaml"
KIT_DIR = ".inception-kit"
ROOT_ENV = "INCEPTION_KIT_REPO"
PROJECT_ENV = "CLAUDE_PROJECT_DIR"

DEFAULT_PATHS = {
    "research": "docs/research",
    "investigations": "docs/research/investigations",
    "registry": "docs/research/registry",
    "decisions": "docs/decisions",
    "inbox": "inbox",
    "constitution": "docs/research/constitution.md",
}
DEFAULT_ID_WIDTH = 2
DEFAULT_ID_CLASSES = {"r": "desk research", "f": "field work"}
DEFAULT_RUNS = {"default": 2, "default_mode": "independent"}
DEFAULT_HORIZONS = {"alta": 6, "media": 18, "baja": 36}
RUN_MODES = ("independent", "chained")
METRIC_KINDS = ("percent", "integer", "text")
STATUS_ORDER = ("pending", "frozen", "running", "qa", "done")

#: Nombres de los registries: los fija la spec, no el proyecto (una casa por cosa).
REGISTRY_FILES = {
    "status": "STATUS.md",
    "conflicts": "conflicts.md",
    "requirements": "requirements.md",
    "metrics": "metrics.md",
    "supersessions": "supersessions.md",
    "ingest_log": "ingest-log.md",
    "migrations": "migrations.md",
    "qa_audits": "qa-audits.md",
}


@dataclass(frozen=True)
class MetricColumn:
    key: str
    label: str
    kind: str
    tokens: tuple

    @property
    def flag(self) -> str:
        return f"--{self.key}"


@dataclass(frozen=True)
class Config:
    root: Path
    data: dict

    # — rutas —
    def path(self, name: str) -> Path:
        return self.root / self.data["paths"][name]

    @property
    def research(self) -> Path:
        return self.path("research")

    @property
    def investigations(self) -> Path:
        return self.path("investigations")

    @property
    def registry(self) -> Path:
        return self.path("registry")

    @property
    def decisions(self) -> Path:
        return self.path("decisions")

    @property
    def inbox(self) -> Path:
        return self.path("inbox")

    @property
    def constitution(self) -> Path:
        return self.path("constitution")

    def registry_file(self, name: str) -> Path:
        return self.registry / REGISTRY_FILES[name]

    def relative(self, path: Path) -> str:
        try:
            return str(Path(path).resolve().relative_to(self.root))
        except ValueError:
            return str(path)

    # — IDs —
    @property
    def id_width(self) -> int:
        return self.data["ids"]["width"]

    @property
    def id_classes(self) -> dict:
        return self.data["ids"]["classes"]

    # — corridas —
    @property
    def runs_default(self) -> int:
        return self.data["runs"]["default"]

    @property
    def runs_default_mode(self) -> str:
        return self.data["runs"]["default_mode"]

    # — caducidad —
    @property
    def horizons(self) -> dict:
        return self.data["horizons"]

    # — métricas —
    @property
    def metrics_version(self) -> int:
        return self.data["metrics"]["version"]

    @property
    def metric_columns(self) -> tuple:
        return tuple(
            MetricColumn(
                key=column["key"],
                label=column["label"],
                kind=column.get("kind", "text"),
                tokens=tuple(column.get("tokens") or ()),
            )
            for column in self.data["metrics"]["columns"]
        )

    # — records —
    @property
    def extra_immutable_paths(self) -> tuple:
        return tuple(self.data["records"]["extra_immutable_paths"] or ())

    @property
    def kit_version(self) -> str:
        return str(self.data.get("kit_version") or "0.0.0")


def find_repo_root(start: Path | None = None) -> Path:
    """Sube desde `start` hasta encontrar `framework.config.yaml`.

    Prioridad: `$INCEPTION_KIT_REPO` → `start` → `$CLAUDE_PROJECT_DIR` → cwd.
    """
    override = os.environ.get(ROOT_ENV)
    if override:
        root = Path(override).expanduser().resolve()
        if not (root / CONFIG_NAME).is_file():
            fail(f"{ROOT_ENV}={root}: no encuentro {CONFIG_NAME} ahí")
        return root
    begin = Path(start or os.environ.get(PROJECT_ENV) or Path.cwd()).resolve()
    for candidate in (begin, *begin.parents):
        if (candidate / CONFIG_NAME).is_file():
            return candidate
    fail(f"no encuentro {CONFIG_NAME} desde {begin} hacia arriba — "
         f"¿corriste `kit-init` en este repo?")


def read_yaml(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    try:
        import yaml
    except ImportError:
        return yamlmin.load(text, source=path.name) or {}
    try:
        return yaml.safe_load(text) or {}
    except yaml.YAMLError as error:  # pragma: no cover - depende del archivo
        fail(f"{path}: YAML inválido — {error}")


def load(start: Path | None = None) -> Config:
    root = find_repo_root(start)
    data = merge_defaults(read_yaml(root / CONFIG_NAME))
    validate(data, root / CONFIG_NAME)
    return Config(root=root, data=data)


def merge_defaults(raw: dict) -> dict:
    paths = {**DEFAULT_PATHS, **(raw.get("paths") or {})}
    ids = raw.get("ids") or {}
    runs = raw.get("runs") or {}
    records = raw.get("records") or {}
    metrics = raw.get("metrics") or {}
    return {
        "kit_version": raw.get("kit_version"),
        "paths": paths,
        "ids": {
            "width": ids.get("width", DEFAULT_ID_WIDTH),
            "classes": ids.get("classes") or dict(DEFAULT_ID_CLASSES),
        },
        "runs": {
            "default": runs.get("default", DEFAULT_RUNS["default"]),
            "default_mode": runs.get("default_mode", DEFAULT_RUNS["default_mode"]),
        },
        "horizons": raw.get("horizons") or dict(DEFAULT_HORIZONS),
        "metrics": {
            "version": metrics.get("version", 1),
            "columns": metrics.get("columns") or [],
        },
        "records": {"extra_immutable_paths": records.get("extra_immutable_paths") or []},
    }


def stamp_kit_version(text: str, version: str) -> str:
    """Sella `kit_version:` en el texto del config sin tocar comentarios ni orden."""
    updated, count = re.subn(r"^kit_version:.*$", f"kit_version: {version}",
                             text, count=1, flags=re.M)
    if count:
        return updated
    return f"kit_version: {version}\n" + text


def validate(data: dict, source: Path) -> None:
    problems: list[str] = []
    for name, value in data["paths"].items():
        if not isinstance(value, str) or value.startswith("/") or ".." in value:
            problems.append(f"paths.{name}: debe ser una ruta relativa al repo, sin `..`")

    width = data["ids"]["width"]
    if not isinstance(width, int) or width < 1:
        problems.append("ids.width: entero ≥ 1 (default 2; al desbordar el ancho crece)")
    classes = data["ids"]["classes"]
    if not isinstance(classes, dict) or not classes:
        problems.append("ids.classes: mapa `prefijo: descripción`, no vacío")
    else:
        for prefix in classes:
            if not (isinstance(prefix, str) and len(prefix) == 1 and prefix.isalpha()
                    and prefix.islower()):
                problems.append(f"ids.classes: prefijo '{prefix}' — una sola letra minúscula")

    if not isinstance(data["runs"]["default"], int) or data["runs"]["default"] < 1:
        problems.append("runs.default: entero ≥ 1")
    if data["runs"]["default_mode"] not in RUN_MODES:
        problems.append(f"runs.default_mode: uno de {list(RUN_MODES)}")

    horizons = data["horizons"]
    if set(horizons) != set(VOLATILITY_WORDS):
        problems.append(f"horizons: claves exactas {list(VOLATILITY_WORDS)} "
                        f"(el enum migra con la spec v0.3, no acá)")
    else:
        for key, months in horizons.items():
            if not isinstance(months, int) or months < 1:
                problems.append(f"horizons.{key}: meses como entero ≥ 1")

    columns = data["metrics"]["columns"]
    if not columns:
        problems.append("metrics.columns: al menos una columna (QA que no mide nada es ceremonia)")
    seen = set()
    for index, column in enumerate(columns):
        if not isinstance(column, dict) or "key" not in column or "label" not in column:
            problems.append(f"metrics.columns[{index}]: requiere `key` y `label`")
            continue
        key = column["key"]
        if key in seen:
            problems.append(f"metrics.columns: `{key}` duplicada")
        seen.add(key)
        kind = column.get("kind", "text")
        if kind not in METRIC_KINDS:
            problems.append(f"metrics.columns[{key}].kind: uno de {list(METRIC_KINDS)}")

    if problems:
        fail(f"{source}: configuración inválida\n  - " + "\n  - ".join(problems))
