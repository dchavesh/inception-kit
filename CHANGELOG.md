# Changelog

Todas las versiones del `inception-kit`. Formato: [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/);
versionado: [SemVer](https://semver.org/lang/es/).

El kit se actualiza por **bump de versión**, jamás por cirugía repo por repo.
Al subir de versión, cada repo consumidor corre `kit-init` (runner de
migraciones) — principio #7, sintonía por migración.

## [0.2.0] — 2026-08-19

**La activación de la spec v0.3.** La spec quedó ratificada por gate humano el
2026-08-19 (`733b1d7`: acta A1–A14 + B1–B32); esta versión la implementa. Las
reglas que declaraban *regla de activación* —enum inglés, ingesta con destino
obligatorio, `language`, enforcement de `context` y del bloque ratificado—
entran **juntas, en un solo bump y jamás a medias** (spec §1.6, §9.4).

### Changed — BREAKING

- **Enum de madurez y volatilidad en INGLÉS**, en un pase indivisible:
  parsers (`kitlib/vocab.py` y sus lectores `doctor`, `validate-report`,
  `derive-review-by`), plantillas (report de `research-close`, protocol,
  preflight) y **claves de `horizons`** (`alta/media/baja` → `high/medium/low`).
  Valores: `established` · `supported` · `plausible` · `speculative` ·
  `high` · `medium` · `low`. **El corpus histórico NO se reescribe**: se lee con
  el glosario de spec §13.2, y `doctor` lo nombra como tal en vez de decir "no
  parseable" — migrarlo es supersesión mecánica con opt-in humano (`/migrate`).
- **El `inbox/` deja de existir** como ruta, como casa y como concepto
  (spec §2.6). El único staging es **externo al repo**. `paths` pierde `inbox`
  y gana `evidence` y `hard_docs`; la guarda de rutas pasa a proteger **las
  casas reales** donde el material aterriza. Un `inbox/` legado sigue protegido
  mientras exista, declarado en `records.extra_immutable_paths`.
- **`ingest` exige destino** — y hay exactamente tres: `--unit UNIT [--run N]`
  (el verbatim de una corrida aterriza **directo** en `<unit>/raw/run-NN.md`;
  `/close` solo verifica), `--class <clase>` → `<research>/evidence/<class>/`
  con sidecar de procedencia obligatorio, y `--hard-doc` → `paths.hard_docs`,
  o `--hard-doc --external PUNTERO` cuando el binario debe vivir afuera (el
  repo retiene puntero + `sha256` + sidecar, y la fila va al ingest-log).
  **Ante ambigüedad pregunta y no avanza**: sin destino, con dos, o con una
  clase fuera del enum, falla sin tocar nada. El desenlace del original no
  cambia: push fallido ⇒ **nada se borra**.
- **Nombres de sección y columna del report, en inglés** (`## 1. Summary` …
  `## 7. Requirements table`; `| ID | Title | Author/Org | Date | Type |
  Quality | Volatility |`). Son nombres de concepto y anclas del validador; la
  **prosa** debajo va en el idioma del repo.
- Las columnas del ingest-log nombran ahora la **ruta destino real**
  (`Destination`, `Class`). Un repo migrado conserva su encabezado: es
  append-only, y el cambio queda anotado en el log de migraciones.

### Added

- **`language:` en `framework.config.yaml`** (spec §1.8), valor de arranque
  `en`. La prosa de salidas y plantillas se escribe en él; nombres, campos,
  claves, enums, marks y columnas siguen **siempre** en inglés. Una sola versión
  de cada skill y plantilla: jamás copias traducidas. `kit-init` pide
  confirmarlo con el equipo — cambiarlo después es migración, no edición.
- **Enforcement de `context: clean-room | scoped`** (spec §8): campo en el
  protocol, `context.default` en la config, composición del payload por postura
  en `/launch`, y las tres guardas en `doctor` — `clean-room` exige `needs: []`,
  el payload sellado tiene que existir desde `running`, y el **corpus
  solo-vigente** (toda versión no vigente declarada como superada).
- **Gate del bloque ratificado** (spec §12 G4) en la guarda: cambiar
  `horizons`, `runs`, `ids`, `metrics` o `context` exige subir `version:` de la
  constitution **en el mismo commit**. Compara el *significado*, no la
  ortografía: el relabel mecánico del enum no dispara el gate; un número
  epistémico distinto, sí.
- **`registry/gates.md`** — el noveno registry, append-only: un registro por
  gate consumido (spec §7.4, §12 G6). `doctor` verifica el **set cerrado** de
  registries: falta uno, o sobra un `.md` no declarado, es problema de
  integridad.
- **Migración `0.1 → 0.2`** en el runner de `kit-init`: renombra las claves de
  `horizons`, saca `inbox` de `paths` y lo declara como ruta inmutable si el
  directorio existe, agrega `evidence`/`hard_docs`, siembra `language` y
  `context`, y deja el rastro obligatorio de spec §9.2 en el log de migraciones
  — **con lo que quedó fuera de alcance y por qué**. Idempotente.

### Fixed

- Los dos nits de 0.1.x: IDs de ejemplo neutros (`rXX`/`rYY`) en
  `skills/close/templates/marks.md`, y el comentario ilustrativo de
  `kitlib/installation.py` sin nombrar un proyecto consumidor.
- Referencias `§` de scripts y skills realineadas a la numeración de la spec
  v0.3 (la v0.2 numeraba distinto).

### Notas de contrato

- **Migran juntos o no migra ninguno.** Un repo 0.1.x que corre el kit 0.2.0 es
  un error de integridad hasta que corra `kit-init` (spec §9.3) — y después,
  sus records de lectura en dialecto histórico siguen reportados hasta que
  `/migrate` (Fase 3.5) ofrezca el pase de supersesión mecánica.
- **Lo que 0.2.0 NO hace:** no reescribe verbatim, no supersede records, no
  reconcilia `inbox/` legados y no genera el índice puerta-de-entrada. Todo eso
  es Fase 3.
- **Roster de archivos repo-level (spec §4.5):** `doctor` lo verifica donde es
  mecánicamente inequívoco — el set cerrado de registries. El censo de la raíz
  queda para `/normalize` (Fase 3): la tabla de §4.5 no declara fila para los
  documentos de plan, que §12 G1 sí exige (el briefing es su Parte II).
- **Adopción de proyectos: sigue fuera de alcance** hasta completar las fases
  1–3. 0.2.0 se validó contra repos desechables, jamás contra un proyecto real.

## [0.1.0] — 2026-08-18

Primera versión: la extracción de Fase 1 del plan de mejoras (v1.10). Los 10
scripts del coordinador de meridian salen de un repo y pasan a ser un plugin
generalizado por `framework.config.yaml`.

### Added

- **`bin/` — 10 comandos deterministas** (van al PATH de Bash con el plugin
  activo): `doctor`, `derive-status`, `derive-review-by`, `validate-report`,
  `claim-audit-sample`, `extract-registry`, `append-metrics`,
  `freeze-protocols`, `ingest` y `kit-init`. Sobre `bin/kitlib/`, el núcleo
  compartido (config, IDs, parsing markdown, fechas, vocabulario, registries).
- **`framework.config.yaml`** — el contrato por repo: rutas, gramática de IDs
  (`ids.width` default 2, prefijos como set cerrado por clase), contrato de
  corridas por defecto (`runs.default` + `runs.default_mode`), horizontes de
  caducidad y **definiciones versionadas de métricas** (cada columna es una
  flag de `append-metrics` y una columna del record append-only).
- **Orden SIEMPRE numérico** de unidades en todo tooling y vista
  (`r2 < r9 < r10 < r100`), jamás lexicográfico. El ancho de ID es mínimo: al
  desbordar crece y **nada se renumera**.
- **6 skills del plugin**: `launch`, `close`, `synthesis`, `status`, `ingest`,
  `plan` — con sus plantillas DENTRO del plugin (preflight de payload,
  gramática del archivo de marks, esqueletos de plan y de protocol).
  El preflight de `/launch` renderiza `runs: N` + `mode: independent | chained`
  con etiquetas `run-01..run-NN`.
- **`kit-init` idempotente**: siembra la estructura de un repo nuevo (config,
  carpetas y registries con su encabezado), **vendoriza el hook y su librería**
  en `.inception-kit/` e instala el shim en la **ruta efectiva de hooks**
  (`core.hooksPath`, nunca `.git/hooks` a ciegas ni el caché del plugin); un
  `pre-commit` ajeno preexistente se conserva como `pre-commit.local` y sigue
  corriendo primero. Es además el **runner de migraciones** entre versiones del
  kit, y deja rastro en el registry de migraciones.
- **Guarda de inmutabilidad** (git `pre-commit`): records, protocols sellables
  solo en frontmatter y solo hacia adelante, registries append-only y
  constitution con bump de versión obligatorio. Corre sin Claude Code ni
  dependencias instaladas.
- **`.claude-plugin/plugin.json` + `marketplace.json`**: el repo es su propio
  marketplace.
- **Skills de claude.ai** (`claude-ai-skills/`, ya ratificadas):
  `research-preflight`, `research-close`, `new-run` — con su paso de
  instalación documentado.

### Notas de contrato

- **Enums de madurez y volatilidad en ESPAÑOL, a propósito.** El enum inglés
  (`established/supported/plausible/speculative` · `high/medium/low`) está
  ratificado pero entra **junto con la spec v0.3**: parsers, plantillas y
  corpus migran a la vez, jamás a medias. Por eso el enum vive en el kit
  (`kitlib/vocab.py`) y no en la config: no es decisión por proyecto.
- **`validate-report --lenient` se conserva** como flag, sin skill que lo
  invoque: pertenece al retro-parse de corpus artesanal del flujo `/adopt`
  (Fase 3). `/close-lite` no existe.
- **La spec vive en este repo** y se redacta como v0.3 (Fase 2). Los `§`
  citados en scripts y skills apuntan a ella.
- **Adopción de proyectos: fuera de alcance** hasta completar las fases 1–3.
  0.1.0 se validó contra repos desechables, jamás contra un proyecto real.

[0.2.0]: https://gitlab.com/blite-systems/tools/inception-kit/-/tags/v0.2.0
[0.1.0]: https://gitlab.com/blite-systems/tools/inception-kit/-/tags/v0.1.0
