# inception-kit

El **inception-framework** completo en una sola casa: spec, scripts, skills, plantillas y hook, empaquetado como **plugin de Claude Code** (este repo es también su marketplace) y consumido por los proyectos blite.

**Estado: 0.4.1** — el framework **completo** sobre la `SPEC.md` **v0.4 ratificada** (2026-08-20): a la integridad profunda de 0.3.0 se suman los **tres flujos de entrada** —`/inception` (idea nueva), `/adopt` (corpus artesanal), `/normalize` (repo existente), **y no hay más entradas**— y **`/distill`**, que lleva el bronze no investigativo hasta el conocimiento por el mismo carril de procedencia. La v0.4 canonizó esa práctica y 0.4.1 alineó el tooling a su letra (ver `CHANGELOG.md`).

**La spec manda.** `SPEC.md` es la constitution del framework y la única fuente normativa: los `§` que citan scripts y skills apuntan ahí. Enmendarla exige bump de `version:`, fila de changelog y gate humano.

## Contrato ratificado (2026-08-18, activado en 0.2.0)

| Decisión | Valor |
|---|---|
| Hogar remoto | `gitlab.com/blite-systems/tools/inception-kit` (subgrupo `tools` = categoría local — mapeo 1:1, misma descripción que el manifest) |
| Hogar local | `~/projects/blite/tools/inception-kit` (categoría `blite/tools`) |
| Nombre | `inception-kit` — repo, plugin y namespace de skills (`/inception-kit:…`); jamás se renombra |
| Spec | Vive ACÁ (una casa por cosa): `SPEC.md` v0.4, clase constitution, `status: ratified` (2026-08-20; la v0.3 lo fue el 2026-08-19). Un repo consumidor no la copia — la referencia por el `kit_version` que declara su config |
| Distribución | Plugin de Claude Code + marketplace en este mismo repo; instalación/updates por https (credencial oauth de la máquina, verificada; el alias SSH `gitlab-blite` queda para uso interactivo) |
| Versionado | Semver explícito desde `0.1.0` + `CHANGELOG.md`; update = bump del kit, jamás cirugía por repo; `autoUpdate` encendido en consumidores |
| Contenido | 16 scripts generalizados (`bin/`) · **11 skills**: los tres flujos de entrada `inception`, `adopt`, `normalize` + `plan`, `launch`, `close`, `synthesis`, `distill`, `ingest`, `migrate`, `status` (el cierre retro-lenient no es skill: lo absorbe el flujo `/adopt`) · plantillas internas al plugin · hook de inmutabilidad + `kit-init` idempotente (única costura por-repo) · skills de claude.ai: `research-preflight`, `research-close`, `new-run` (en `claude-ai-skills/`; el humano las copia a su cuenta) · `framework.config.yaml` por proyecto |
| Entradas | **Tres, y no hay más** (pipelines de normalización): `/inception` (idea nueva → elicitación idea-agnóstica → semilla + constitution neutral → R0 en `pending`) · `/adopt` (corpus artesanal sin repo → retro-parse, protocols retroactivos, cierre retro-lenient anotado) · `/normalize` (repo con documentación → inventario → clases → estandarizar → retención y borrado). Un edge case no se le agrega al framework: se normaliza hacia él |
| Destilación | `/distill` cierra el medallion para el bronze que no es una corrida: silver re-derivable con locators por clase, borrador de gold con techo de madurez (una sola fuente no da `established`), y el sello como anotación append-only del sidecar. **La carga sin destilar es deuda** y `check-recurrence` la lista (spec §2.4) |
| Nomenclatura | **Inglés** para todo nombre de skill, comando, campo de contrato, columna, operación y definición — **incluidos los valores de enum**: madurez `established / supported / plausible / speculative`, volatilidad `high / medium / low`. **Vigente desde 0.2.0**: parsers, plantillas y claves de `horizons` migraron juntos, jamás a medias. El corpus histórico no se reescribe: se lee con el glosario de spec §13.2 |
| Idioma de prosa | `language:` en la config (arranque `en`, spec §1.8). El framework es inglés; la **prosa** —cuerpo de protocols, reports, findings, sources, payloads, constitution y ADRs, y lo que las skills le dicen al humano— va en el idioma declarado. **Una sola versión de cada skill y plantilla**: jamás copias traducidas. Cambiarlo tras el primer artefacto es migración |
| Ingesta | **Destino obligatorio, tres formas** (spec §2.6): unidad (`--unit [--run N]` → `raw/`), clase sin unidad (`--class` → `evidence/<class>/` con sidecar), documentación dura (`--hard-doc`, o `--external` con puntero + `sha256` + sidecar en el ingest-log). **El `inbox` no existe**: el único staging es externo al repo, y ante ambigüedad la ingesta pregunta y no avanza |
| Runs | `runs: N` + `mode: independent \| chained` en el protocol (default `independent`); etiquetas `run-01..run-NN` (un nombre por concepto — "C1/C2" del corpus histórico = "corrida", queda solo en records inmutables con glosario); `chained` = partes deliberadas, una unidad epistémica; el contexto se declara, jamás se improvisa |
| Contexto | Postura declarable por unidad: `context: clean-room \| scoped`, con default en la config. **Vigente desde 0.2.0**: `/launch` compone el payload por postura (`scoped` = preflight + briefing + findings de sus `needs` + protocol; `clean-room` = preflight + protocol, nada más) y `doctor` hace cumplir las tres guardas — `clean-room` exige `needs: []`, el payload sellado existe desde `running`, y el corpus es solo-vigente. Contra el eco por frecuencia |
| Bloque ratificado | `horizons`, `runs`, `ids`, `metrics` y `context` portan autoridad epistémica: cambiarlos exige subir `version:` de la constitution **en el mismo commit** (spec §12 G4), y la guarda lo hace cumplir. El resto de la config es operativo — que no es gratis: mover una ruta o cambiar `language` arrastra migración |
| IDs | Llave estable "tonta" + slug + índice generado (los smart codes se rechazan: el significado embebido se pudre y los IDs jamás se renombran). Prefijos = set cerrado por clase (`r` desk, `f` field; extensión solo por config). `id_width` configurable (default 2), desborde crece (`r99`→`r100`), orden SIEMPRE numérico, hex rechazado. Conflictos: `rNN-conNN` local · `con-NN` registry. Enum de madurez único, pinneado en el payload |
| Registries | **Datos con schema desde 0.3.0**: `<registry>/data/*.jsonl` (JSON Lines, un objeto por línea) y el `.md` es su **vista generada**. Se eligió JSONL porque append-only es literalmente agregar una línea — verificable byte a byte sin parser, y `json` es stdlib. Los tres regímenes de spec §12 G6 se hacen cumplir sobre los datos: **append-only** (6), **marcable** (2, solo mutan los campos declarados) y **vista derivada** (`STATUS.md`). El comando `registry` es la única puerta de escritura; `doctor` valida schema y sintonía de cada vista |
| Índice | **`INDEX.md` en la raíz, generado** (`derive-index`, spec §1.2/§4.5): tablero con el objetivo de cada unidad en una línea, ADRs vigentes, conflictos abiertos, síntesis vigente y dónde vive cada clase de cosa. Puntero delgado y vista derivada: **ninguna regla vive ahí** — si se borra, solo se pierde el atajo. La prosa va en `language`; columnas, IDs y enums en inglés |
| Migración | Por capas, voluntaria, al subir versión del kit/spec (`/migrate`; `kit-init` es su runner de versiones): evergreen in-place · derivados regenerados · records de lectura por **supersesión mecánica con opt-in y round-trip** (el diff es la evidencia; si el original no se reconstruye byte a byte, el pase se aborta) · **verbatim bronze jamás se reescribe** — a lo sumo se **reubica**, con `sha256` idéntico antes y después. **Rastro obligatorio:** entrada en el registry de migraciones + anotación en el sidecar de cada record afectado — la incisión va al sidecar, jamás a los bytes |
| Recurrencia | `check-recurrence` deriva las dos capas de spec §6 —`review_by` vencidos y cadencias `refresh:` cumplidas— y **PROPONE** relanzamientos y re-síntesis. Jamás ejecuta ni escribe: los gates son humanos. Exit 1 cuando hay algo que proponer; `templates/ci/recurrence.yml` lo corre periódicamente (opcional) |
| Validación | Repos desechables durante el desarrollo (sembrados por `kit-init`). El diagnóstico read-only de **Chimera** ya se ejecutó (2026-08-18, `meridian/docs/research/diagnostico-chimera-v1.md`) y alimenta el diseño de `/normalize` — veredicto: cero mecanismos nuevos requeridos |
| Adopción | **DESPUÉS de completar las fases 1–3** (ratificado 2026-08-18): ningún proyecto va primero por diseño — meridian, daedalus, chimera-refactor y los demás reciben lo mismo; validación del desarrollo contra repos desechables, jamás proyectos reales |

