---
name: launch
description: Arma el payload de una unidad frozen+ready en su propia carpeta (preflight incluido) y, cuando el humano trae la URL del chat, sella session y commitea el payload como record. Uso — /inception-kit:launch UNIT_ID [URL del chat]
---

# /inception-kit:launch UNIT_ID

Lanza una unidad de investigación: el payload sale del repo, la sesión vive en
claude.ai. **La frontera son archivos.** Esta skill no porta ideas del
proyecto: arma un sobre y lo sella.

## 1. Precondiciones (verificar, no asumir)

Correr `derive-status`. La unidad debe estar **`frozen` y ready** (todos sus
`needs` en `done`):

- `pending` ⇒ falta el freeze, que es **gate humano**: avisar y parar.
- No ready ⇒ decir exactamente qué unidad espera y parar.

## 2. Armar el payload

Escribir `<investigations>/<UNIT_ID>-<slug>/payload.md` — **sin commitear**:
antes de lanzar se regenera a voluntad. Se concatena, sin editar contenido:

1. **Bloque de preflight** — `templates/preflight.md` de esta skill, resolviendo
   `{unit}`, `{runs}` y `{mode}`.
2. **El Bloque Común** del plan al que pertenece la unidad (la Parte II del
   documento que declara su frontmatter `plan:`). Si el protocol no lo declara,
   **preguntá al humano cuál es** — no lo adivines.
3. El **`02-findings` vigente** de cada unidad en `needs`, en el orden
   declarado (vigente = mayor `.vN`, nunca la versión superada).
4. El `00-protocol.md` de la unidad.

**Jamás viajan:** la semilla o tesis del proyecto, la constitution completa,
reports o raws de otras unidades, ni material de unidades que no estén en
`needs`. El payload crece con cada `need`: por eso los `needs` son mínimos.

**Resolver `runs` y `mode`:** del frontmatter del protocol (`runs: N`,
`mode: independent | chained`); si no los declara, de `runs.default` y
`runs.default_mode` de `framework.config.yaml`. Las etiquetas son siempre
`run-01..run-NN`, en ambos modos. (`C1`/`C2` es vocabulario histórico del
corpus viejo: jamás se emite.)

## 3. Costura para el humano (instrucciones concretas)

- Chat nuevo, titulado `UNIT_ID — slug`, con el **modo Research activo**.
- Pegar el payload completo.
- La sesión ejecuta el preflight **antes** de investigar; si una precondición
  falla, se detiene hasta que el humano la resuelva.
- Entre corridas, la sesión invoca la skill `new-run` de claude.ai; para cerrar,
  `research-close` (las tres skills de claude.ai se instalan una vez por cuenta
  desde `claude-ai-skills/` del kit — ver su README).
- Los exports verbatim van a `raw/run-NN.md` de la unidad, vía
  `/inception-kit:ingest`.

## 4. Sellar (cuando el humano trae la URL del chat)

1. En el frontmatter del protocol: `session: <URL>`, `constitution: <versión
   vigente>`, `status: frozen → running`. **Solo esos campos** — el cuerpo del
   protocol es inmutable y el hook lo hace cumplir.
2. **Commitear el payload junto con el sello.** Desde ese commit el payload es
   **record**: la evidencia exacta de qué leyó la sesión. Se regenera libremente
   solo ANTES de lanzar, jamás después.
   Commit: `feat: launch UNIT_ID (payload sellado, constitution vX)`.

## 5. Después

Al volver los exports: `/inception-kit:close UNIT_ID`.
