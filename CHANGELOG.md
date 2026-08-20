# Changelog

Todas las versiones del `inception-kit`. Formato: [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/);
versionado: [SemVer](https://semver.org/lang/es/).

El kit se actualiza por **bump de versión**, jamás por cirugía repo por repo.
Al subir de versión, cada repo consumidor corre `kit-init` (runner de
migraciones) — principio #7, sintonía por migración.

## [0.4.1] — 2026-08-20

**El tooling se alinea a la spec v0.4 ratificada.** La v0.4 no exigió activación
—canonizó lo que el kit 0.4.0 ya implementaba—, pero su redacción dejó
enumerados, uno por uno, los desajustes entre la letra nueva y el tooling
existente: las **siete notas post-gate** de su acta y las adjudicaciones de
§14.7. Este pase las implementa y nada más. Cero decisiones de diseño, cero
cambios a `SPEC.md`.

### Changed

- **El censo del roster reconoce los archivos que exige el ecosistema**
  (`LICENSE`, `NOTICE`, `CITATION.cff`): §4.5 les declara fila desde la v0.4, así
  que dejan de salir como **fuera del roster**. La fila la define un **criterio**
  —lo pide el mundo donde el repo vive, no el framework, y no porta reglas
  adentro— y su lista es ilustrativa: el censo reconoce la convención, y una
  convención nueva (`SECURITY.md`, `CODEOWNERS`…) sigue saliendo fuera del roster
  para que la **adjudique el humano** en el gate de `/normalize`. Inventar el
  criterio en un script sería juicio automatizado, que es justamente lo que §4.5
  le prohíbe al chequeo.
- **Los documentos de plan son roster, no una canasta aparte.** Con la fila de
  §4.5 (Δ18) desaparece la constancia de "cola de enmiendas": el censo los
  reporta como lo que son, **records** apuntados por el `plan:` de un protocol.
- **`normalize retire` se planta ante un plan y ante un archivo del ecosistema.**
  Consecuencia mecánica de las dos filas nuevas: un plan es record y se supersede
  con un plan nuevo; un archivo del ecosistema tiene su dueño **fuera del
  framework** y el ciclo de vida de borrado no lo alcanza.
- **El gate de adjudicación de vigentes tiene nombre en el kit:
  `current-adjudication`.** §11.1 le declara la fila pero no fija tokens de gate
  —los nombres son un playbook por flujo, no un enum cerrado—, así que el nombre
  lo pone el kit (adjudicado en §14.7). `/normalize` paso 4 lo escribía bajo
  `map-ratification`, que es el nombre de **otro** gate. Las filas ya escritas no
  se reescriben: el registry es append-only y se leen por su decisión (§13.2).
- **`/adopt` deja la fila de su gate.** El paso 7 hacía la adjudicación con el
  humano y escribía las supersesiones, pero no la fila que §7.4 exige de todo
  gate consumido. Ahora la escribe — y si el corpus no trae versiones
  conviviendo, el gate no se disparó y **no se inventa** la fila.
- **`kit_version`, README y CHANGELOG referencian la spec v0.4** (`ratified`,
  2026-08-20).

### Removed

- **Las constancias de "encolado para el batch v0.4".** `/adopt` anotaba que la
  fila de `retro-lenient-deviations.md` estaba encolada y `/distill` que la casa
  del silver fuera de una unidad no estaba declarada. Ambas cosas están hoy en la
  letra (Δ15 y Δ16): la constancia dejó de ser cierta, y una línea que enseña
  algo falso se retira, no se envejece.

## [0.4.0] — 2026-08-20

**Los flujos de entrada y la destilación.** El framework deja de tener una sola
puerta: `/inception` para un proyecto nuevo, `/adopt` para un corpus artesanal
que ya existe, `/normalize` para un repo con documentación — **y no hay más
entradas**. Con `/distill`, el bronze que no es una corrida de investigación
llega hasta el conocimiento por el mismo carril de procedencia que todo lo demás.

Un edge case no se le agrega al framework: se **normaliza** hacia él (principio
de diseño #1). Estos cuatro flujos son esas pipelines de normalización.

### Added

- **`/inception-kit:inception`** — de una idea cruda a un programa listo para
  congelar (spec §10.2). Entrevista de elicitación **idea-agnóstica** (la skill
  no porta ninguna idea de proyecto: pregunta, no propone), `language`
  confirmado **antes del primer artefacto** —cambiarlo después es migración,
  §1.8—, repo sembrado, **constitution neutral** en borrador para el gate humano
  y protocols **R0** en `pending`. Las R0 son las que deciden si el programa va,
  pivotea o se descarta, y nacen `clean-room`: son exploración y son sensibles a
  falsificación. El freeze sigue siendo orden humana.
  - `skills/inception/templates/constitution.md` — supuestos refutables,
    dominio, techo de gasto, umbrales de QA, disparadores y jerarquía de
    independencia, con changelog de enmiendas vacío. **Los horizontes NO se
    escriben ahí:** la constitution apunta al bloque ratificado de la config
    (§12 G4), y ratificarla ratifica esos valores tal como están.
- **`/inception-kit:adopt`** — retro-parse de un corpus artesanal sin repo:
  protocols **retroactivos** que describen la comisión que la corrida
  efectivamente tuvo (`runs:` es cuántas hubo; los kill criteria que no
  existieron se declaran vacíos), jerarquía de independencia **declarada** —el
  pecado no es el contexto, es el contexto no declarado— y **cierre
  retro-lenient ANOTADO**, que es el único lugar donde vive `--lenient`.
  - La desviación se anota en `<unit>/retro-lenient-deviations.md` con la salida
    literal del validador, su fila de gate y la anotación de sidecar. **Lo
    lenient no lava nada:** sin fuente, la afirmación sigue siendo `speculative`.
  - **Costura declarada — `/adopt` NO agrega un escritor del ingest-log.** El
    ingest-log registra *llegadas*; el verbatim que llega de afuera pasa por
    `ingest` y su fila nace ahí por construcción, y el material que ya vivía en
    el repo no tuvo llegada — llenar esas columnas sería inventar una ingesta
    que no ocurrió. La procedencia del corpus adoptado queda en tres casas que
    ya existen: ingest-log, registry de migraciones y sidecar.
- **`/inception-kit:normalize` + `normalize`** — el repo existente, llevado al
  formato vigente. `normalize inventory` es read-only y censa **roster §4.5**,
  **prueba del puntero delgado**, documentos a clasificar, **monolitos**,
  **épocas como carpetas**, **familias de versión sin vigente**, **huérfanos** e
  higiene operativa (que se nombra y no se toca). Exit 1 cuando hay algo que
  adjudicar.
  - **Acá vive el enforcement que `doctor` deliberadamente no hace.** El censo
    de la raíz y de `<research>/` necesita juicio y un humano mirando; `doctor`
    corre en cada push y censa solo el registry. La taxonomía de §4.5 es
    **cerrada** (con `SPEC.md` y `AGENTS.md` nombrados uno por uno), y la prueba
    del puntero delgado se **mide**: una línea de `README`/`CLAUDE`/`INDEX` que
    también vive en la constitution o en la config es una segunda casa.
  - **Triturado de monolitos** como paso nombrado: lo vigente sale como datos y
    records individuales; el original queda **congelado en su lugar**
    (`normalize freeze --apply`, vía `records.extra_immutable_paths`) — sale del
    contexto de lectura sin perder un byte.
  - **Borrado con plan primero.** `normalize retire --reason «…» --apply` exige
    **retención declarada**, y se planta antes de proponer un record, un archivo
    del roster o **documentación dura** — la única clase exenta del ciclo de
    vida de borrado de cualquier flujo (§2.3). Sin `--apply` imprime el
    inventario y para.
  - **La adjudicación de vigentes es gate humano siempre:** ante tres
    arquitecturas simultáneas, ningún mecanismo elige solo.
- **`/inception-kit:distill` + `distill`** — bronze no investigativo →
  **silver re-derivable** → **borrador de gold**. El silver es el `01-report` de
  su unidad y se valida contra la plantilla de siempre (un contrato, un lugar);
  lo que este flujo agrega es la **gramática de locators** por clase (página ·
  `mm:ss` · ID de respuesta · encuadre) y el techo de madurez: una sola fuente
  no da `established`, y sin `<unit>-srcNN` la afirmación es `speculative`.
  - `distill BRONZE --unit U --silver RUTA --apply` **re-verifica el `sha256`
    contra el sidecar antes de declarar nada** —si el bronze cambió, se planta—
    y sella la destilación como anotación **append-only** del sidecar.
  - **La destilación la aloja una unidad, siempre**: el gold es un
    `02-findings`, y vive en la carpeta de su unidad. Un bronze de
    `evidence/<class>/` **se queda donde está** y la unidad lo cita.
- **`check-recurrence` gana su tercera capa: la carga sin destilar** (§2.4).
  Material cargado sin destilación declarada es **deuda** y ahora aparece como
  pendiente, con la propuesta concreta que la salda. Se sumó al comando que ya
  hacía exactamente eso —listar lo pendiente y nombrar quién lo atiende— en vez
  de abrir un segundo mecanismo.
- **`kitlib.records`** — el backstop por rutas en una sola casa. La guarda de
  inmutabilidad y `normalize` leen la misma lista: un flujo que no puede
  proponer el borrado de un record necesita saber exactamente lo mismo que la
  guarda usa para rechazarlo.
- **`kitlib.passes`** — la mecánica común de los pases que escriben (git, índice
  limpio, `--apply`, rastro en el registry de migraciones), compartida por
  `migrate` y `normalize`.

### Changed

- **La guarda aplica la regla pre-gate de §4.3 a la constitution del proyecto.**
  El protocolo duro de enmienda gobierna un documento **en vigor**: mientras su
  `status:` es `draft`/`proposed`, la constitution es todavía la propuesta que
  el gate va a ratificar, y editarla —incluido **ratificarla**— entra a esa
  misma versión sin bumpearla, porque no hay nada vigente que superar. Lo mismo
  vale para el bloque ratificado de la config: pre-gate, esos valores se
  ratifican **con** la constitution. Sin esto, `/inception` no podía cerrar su
  primer gate sin inventar una v2 que nunca existió. Falla del lado seguro: una
  constitution sin `status:` declarado se trata como vigente.

## [0.3.0] — 2026-08-19

**Integridad profunda.** Los registries dejan de ser markdown y pasan a ser
**datos con schema**; nace el **índice puerta-de-entrada** que §1.2 y §4.5 ya
daban por supuesto; `/migrate` materializa la migración por capas de §9 más allá
del runner de versiones; y un chequeo de recurrencia vigila las dos capas de
frescura de §6 — proponiendo, jamás ejecutando.

### Changed — BREAKING

- **Los nueve registries son DATOS y su `.md` es una vista generada.** El
  registry vive en `<registry>/data/<name>.jsonl` — **JSON Lines**, un objeto
  por línea — y el `.md` se renderiza desde ahí. Se eligió JSONL por
  simplicidad: append-only es literalmente *agregar una línea*, verificable con
  una comparación de prefijo byte a byte sin parser y sin ambigüedad de
  indentación, y `json` es stdlib (la guarda sigue corriendo con git + Python
  estándar, spec §4.4). **La spec norma el régimen, no el formato** (§12 G6 y
  Preguntas al final #2): los tres regímenes no cambian, ahora se hacen cumplir
  sobre los datos.
  - **append-only** (metrics, ingest-log, supersessions, migrations, qa-audits,
    gates): el contenido previo no se pisa.
  - **markable** (requirements, conflicts): la fila no se borra y solo mutan
    los campos declarados `markable` — el ID y lo que la fila afirmó, jamás.
  - **derived view** (`STATUS.md`): sin datos propios; deriva de los protocols.
- **Nadie edita un registry a mano.** El comando **`registry`** es la única
  puerta: `add` (append-only), `mark` (marcable), `render` (vistas), `show`,
  `schema`. `extract-registry`, `append-metrics` e `ingest` escriben por ahí.
- **La guarda verifica los tres regímenes sobre los datos** y rechaza además
  editar a mano la **vista** de un registry: tiene que ser exactamente la
  regeneración de sus datos.
- **`STATUS.md` cambia de forma**: columnas en inglés (`Unit`, `Status`,
  `Needs`, `Ready`, `Note` — §1.8: las columnas siempre) y prosa en el idioma
  que declare `language`. Es vista derivada: se regenera, no se migra.

### Added

- **`INDEX.md` — el índice puerta-de-entrada** (spec §1.2, §4.5), vista raíz
  generada por `derive-index`. En una página: tablero con el objetivo de cada
  unidad en una línea, **ADRs vigentes** (superado se marca, no se borra),
  **conflictos abiertos**, **síntesis vigente** (la última fila del gate de
  síntesis) y **dónde vive cada clase de cosa**, derivado de `paths`. Ninguna
  regla vive ahí: si se borra, solo se pierde el atajo. `doctor` lo verifica
  contra su regeneración.
- **`/inception-kit:migrate` + `migrate`** — la migración por capas de spec §9,
  entera. `plan` diagnostica sin escribir; `derived --apply` regenera tablero,
  vistas e índice; `relabel UNIT --pass vocab|runs --apply` hace la
  **supersesión mecánica** de un record de lectura; `relocate SRC --class C
  --apply` reubica bronze legado. **Todo pase que escribe exige `--apply`**, y
  el `--apply` se pide con el diff a la vista (§9.1).
  - **El round-trip es la evidencia:** cada sustitución se registra con su
    posición y el original se reconstruye byte a byte desde el texto nuevo. Si
    no vuelve, el pase se aborta. El pase `vocab` toca etiquetas **solo dentro
    de una anotación** — `alta` o `media` en prosa quedan intactas.
  - **Nunca hay supersesiones vacías:** un record ya canónico no se supersede
    «por consistencia».
  - **Reubicar no es reescribir:** `relocate` mueve, verifica que el `sha256`
    sea el mismo antes y después, y escribe el sidecar de procedencia. La
    guarda acepta el rename **solo** con blob idéntico, destino en casa
    protegida y la entrada de migraciones en el MISMO commit.
  - **Rastro doble, siempre** (§9.2): entrada en el registry de migraciones +
    anotación en el sidecar del record afectado. Un record sin sidecar recibe
    uno; el sidecar pasa a ser **append-only** — la incisión va ahí y jamás
    dentro del verbatim.
- **`check-recurrence`** — las dos capas de frescura de spec §6 en un comando:
  `review_by` vencidos y cadencias `refresh:` cumplidas, con los relanzamientos
  y la re-síntesis que **propone**. No escribe un solo archivo y no ejecuta
  nada: los gates son humanos. Exit 1 cuando hay algo que proponer.
  `templates/ci/recurrence.yml` lo corre periódicamente — **opcional**, no lo
  instala `kit-init`.
- **`refresh:` en el contrato del protocol** (spec §6.2): cadencia `<N><w|m|y>`,
  validada al cargar la unidad. Se declara la cadencia, jamás la fecha.
- **Schema validado por `doctor`**: cada fila contra los campos declarados
  (obligatorios, tipos, fechas ISO, enums, IDs únicos), el set cerrado de
  archivos de datos, y cada vista contra su regeneración.
- **Migración `0.2 → 0.3`** en el runner de `kit-init`: convierte cada tabla
  markdown a datos fila por fila —sin reinterpretar nada— y deja el `.md` como
  vista. Lo único que traduce es el dialecto que el propio kit escribió
  (`Status` de conflicto `abierto` → `open`, porque los valores de enum van en
  inglés), y la traducción queda declarada en el rastro. Idempotente.

### Fixed

- `derive-review-by` y el índice comparten el cálculo de frescura con
  `check-recurrence` (`kitlib/freshness.py`): un contrato, un lugar.
- `kit-init` corre las migraciones **antes** de sembrar (un repo viejo trae sus
  registries en formato anterior) y regenera los derivados **al final**, ya con
  `kit_version` sellada — antes el índice nacía desactualizado.

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