## Principios (heredados del plan de mejoras — no negociables)

Simplicidad — un mecanismo por problema; los edge cases se adaptan al framework, jamás al revés. Skills sin lógica de negocio. Procesos endurecidos, investigación libre. Un contrato, un lugar, varios lectores. Colocación por unidad. El norte: **coordinación · organización · extracción**.

## Qué hay adentro

```
SPEC.md             la constitution del framework — la fuente normativa
.claude-plugin/     plugin.json + marketplace.json (el repo es su propio marketplace)
bin/                los 16 comandos deterministas — van al PATH de Bash con el plugin activo
  kitlib/           núcleo compartido: config, IDs, parsing, fechas, vocabulario, registries,
                    frescura, relabel, sidecars, vistas derivadas, roster, inventario,
                    destilación, rutas de record y mecánica de pases
skills/             las 11 skills del plugin, con sus plantillas adentro
templates/          lo que kit-init siembra en un repo: framework.config.yaml + hook
                    (y `ci/recurrence.yml`, opcional, que el kit NO instala)
claude-ai-skills/   las 3 skills del otro lado de la frontera (el humano las copia — ver su README)
```

| Comando | Qué hace |
|---|---|
| `kit-init` | siembra el repo, instala el hook y corre las migraciones. Idempotente |
| `doctor` | integridad del repo: instalación, protocols, findings, supersesiones, IDs, tablero |
| `derive-status` | regenera el tablero derivado desde los frontmatter |
| `derive-index` | regenera `INDEX.md`, el índice puerta-de-entrada |
| `registry` | la única puerta de escritura del registry: `add`, `mark`, `render`, `show`, `schema` |
| `migrate` | migración por capas: `plan`, `derived`, `relabel`, `relocate` (todo pase escribe solo con `--apply`) |
| `normalize` | inventario read-only de un repo existente (roster §4.5, puntero delgado, monolitos, épocas, huérfanos) + `freeze` y `retire`, ambos solo con `--apply` |
| `distill` | sella la destilación de un bronze en su sidecar, tras re-verificar su `sha256` |
| `check-recurrence` | vencidos, cadencias cumplidas y carga sin destilar, con los relanzamientos que propone |
| `derive-review-by` | deriva `review_by` por hallazgo y lista vencidos |
| `validate-report` | valida el formato del report de una unidad (`--lenient` reservado a `/adopt`) |
| `claim-audit-sample` | muestra determinista de afirmaciones + candidatos a eco |
| `extract-registry` | extrae requisitos a la RTM (con marks) y propaga enmiendas |
| `append-metrics` | agrega la fila de métricas del cierre (columnas desde la config) |
| `freeze-protocols` | `pending → frozen`. Gate humano: exige `--confirm` |
| `ingest` | ingesta con destino obligatorio (unidad · clase · hard-doc); borra el original solo tras verificar el remoto |

