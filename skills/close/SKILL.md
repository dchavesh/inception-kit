---
name: close
description: Cierre de una unidad de investigación — QA completo, extracción a la RTM, métricas y findings, hasta dejarla en done. Uso — /inception-kit:close UNIT_ID
---

# /inception-kit:close UNIT_ID

El QA gate y todo lo que sigue. **Determinismo en los scripts, juicio acá,
autoridad en el humano.** Nunca saltear un paso, nunca continuar tras un STOP
sin confirmación humana explícita.

## Precondiciones

1. `session` sellada en el protocol (URL del chat + `constitution:` +
   `status: frozen → running`). Si el humano no la trajo: pedirla y sellarla
   primero.
2. En la carpeta de la unidad: `raw/run-NN.md` (exports verbatim, uno por
   corrida declarada, aterrizados **directo** por `/inception-kit:ingest --unit
   … --run …` — el cierre no mueve nada) y los tres documentos de cierre de la
   sesión — report en plantilla, borrador de findings y bitácora — generados
   con la skill `research-close` de claude.ai. Si falta algo: pedirlo y parar.
3. **Contar los raws contra el contrato:** `runs: N` del protocol. Si faltan
   corridas, la desviación se anota por escrito en el protocol antes de seguir;
   jamás se completa investigando de más.
4. Sellar `status: running → qa`.

## Los 8 pasos, en orden

1. **Validación de formato** — `validate-report UNIT_ID` (sin `--lenient`; el
   modo lenient es del retro-parse de corpus artesanal, no de un cierre
   normal). No valida ⇒ se corrige **en origen** (pedirle a la sesión que
   re-emita) o el humano acepta la desviación por escrito. **Jamás maquillar un
   export.**
2. **Auditoría de afirmaciones** — `claim-audit-sample UNIT_ID` (muestra
   determinista + candidatos a eco). El juicio va acá: ¿la fuente existe y dice
   lo que se afirma? ¿la evidencia sostiene la madurez etiquetada? ¿hay fuentes
   del mismo origen contadas como independientes? **Fuente inexistente o
   afirmación sin soporte ⇒ STOP: gate humano.** Todo queda trazado en el
   registry de auditorías.
3. **Kill criteria** — ¿algún hallazgo dispara los kill criteria globales del
   plan o los propios de la unidad? **Cualquier disparo ⇒ STOP: gate humano.**
   Todo gate consumido —este, el de una fuente inexistente, el que sea— deja su
   fila en `registry/gates.md`: cuál, cuándo, qué se decidió y qué enmendó.
4. **Commit de records** — `raw/`, `01-report` y `03-sources`. Inmutables desde
   ese commit; el hook lo garantiza.
5. **Extracción a la RTM** — juzgar cada `<unit>-reqNN` de la sección 7
   (*Requirements table*) contra las filas existentes del registry y escribir
   el archivo de marks (`templates/marks.md` de esta skill tiene la
   gramática), luego
   `extract-registry UNIT_ID --marks <archivo>`. `contradicts` sin
   `supersedes:` ⇒ rechazo total: se declara o se registra distinto. Los
   conflictos entre unidades quedan anotados como `con-NN`, sin resolverse acá.
6. **Métricas** — `append-metrics UNIT_ID …` con las flags que declare
   `metrics.columns` de `framework.config.yaml`, y con valores **medidos** en
   los pasos 1–2. Nada estimado; lo no medido se declara con su token
   (`n/a`, `n/m`).
7. **Finalizar `02-findings.md`** sobre el borrador de la sesión: ≤2 páginas,
   5–10 hallazgos numerados, cada uno con
   `(<established|supported|plausible|speculative> · <high|medium|low> · fecha)`
   parseable por `derive-review-by` — el enum va en inglés y sin dialecto, la
   prosa en el idioma que declare `language`. Tablas-insumo solo referenciadas;
   huecos explícitos. Si hubo varias corridas, conservar la atribución por
   `run-NN`. Commit.
8. **Cerrar** — `status: qa → done`; correr `derive-status` y `doctor`;
   anunciar qué unidades quedaron ready y cuál es el próximo gate humano.

## Reglas

- Una contradicción **entre corridas** es un hallazgo, no un error a promediar:
  se reporta como conflicto con las dos versiones.
- Ninguna afirmación sube de madurez por conveniencia; lo vencido entra
  degradado o se refresca, jamás lavado.
- El cierre no investiga: consolida lo que la sesión trajo.
