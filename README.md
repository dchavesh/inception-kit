# inception-kit

El **inception-framework** completo en una sola casa: spec, scripts, skills, plantillas y hook, empaquetado como **plugin de Claude Code** (este repo es también su marketplace) y consumido por los proyectos blite.

**Estado: 0.1.0** — la extracción de Fase 1 está hecha: 10 comandos en `bin/`, 6 skills con sus plantillas, `kit-init` idempotente y la guarda de inmutabilidad, todo generalizado vía `framework.config.yaml` (ver `CHANGELOG.md`). Pendiente: la spec v0.3 se redacta en este repo (Fase 2) y los flujos de entrada llegan en Fase 3. El plan de mejoras vigente vive en `meridian/docs/research/` vía su `registry/supersessions.md` y migra acá con la adopción.

## Contrato ratificado (2026-08-18)

| Decisión | Valor |
|---|---|
| Hogar remoto | `gitlab.com/blite-systems/tools/inception-kit` (subgrupo `tools` = categoría local — mapeo 1:1, misma descripción que el manifest) |
| Hogar local | `~/projects/blite/tools/inception-kit` (categoría `blite/tools`) |
| Nombre | `inception-kit` — repo, plugin y namespace de skills (`/inception-kit:…`); jamás se renombra |
| Spec | Vive ACÁ (una casa por cosa): la v0.3 se redacta en este repo; daedalus pasa a consumidor |
| Distribución | Plugin de Claude Code + marketplace en este mismo repo; instalación/updates por https (credencial oauth de la máquina, verificada; el alias SSH `gitlab-blite` queda para uso interactivo) |
| Versionado | Semver explícito desde `0.1.0` + `CHANGELOG.md`; update = bump del kit, jamás cirugía por repo; `autoUpdate` encendido en consumidores |
| Contenido v0.1 | 10 scripts generalizados (`bin/`) · **6 skills**: `launch`, `close`, `synthesis`, `status`, `ingest`, `plan` (el cierre retro-lenient no es skill: lo absorbe el flujo `/adopt`) · plantillas internas al plugin · hook de inmutabilidad + `kit-init` idempotente (única costura por-repo) · skills de claude.ai: `research-preflight`, `research-close`, `new-run` (en `claude-ai-skills/`; el humano las copia a su cuenta) · `framework.config.yaml` por proyecto |
| Nomenclatura | **Inglés** para todo nombre de skill, comando, campo de contrato, operación y definición — **incluidos los valores de enum**: madurez `established / supported / plausible / speculative`, volatilidad `high / medium / low` (ratificado 2026-08-18, adelantado al gate de la spec); un solo idioma, cero híbridos. Los parsers, plantillas y corpus nuevos migran JUNTOS con la spec v0.3 — jamás a medias |
| Runs | `runs: N` + `mode: independent \| chained` en el protocol (default `independent`); etiquetas `run-01..run-NN` (un nombre por concepto — "C1/C2" del corpus histórico = "corrida", queda solo en records inmutables con glosario); `chained` = partes deliberadas, una unidad epistémica; el contexto se declara, jamás se improvisa |
| Contexto | Postura declarable por unidad: `context: clean-room \| scoped` — clean-room para exploración/competencia de ideas/etapas tempranas (solo objetivo neutral, cero ideología del proyecto — generaliza la sala limpia y "la semilla nunca viaja"); scoped para integración (needs + decisiones vigentes, nada más). Contra el eco por frecuencia (acoplamiento ideológico) |
| IDs | Llave estable "tonta" + slug + índice generado (los smart codes se rechazan: el significado embebido se pudre y los IDs jamás se renombran). Prefijos = set cerrado por clase (`r` desk, `f` field; extensión solo por config). `id_width` configurable (default 2), desborde crece (`r99`→`r100`), orden SIEMPRE numérico, hex rechazado. Conflictos: `rNN-conNN` local · `con-NN` registry. Enum de madurez único, pinneado en el payload |
| Migración | Por capas, voluntaria, al subir versión del kit/spec (`/migrate`; `kit-init` es su runner): evergreen in-place · derivados regenerados · records de lectura por supersesión mecánica (diff como evidencia) · **verbatim bronze jamás se reescribe** (se lee con glosario histórico). **Rastro obligatorio:** log de migraciones en el registry + anotación en el sidecar de cada record afectado — la incisión va al sidecar, jamás a los bytes (el sha256 es la identidad del record) |
| Validación | Repos desechables durante el desarrollo (sembrados por `kit-init`). El diagnóstico read-only de **Chimera** ya se ejecutó (2026-08-18, `meridian/docs/research/diagnostico-chimera-v1.md`) y alimenta el diseño de `/normalize` — veredicto: cero mecanismos nuevos requeridos |
| Adopción | **DESPUÉS de completar las fases 1–3** (ratificado 2026-08-18): ningún proyecto va primero por diseño — meridian, daedalus, chimera-refactor y los demás reciben lo mismo; validación del desarrollo contra repos desechables, jamás proyectos reales |