| Skill | Qué hace |
|---|---|
| `/inception-kit:inception` | idea cruda → elicitación → semilla + constitution neutral → R0 en `pending` |
| `/inception-kit:adopt` | corpus artesanal sin repo → retro-parse + cierre retro-lenient anotado |
| `/inception-kit:normalize` | repo existente → inventario → clases → estandarizar → retención y borrado |
| `/inception-kit:distill` | bronze no investigativo → silver re-derivable + borrador de gold |
| `/inception-kit:plan` | necesidad → mapa de unidades + Bloque Común + protocols en `pending` |
| `/inception-kit:launch` | payload de una unidad frozen+ready, preflight incluido; sella session |
| `/inception-kit:close` | QA completo → RTM → métricas → findings → `done` |
| `/inception-kit:status` | tablero + índice + caducidad y recurrencia + integridad + próxima acción |
| `/inception-kit:migrate` | sintonía por capas: diagnóstico, derivados, supersesión mecánica y reubicación |
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
  comandos encuentran el repo subiendo hasta él. Su **bloque ratificado**
  (`horizons`, `runs`, `ids`, `metrics`, `context`) solo cambia por enmienda,
  con bump de la constitution en el mismo commit.
- **Las casas del framework** las declara `paths`: `research`,
  `investigations`, `registry`, `decisions`, `evidence` (bronze con clase pero
  sin unidad), `hard_docs` (documentación dura, que jamás se borra) y
  `constitution`. **No hay bandeja de entrada**: el staging es externo.
- **`INDEX.md`** en la raíz responde qué hay, qué está decidido, qué está en
  disputa y dónde vive cada cosa — sin abrir nada más. Es generado: para
  cambiarlo se cambia la fuente y se regenera.
- **El registry son los `.jsonl` de `<registry>/data/`**; los `.md` de al lado
  son sus vistas. Se escribe con `registry add` / `registry mark`, jamás a mano
  — y la guarda rechaza tanto pisar una fila como editar una vista.
- **`.inception-kit/`** es la costura: el hook y su librería, vendorizados y
  versionados con el repo — nada apunta al caché del plugin, así que el hook
  corre aunque Claude Code no esté instalado.
- El shim del hook va a la **ruta efectiva** que dicte `core.hooksPath`; si el
  repo ya tenía un `pre-commit`, se conserva como `pre-commit.local` y sigue
  corriendo primero.
