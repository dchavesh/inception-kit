# Changelog

Todas las versiones del `inception-kit`. Formato: [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/);
versionado: [SemVer](https://semver.org/lang/es/).

El kit se actualiza por **bump de versión**, jamás por cirugía repo por repo.
Al subir de versión, cada repo consumidor corre `kit-init` (runner de
migraciones) — principio #7, sintonía por migración.

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

[0.1.0]: https://gitlab.com/blite-systems/tools/inception-kit/-/tags/v0.1.0