## Principios (heredados del plan de mejoras — no negociables)

Simplicidad — un mecanismo por problema; los edge cases se adaptan al framework, jamás al revés. Skills sin lógica de negocio. Procesos endurecidos, investigación libre. Un contrato, un lugar, varios lectores. Colocación por unidad. El norte: **coordinación · organización · extracción**.

## Qué hay adentro

```
.claude-plugin/     plugin.json + marketplace.json (el repo es su propio marketplace)
bin/                los 10 comandos deterministas — van al PATH de Bash con el plugin activo
  kitlib/           núcleo compartido: config, IDs, parsing, fechas, vocabulario, registries
skills/             las 6 skills del plugin, con sus plantillas adentro
templates/          lo que kit-init siembra en un repo: framework.config.yaml + hook
claude-ai-skills/   las 3 skills del otro lado de la frontera (el humano las copia — ver su README)
```

| Comando | Qué hace |
|---|---|
| `kit-init` | siembra el repo, instala el hook y corre las migraciones. Idempotente |
| `doctor` | integridad del repo: instalación, protocols, findings, supersesiones, IDs, tablero |
| `derive-status` | regenera el tablero derivado desde los frontmatter |
| `derive-review-by` | deriva `review_by` por hallazgo y lista vencidos |
| `validate-report` | valida el formato del report de una unidad (`--lenient` reservado a `/adopt`) |
| `claim-audit-sample` | muestra determinista de afirmaciones + candidatos a eco |
| `extract-registry` | extrae requisitos a la RTM (con marks) y propaga enmiendas |
| `append-metrics` | agrega la fila de métricas del cierre (columnas desde la config) |
| `freeze-protocols` | `pending → frozen`. Gate humano: exige `--confirm` |
| `ingest` | ingesta verificada al inbox; borra el original solo tras verificar el remoto |

| Skill | Qué hace |
|---|---|
| `/inception-kit:plan` | necesidad → mapa de unidades + Bloque Común + protocols en `pending` |
| `/inception-kit:launch` | payload de una unidad frozen+ready, preflight incluido; sella session |
| `/inception-kit:close` | QA completo → RTM → métricas → findings → `done` |
| `/inception-kit:status` | tablero + caducidad + integridad + próxima acción |
| `/inception-kit:ingest` | ingesta verificada de archivos externos |
| `/inception-kit:synthesis` | pre-flight PASS/FAIL y, con orden humana, el fan-in |

## Instalación

En Claude Code, una vez por máquina:

```
/plugin marketplace add https://gitlab.com/blite-systems/tools/inception-kit.git
/plugin install inception-kit@inception-kit
```

Y una vez por repo consumidor, desde su raíz:

```
kit-init
```

`kit-init` es idempotente y es también el runner de migraciones: se vuelve a
correr después de cada update del kit. Las skills de claude.ai se instalan
aparte, una vez por cuenta — ver `claude-ai-skills/README.md`.

**Requisitos:** git y Python 3.10+. Sin dependencias: si PyYAML está instalado
se usa, y si no, el kit trae su propio lector del subconjunto de YAML que la
config necesita.

## Cómo se lee un repo con el kit puesto

- **`framework.config.yaml`** en la raíz es el contrato y el ancla: los
  comandos encuentran el repo subiendo hasta él.
- **`.inception-kit/`** es la costura: el hook y su librería, vendorizados y
  versionados con el repo — nada apunta al caché del plugin, así que el hook
  corre aunque Claude Code no esté instalado.
- El shim del hook va a la **ruta efectiva** que dicte `core.hooksPath`; si el
  repo ya tenía un `pre-commit`, se conserva como `pre-commit.local` y sigue
  corriendo primero.
