---
id: inception-framework-spec
type: constitution
version: 0.3
status: ratified — 2026-08-19 (gate humano: Sección A confirmada, Sección B aprobada completa)
date: 2026-08-19
supersedes: inception-framework-v0.2
home: inception-kit (este repo)
consumer: toda sesión, humano o script que opere bajo el inception-framework
reading-moment: antes de crear, cerrar o migrar cualquier artefacto del framework
---

# Inception Framework — spec v0.3

**Propósito.** Convertir una idea cruda en una base de desarrollo respaldada por
evidencia: un programa de investigación ejecutado por sesiones de IA, coordinado
sobre un repo de archivos, cerrado por una síntesis que siembra arquitectura y
decisiones. El framework cubre la fase *anterior* al desarrollo dirigido por
especificación y le entrega el relevo.

**El norte.** Tres funciones, y toda regla de esta spec se juzga contra ellas:
**coordinación** (planificar y gobernar la entrada de material nuevo, con gates
humanos y procedencia desde el minuto 1) · **organización** (una casa lógica por
cosa) · **extracción** (destilar lo importante para que agente y humano lean
rápido y sin ruido).

**Principio de diseño.** Determinismo en los scripts. Juicio en los prompts.
Autoridad en los gates humanos.

## Cómo se lee y cómo se enmienda este documento

Esta spec es un documento **clase constitution** (§4.3): es evergreen — se
edita para seguir siendo verdadera — pero **jamás en silencio**. Toda enmienda
sube `version:` y agrega su fila al changelog (§14), y la ratifica el humano.
No hay corrección tipográfica exenta: si el texto normativo cambia, la versión
cambia.

**Enmienda antes del gate.** Ese protocolo duro gobierna una spec **en vigor**.
Mientras el `status:` es `proposed`, el documento todavía es la propuesta que el
acta somete a ratificación: una enmienda ratificada en conversación **antes** del
gate entra a esta misma versión — no la bifurca ni la bumpea, porque no hay nada
vigente que superar. A cambio, no entra en silencio: se redacta en su sección, se
registra en la tabla de enmiendas pre-gate (§14.3) y se agrega como ítem con
alternativa descartada al acta (Sección B.4). Ratificado el acta, la versión
queda congelada y todo cambio posterior vuelve al protocolo duro.

**Qué es v0.3.** Esta versión supersede a la v0.2 y la reemplaza como
constitution vigente: es autocontenida, y ningún lector necesita la v0.2 para
operar. Se construyó bajo una regla dura de alcance: **v0.3 = v0.2 arrastrada
sin cambio + los 10 ítems de la Fase 2 del plan de mejoras vigente + las
enmiendas pre-gate ratificadas el 2026-08-19 (§14.3)**. Todo párrafo normativo de
este documento traza a uno de los tres orígenes; las tablas de trazabilidad de
§14 lo hacen auditable. Nada nació por iniciativa del redactor.

**Estado.** `proposed`. Esta spec **no está en vigor** hasta que el humano
ratifique el ACTA DE GATE del final. Las reglas que exigen migración de tooling
declaran además su **regla de activación** (§1.6, §9.4): la spec declara, el kit
implementa después.

---

## 0. Principios

Dos listas gobiernan cosas distintas y por eso llevan nombres distintos
(§1.1): los **principios de diseño** rigen cómo se construye el framework; los
**principios de operación** rigen cómo se trabaja bajo él.

### 0.1 Principios de diseño (ratificados en el plan de mejoras)

1. **Simplicidad.** Flujos claros y no redundantes, un mecanismo por problema,
   naming entendible, formatos simples. Los edge cases se adaptan al framework,
   jamás al revés; se tratan como **pipelines de normalización**. Simple ≠
   incapaz de lo complejo: si no puede con un escenario grande, se
   sobre-simplificó.
2. **Skills sin lógica de negocio.** Ninguna skill porta ideas de proyecto: solo
   preguntas y pasos indiferentes a cualquier idea. Lo que no esté claro se
   ratifica con el humano mediante preguntas generadoras — nunca se asume.
3. **Procesos endurecidos, investigación libre.** Los pasos mecánicos llevan
   gates que se detienen ante error humano o precondición incumplida. La
   investigación no se encorseta: se le da forma, no se le mata la creatividad.
4. **Un contrato, un lugar, varios lectores.** Cada regla vive en una única
   fuente y se renderiza a quienes la leen; jamás en comentarios ni texto
   duplicado.
5. **Colocación por unidad.** Todo lo que pertenece a una unidad vive en su
   carpeta. Sin carpetas genéricas top-level confundibles entre proyectos.
6. **Nomenclatura en inglés.** Todo nombre de skill, comando, campo de contrato,
   operación, etiqueta y **valor de enum** va en inglés — kit, consumidores y
   claude.ai. La prosa del corpus sigue siendo la del proyecto: **el idioma de
   prosa es un parámetro declarado** (`language`, §1.8), y las skills son una
   sola versión que escribe en él — jamás copias traducidas. Un solo idioma para
   los nombres, cero híbridos.
7. **Sintonía por migración.** Cuando el framework mejora, un proyecto puede y
   debería migrar TODO a la versión vigente. La migración es **por capas** y
   jamás falsifica evidencia (§9).

### 0.2 Principios de operación

1. **Una sola fuente por hecho.** Se declara solo lo que no se deriva de algo ya
   declarado. Las vistas derivadas (tablero de status, `review_by`) son cachés
   regenerables: jamás se editan a mano, jamás son autoritativas.
2. **Records vs evergreen.** Todo documento pertenece a exactamente un régimen
   (§4). Los *records* se escriben una vez y no se editan; las correcciones se
   agregan como enmiendas. Los *evergreen* describen estado actual y se editan
   para seguir siendo verdaderos. **La supersesión es una operación, no una
   convención:** un record que contradice a otro existente se rechaza al cierre
   salvo que declare `supersedes:`; la entrada superada se marca, nunca se
   borra; una enmienda propaga marca de invalidación a toda fila del registry
   que cite el record enmendado.
3. **Cadena de evidencia — solo hacia arriba.**
   `source → raw → report claim → finding → requirement → ADR → architecture →
   spec → code`. Un artefacto solo puede citar capas por debajo de sí mismo.
   **Toda afirmación de un report lleva su ID de fuente (`<unit>-srcNN`); una
   afirmación sin fuente es, por definición, `speculative`.** Las decisiones
   (ADRs, salidas de síntesis) se citan *como decisiones*, jamás como evidencia.
   Así los bucles de eco de modelo son estructuralmente imposibles, no
   meramente desaconsejados.
4. **La madurez no se lava — y se mueve solo por regla.** Toda afirmación lleva
   etiqueta de madurez y de volatilidad, fechada (§1.6). Ningún artefacto
   derivado puede subir la etiqueta de aquello de lo que deriva. La madurez
   **sube** por triangulación (≥2 fuentes independientes A/B) o replicación
   entre runs; **baja** por fuente única, evidencia solo de parte interesada,
   evidencia indirecta, inconsistencia entre fuentes o vencimiento.
5. **El conocimiento vence.** `review_by` se deriva, jamás se almacena (§6).
   Un hallazgo vencido sin re-verificar **baja un nivel de madurez
   automáticamente**: el no-lavado aplicado al tiempo.
6. **Aislamiento por diseño.** Las unidades corren en sesiones separadas y no
   comparten nada salvo los findings de sus `needs` declarados. La
   independencia entre unidades concurrentes la garantiza el grafo de
   dependencias, no un chequeo en tiempo de ejecución (§3, §8).
7. **Divulgación progresiva.** El consumidor baja solo hasta donde su tarea
   exige: findings (≤2 páginas) → report → raw → fuente externa. Cada nivel es
   autocontenido para su propósito.
8. **Contrato de estilo (anti-slop).** Densidad sobre extensión; sin preámbulos,
   relleno ni cortesías de cierre; sin prosa que repita lo que ya dice un dato;
   prosa solo donde vive el juicio; los datos como datos (frontmatter, tablas);
   la especulación siempre etiquetada. **Ningún artefacto nuevo sin consumidor y
   momento de lectura declarados** (§4.4).

---

## 1. Nomenclatura

*Origen: Fase 2 ítem 1.* Un nombre por concepto, en inglés, con glosario llano
(§13). El síntoma que esta sección cierra es real y está documentado: "constitution"
llegó a nombrar dos cosas distintas en dos proyectos, lo que obligó a inventar
el "Bloque Común" a mitad de vuelo.

### 1.1 Un nombre por concepto

| Concepto | Nombre canónico | Casa |
|---|---|---|
| Reglas de gobernanza del repo (supuestos, dominio, techo de gasto, umbrales, disparadores) | **constitution** | `<research>/constitution.md` |
| Bloque común que viaja en todo payload de un programa (rúbricas, marcado, reglas de investigación) | **briefing** | Parte II del documento de **plan** que comisiona las unidades (§12, G1) |
| La comisión de una unidad (objetivo, `needs`, fuera de alcance, kill criteria) | **protocol** | `<unit>/00-protocol.md` |
| El sobre exacto que recibió una sesión | **payload** | `<unit>/payload.md` (record al sellar) |
| Export verbatim de una corrida | **raw** | `<unit>/raw/run-NN.md` |
| Informe completo validado contra plantilla | **report** | `<unit>/01-report.md` |
| Resumen ≤2 páginas — el único artefacto que viaja entre unidades | **findings** | `<unit>/02-findings.md` |
| Bitácora de búsqueda | **sources** | `<unit>/03-sources.md` |
| Tabla maestra de requisitos | **RTM** (`requirements`) | `<registry>/requirements.md` |
| Una corrida de investigación dentro de una sesión | **run** (`run-01`…) | etiqueta |

**Los prefijos numéricos de archivo codifican orden de lectura dentro de la
carpeta, jamás orden de ejecución del programa** — el orden de ejecución es el
grafo `needs`. Los nombres internos son fijos: el `02-findings.md` de cualquier
unidad es siempre la misma clase de cosa.

**Nombres de archivo y de ID:** ASCII kebab-case, sin tildes ni espacios.

**El contrato viaja en el payload, jamás en una skill.** Ninguna skill
auto-activada porta contrato: las skills son mecánica de proceso (ritual de
arranque, límite entre runs, formato de cierre). Qué investigar, cuántos runs y
en qué modo sale del payload (principio de diseño #2).

### 1.2 Gramática de IDs — llave estable, jamás semántica

El ID es **llave inmutable y "tonta"**: `<prefijo><NN>[letra]` más un slug. El
significado vive en el slug y en el índice, jamás dentro del ID.

Los **smart codes** (codificar categoría o función dentro del ID) se
**rechazan**: el significado embebido se pudre — la unidad que nace "de mercado"
termina cubriendo legal, y como los IDs jamás se renombran, un ID semántico
mentiría para siempre.

La experiencia de "saber de qué se trata sin abrir el documento" la dan dos
mecanismos, no el ID:

- el **índice puerta-de-entrada** generado: `id → slug → objetivo en una línea →
  status`;
- la **regla de prosa**: la primera mención de una unidad en un documento se
  escribe `rNN (slug-corto)`; de ahí en adelante, `rNN` a secas.

**IDs permanentes.** Nada se renumera ni se reutiliza jamás — ni siquiera
cuando el record que los introdujo queda superado (§7.2).

### 1.3 Prefijos: set cerrado por clase de unidad

Los prefijos son un **set cerrado declarado en `framework.config.yaml`**
(`ids.classes`), una sola letra minúscula cada uno. El kit trae dos: `r` (desk
research) y `f` (field work). Agregar una clase es decisión del proyecto, entra
por config y **exige su entrada de glosario**.

**Convención de fase:** `X00` más sufijo alfabético (`r00a`, `r00b`, …) son
unidades preliminares o de inception de la clase X — las que deciden si el
programa va, pivotea o se descarta. `X01+` es el programa.

### 1.4 Ancho y orden

- `ids.width` (default 2) es el ancho **MÍNIMO** de la parte numérica.
- Al desbordar, **el ancho crece** (`r99` → `r100`) y **nada se renumera**. No
  hay tope.
- El orden es **SIEMPRE numérico**, jamás lexicográfico, en todo tooling y toda
  vista: `r2 < r9 < r10 < r100`.
- El hexadecimal se rechaza: viola "claro y sencillo".
- **Un solo `ids.width` gobierna IDs de unidad, sub-IDs y IDs de registry**
  (§12, G5).

### 1.5 Sub-IDs y gramática de conflictos

Un solo esquema de namespacing por unidad:

| Cosa | ID | Ámbito |
|---|---|---|
| Unidad | `rNN` | repo |
| Fuente | `<unit>-srcNN` | unidad |
| Requisito | `<unit>-reqNN` | unidad |
| Contradicción local de la unidad | `<unit>-conNN` | unidad |
| Contradicción del registry central | `con-NN` | repo |
| Decisión | `adr-NNNN` | repo |

**Conflictos.** Una contradicción detectada dentro de una unidad (entre fuentes
o entre runs) es `<unit>-conNN`. Una contradicción **load-bearing** — la que
cruza unidades o condiciona una decisión — sube al registry central como
`con-NN`, con la fila que enlaza su origen. Los tres vocabularios históricos
(`CONTRA-NN`, `CONTRA-rNN-NN`, `K1..K7`) quedan como vocabulario histórico con
entrada de glosario (§13.2): se leen, jamás se emiten.

**`adr-NNNN` conserva su ancho de 4 dígitos** por convención MADR externa al
framework; es la única excepción documentada a `ids.width`.

### 1.6 Enum de madurez y volatilidad — UNA forma, en inglés

Toda afirmación, hallazgo y fila de evidencia lleva, fechada, una etiqueta de
cada enum. **Los valores son estos y no admiten dialecto:**

| Enum | Valores |
|---|---|
| **maturity** | `established` · `supported` · `plausible` · `speculative` |
| **volatility** | `high` · `medium` · `low` |

`speculative` es la única madurez que puede ir sin ID de fuente — porque una
afirmación sin fuente es speculative por definición (principio de operación #3).

**El enum no es configurable.** Es contrato de esta spec, no perilla por
proyecto: vive en el kit y **jamás** en `framework.config.yaml` (principio de
diseño #4). Un proyecto que necesite otro enum no necesita otro enum: necesita
otro framework.

**El payload pinnea el enum exacto.** Las sesiones no inventan dialectos ni
etiquetas locales; toda etiqueta que emiten sale del payload que recibieron.

#### Regla de activación (el enum inglés entra con el kit 0.2.0)

El enum inglés quedó **ratificado el 2026-08-18**, pero el tooling 0.1.x parsea
el enum español. Esta spec **declara** el enum; **no lo implementa**. Entra en
vigor con el **kit 0.2.0**, que migra en un solo bump y de forma indivisible:

1. los **parsers** (`kitlib/vocab.py` y sus lectores: `doctor`,
   `validate-report`, `derive-review-by`);
2. las **plantillas** (plantilla de report de `research-close`, plantillas de
   protocol y de preflight);
3. las **claves de `horizons`** de `framework.config.yaml`
   (`alta/media/baja` → `high/medium/low`), que son valores del enum de
   volatilidad y por eso migran con él;
4. el **corpus nuevo**; el corpus histórico NO se reescribe — se lee con
   glosario (§13.2) y se migra, si se migra, por las reglas de §9.

**Migran juntos o no migra ninguno.** Que el tooling 0.1.x hable español no es
una violación de esta spec: es la transición declarada. Un repo a medias sí lo
es.

### 1.7 La prueba del lector frío

Un nombre pasa si **alguien sin contexto puede decir qué es el archivo leyendo
solo su nombre**. La prueba se aplica al nombrar cualquier archivo, campo o
etiqueta nuevos, y es un chequeo explícito de los flujos de planificación y de
normalización. Un nombre que no pasa se cambia antes de existir; si ya existe y
no pasa, el cambio entra por migración (§9), no por edición silenciosa.

### 1.8 Idioma de prosa — un parámetro, no una bifurcación

*Origen: enmienda pre-gate E3 (§14.3).* El principio de diseño #6 fija el idioma
de los **nombres**; esta sección fija el de la **prosa**, y hace explícito lo que
ya venía implícito ("la prosa del corpus sigue siendo la del proyecto").

```yaml
language: en        # código ISO 639-1
```

**La frontera es dura:**

| Siempre en inglés, sin excepción | Se escribe en `language` |
|---|---|
| nombres de skill y de comando · campos de contrato y claves de config · valores de enum · etiquetas y marks · columnas de tabla · IDs y nombres de archivo | el cuerpo de protocols, reports, findings, sources y payloads · la constitution del proyecto y sus ADRs · la prosa de los registries · lo que las skills le dicen al humano |

**Las skills tienen UNA sola versión.** Nombres y mecánica en inglés; la skill lee
`language` y escribe su prosa en ese idioma. **Jamás existen copias traducidas**
de una skill, una plantilla o un documento del kit: una copia por idioma es una
segunda casa que deriva al primer cambio (principio de diseño #4). Lo mismo vale
para el corpus — un repo tiene **un** idioma de prosa, no dos versiones del mismo
documento.

**Cambiar `language` es migración, no edición.** La clave es config operativa
—no porta autoridad epistémica, así que no entra al bloque ratificado (§12,
G4)—, pero cambiarla después del primer artefacto arrastra el mismo trabajo que
mover una ruta: evergreen se actualiza, los derivados se regeneran, y los
records **no se reescriben** (§9.1) — el corpus histórico se lee en el idioma en
que se escribió, como cualquier otro legado.

**Los renderizados para terceros son vistas derivadas.** Un PDF, un deck o un
one-pager —traducido o no— se genera desde el artefacto vigente y **vive fuera
del KB**: no es un documento del repo, no es citable como fuente, y no crea una
segunda casa de nada (principio de operación #1).

**El kit habla el idioma del kit.** `language` gobierna la prosa que las skills
**escriben en el repo consumidor**; los artefactos propios del kit —esta spec,
los `SKILL.md`, los comentarios de la config ancla— son documentos del kit y se
redactan en el idioma del kit, con sus nombres en inglés como manda el principio
#6.

#### Regla de activación

La spec **declara** el parámetro; el **kit 0.2.0** lo implementa (clave en la
config ancla, skills que la leen al redactar), junto con el resto de su bump
(§9.4). El kit trae **`en`** como valor de arranque y el flujo de creación de
repo lo confirma con el humano: un repo cuyo equipo escribe en otro idioma lo
declara ahí, una sola vez.

---

## 2. Clases de fuente de evidencia

*Origen: Fase 2 ítem 2.* La unidad deja de estar acoplada a "sesión de
investigación que produce markdown": el framework ingiere entrevistas,
formularios, dictámenes en PDF y medios con la misma disciplina de procedencia.

### 2.1 Las seis clases

| Clase | Qué es | Bronze (verbatim) |
|---|---|---|
| `research-run` | corrida de investigación de una sesión | export verbatim del chat |
| `field-interview` | entrevista o gestión de campo | audio/video/transcripción cruda |
| `form-batch` | tanda de respuestas de formulario | export crudo de la tanda |
| `document-drop` | documento recibido (dictamen, informe, contrato de terceros) | archivo original |
| `media` | foto, captura, plano, grabación | archivo original |
| `hard-doc` | **documentación dura** — documentos oficiales, licencias, contratos y archivos clave del proyecto | archivo original, que **jamás se borra** |

### 2.2 Propiedad medallion

Las cinco primeras clases comparten la misma propiedad de tres capas:

- **bronze** — el original intacto, su `sha256` y su **sidecar de procedencia**
  (`<archivo>.meta.yaml`: origen, fecha, método, licencia y consentimiento
  cuando aplique). El bronze **jamás se edita ni se reescribe**.
- **silver** — transcripción o extracción **re-derivable** desde el bronze.
- **gold** — findings.

**Propiedad medallion:** si cambia la plantilla del report, silver y gold se
re-derivan desde bronze **sin re-ejecutar investigación**.

**Consentimiento y datos personales viven en el sidecar desde el diseño**, no
en la prosa: la legislación de datos personales aplica al propio repo.

### 2.3 Documentación dura (`hard-doc`)

- **Jamás se borra.** Es la única clase exenta del ciclo de vida de borrado de
  cualquier flujo (incluida la normalización de repos existentes).
- Vive en **su casa especial**: la ruta que declara `paths.hard_docs` (§5) o
  **fuera del repo** (Drive, SharePoint) cuando su tamaño o su licencia lo
  exijan.
- Cuando vive fuera, el repo retiene **puntero + `sha256` + sidecar**, y la fila
  que los registra vive en el **ingest-log** (adjudicado en el gate de
  ratificación, 2026-08-19: ya la escribía de facto vía `--keep`, tiene las
  columnas de origen/hash/destino, y no se crea un registry nuevo para una sola
  clase de fila): la ausencia del binario nunca es ausencia de procedencia.
- Se identifica **al ingerir**, no después: es uno de los tres destinos
  obligatorios de la ingesta (§2.6). La ingesta conserva el original (`--keep`)
  en lugar de borrarlo.
- No tiene obligación de silver ni de gold: es fuente de record. Toda afirmación
  derivada de ella recorre la cadena de evidencia normal.

### 2.4 Destilación declarada

**Toda clase declara su flujo de destilación bronze→silver→gold.** Material
cargado sin destilación declarada es **deuda**: entra al repo, queda registrado
y aparece como pendiente. No se prohíbe cargar sin destilar — se prohíbe
olvidarlo.

### 2.5 Rúbrica de calidad de fuente (A–D)

Es la columna `Quality` de toda tabla de fuentes:

| Grado | Qué es |
|---|---|
| **A** | primaria — artículos con revisión por pares, datos medidos, post-mortems de incidentes, documentación técnica normativa |
| **B** | secundaria independiente — evaluaciones de terceros, replicaciones, periodismo técnico con fuentes |
| **C** | parte interesada — afirmaciones de proveedor, marketing, anécdotas sueltas |
| **D** | agregación sin fuente — listículos SEO, resúmenes sin crédito |

**Regla cruzada:** una fuente más vieja que el horizonte de su volatilidad baja
un grado. **Regla de eco:** las fuentes que repiten un mismo origen cuentan como
una sola.

### 2.6 Ingesta clasificada en la puerta

*Origen: enmienda pre-gate E1 (§14.3). Generaliza la resolución de G3 (§12) a
toda llegada, y elimina el `inbox/`.*

**El único staging es externo al repo.** El material espera afuera — la carpeta
de descargas del humano, el adjunto sin abrir, el export recién bajado — y el
repo no tiene bandeja de entrada. **`inbox/` deja de existir**: no es una ruta
del contrato, no es una casa, y ningún flujo escribe ahí.

**Por qué no hay bandeja.** Toda llegada es atendida: no hay material que deba
"esperar turno" dentro del repo. Una bandeja es una casa sin dueño, y una casa
sin dueño reproduce exactamente el tramo huérfano que G3 reportó — algo entra,
nadie sabe quién lo mueve, y el material se sedimenta sin clase ni destino.

**La clasificación ocurre al ingerir**, no después. Toda ingesta declara
**destino obligatorio**, y hay exactamente tres:

| Destino | Cuándo aplica | Dónde aterriza |
|---|---|---|
| **unidad** | el material pertenece a una unidad (el verbatim de un run, un binario recogido por esa unidad) | `<unit>/raw/` — `run-NN.md` para el verbatim de un run (§12, G3); cualquier otro bronze, con su sidecar al lado (§2.2) |
| **clase sin unidad** | el material tiene clase de fuente (§2.1) pero no pertenece a ninguna unidad | `<research>/evidence/<class>/`, **con sidecar de procedencia obligatorio** |
| **`hard-doc`** | documentación dura (§2.3) | su casa especial: `paths.hard_docs`, o fuera del repo con puntero + `sha256` + sidecar registrados en el ingest-log (§2.3) |

`<class>` es un valor del enum de §2.1, sin dialecto: la casa se llama como la
clase, y no hay carpeta de sobrantes. **`evidence/misc/`, `varios/` y similares
están prohibidos** (principio de diseño #5, §5).

**Ante ambigüedad, la ingesta pregunta y no avanza.** Si el destino no está
determinado — no se sabe la unidad, no se sabe la clase, o el mismo archivo
podría ser `document-drop` o `hard-doc` — la operación **se detiene y pregunta al
humano**. Nunca elige por defecto: adivinar la casa es el drift que esta sección
existe para impedir (principio de diseño #2 y principio de operación #1).

**El desenlace del original no cambia.** Copia al destino → fila en el log de
ingesta → commit → push → **verificación contra el remoto** (la rama remota debe
ser HEAD: dos copias independientes) → recién entonces se borra el original,
archivo por archivo re-verificado por hash. Si el push o la verificación fallan,
**nada se borra**. `--keep` conserva el original cuando debe seguir viviendo
afuera (el caso normal de `hard-doc`). Así el staging externo se vacía **solo**
tras ingesta verificada.

**El ingest-log queda idéntico.** Una fila por archivo — fecha, archivo,
`sha256`, origen externo, desenlace del original — y la fila es la misma
cualquiera sea el destino; la columna de archivo nombra ahora la ruta destino
real en vez de un nombre dentro de la bandeja. El régimen sigue siendo
append-only (§12, G6).

**Legado.** Los `inbox/` de proyectos que adopten el framework son **legado
congelado**: bronze que se lee y se cita, jamás se reescribe (§9.1), y donde no
nace nada nuevo. Reconciliarlos con las casas reales es trabajo de `/migrate`,
con el rastro doble de §9.2 y sin tocar un byte del verbatim.

#### Regla de activación

La spec **norma** el destino obligatorio y la desaparición del `inbox`; el
**kit 0.2.0** lo implementa junto con el resto de su bump (§9.4): destino en la
operación de ingesta, `paths` sin `inbox` y con `evidence`/`hard_docs`, y la
guarda apuntada a las casas reales (§4.4).

---

## 3. Contrato de runs

*Origen: Fase 2 ítem 3.* Canoniza el diseño ya probado en campo.

### 3.1 Los campos

En el frontmatter del protocol:

```yaml
runs: 2                  # N corridas dentro de la misma sesión
mode: independent        # independent | chained
```

Si no se declaran, rigen `runs.default` y `runs.default_mode` de
`framework.config.yaml`. El default del kit es `2` / `independent`.

**Las etiquetas son `run-01`..`run-NN` en ambos modos**, sin excepción. `C1`,
`C2`, `PI` y `S` son vocabulario histórico (§13.2): se leen, jamás se emiten.

### 3.2 Los dos modos

| Modo | Qué significa | Efecto epistémico |
|---|---|---|
| `independent` | **réplicas ciegas**: cada run repite la investigación desde el protocol, sin reutilizar hallazgos, fuentes ni conclusiones de los anteriores | alimenta replicación y detección de contradicciones entre runs; la convergencia **sube** madurez |
| `chained` | **partes deliberadas**: cada run declara qué continúa o profundiza del anterior | las N corridas son **UNA sola unidad epistémica**; la métrica de replicación se declara `n/a` |

**Encadenar es legal, se declara y pesa menos.** El pecado no es el contexto: es
el contexto **no declarado**. Un conjunto `chained` cuenta como una unidad
epistémica en la síntesis y en la jerarquía de independencia.

### 3.3 Ciclo de vida

- **`/plan`** declara `runs` y `mode` al escribir el protocol. Los
  encadenamientos se declaran en el plan; jamás se improvisan al lanzar.
- **`/launch`** los renderiza al bloque de preflight del payload y al checklist
  del humano.
- **El preflight de la sesión anuncia el plan de runs en una línea** antes de
  investigar; ante precondición incumplida se detiene y avisa.
- **`/close` valida N raws según el modo.** Si faltan corridas, la desviación se
  anota por escrito en el protocol antes de seguir; **jamás se completa
  investigando de más** en el cierre.

### 3.4 `needs` es el canal entre unidades

`needs` declara qué unidades deben estar `done` **y** cuyos `02-findings`
vigentes viajan en el payload. Es el único canal entre unidades: ni reports, ni
raws, ni material de unidades ausentes de `needs`. Los `needs` son mínimos por
diseño — el payload crece con cada uno.

**Una unidad está `ready` cuando toda unidad de sus `needs` está `done`.**
`ready` se deriva; no existe como estado almacenado.

---

## 4. Política de documentos markdown

*Origen: Fase 2 ítem 4.* Contra el "mar de markdown": el modo de falla criticado
en el tooling adyacente es exactamente lo que hay que diseñar para evitar.

### 4.1 Tres clases por mutabilidad

| Clase | Regla | Muerte |
|---|---|---|
| **record** | append-only y fechado. Se escribe una vez y **jamás se edita**. Se corrige por enmienda (archivo nuevo) o por **supersesión declarada** con puntero | nunca: un record no se borra |
| **evergreen** | **UNA casa por hecho**, dueño declarado. Se edita in-place para seguir siendo verdadero | **se BORRA al morir** — no se archiva: el historial ya vive en git |
| **efímero** | va al chat o al PR. **Jamás se convierte en archivo** | con la conversación |

### 4.2 Regla chat-primero

La clase por defecto de cualquier cosa que se quiera escribir es **efímero**.
**Un archivo nuevo exige consumidor y momento de lectura declarados en su
frontmatter.** Si no hay consumidor nombrado y un momento en que lo lea, no hay
archivo: va al chat.

```yaml
class: record | evergreen
consumer: <quién lo lee>
reading-moment: <cuándo lo lee>
date: <YYYY-MM-DD>          # obligatorio en record
owner: <quién lo mantiene>  # obligatorio en evergreen
```

Los artefactos de nombre fijo del framework (`00-protocol`, `01-report`,
`02-findings`, `03-sources`, `payload`, `raw/`) no declaran `class:`: su clase
la fija esta spec y el consumidor es el flujo.

### 4.3 Clase constitution

Los documentos de gobernanza — `constitution.md` del proyecto y esta spec — son
evergreen con **protocolo de enmienda duro**: toda modificación sube `version:`,
agrega fila al changelog y pasa por gate humano. Es la única forma de evergreen
cuyo cambio no es libre.

### 4.4 Enforcement

El enforcement por clase **SE SUMA** al enforcement por rutas de la guarda de
integridad, no lo reemplaza. La guarda por rutas es el backstop: protege
`raw/`, reports, findings, sources, payloads sellados, ADRs, **las casas de
bronze sin unidad (`<research>/evidence/<class>/`) y la casa de `hard-doc`**, y
las rutas extra que declare el proyecto, aunque un frontmatter mienta o falte.

**La protección sigue a las casas reales, no a una bandeja** (§2.6): con el
`inbox` fuera del contrato, lo que la guarda protegía en él lo protege ahora en
el destino donde el material aterriza. Un `inbox/` legado sigue protegido
mientras exista, como el bronze que es (§9.1).

**La guarda de integridad corre sin dependencias de terceros** — git y Python
estándar bastan, sin el kit de skills instalado y sin paquetes externos. El
subconjunto YAML que consumen la config y los frontmatter es, por contrato,
**escalares y listas inline**: nada que exija un parser completo.

### 4.5 Roster de archivos repo-level

*Origen: enmienda pre-gate E2 (§14.3).* §5 cierra las **carpetas** del repo;
esta tabla cierra sus **archivos de nivel repo**. Es el set completo de lo que el
framework reconoce fuera de la carpeta de una unidad: cada fila declara rol,
lector, momento de lectura y clase (§4.1), como exige la regla chat-primero
(§4.2) a cualquier archivo.

| Archivo | Rol | Lector | Momento de lectura | Clase |
|---|---|---|---|---|
| `README.md` (raíz) | qué es este repo y dónde está cada cosa | humano o agente que aterriza por primera vez | al abrir el repo | evergreen — **puntero delgado** |
| `CLAUDE.md` (raíz) | cómo se opera este repo: qué skills existen, qué está prohibido, dónde están las reglas | sesión de agente | al iniciar toda sesión | evergreen — **puntero delgado** |
| `framework.config.yaml` (raíz) | el contrato de este repo con el kit y su **ancla** (rutas, `ids`, `runs`, `horizons`, `metrics`, `context`, `language`, `kit_version`) | scripts del kit y guarda de integridad | en cada corrida de tooling | evergreen; su **bloque ratificado** cambia solo por enmienda (§12, G4) |
| `<research>/constitution.md` | gobernanza del repo: supuestos refutables, dominio, techo de gasto, umbrales de QA, disparadores | humano en los gates; el coordinador al comisionar | antes de todo gate y de congelar unidades | evergreen **clase constitution** (§4.3) |
| `<registry>/*.md` | la memoria del programa: los ocho registries que son record (metrics, ingest-log, supersessions, migrations, qa-audits, gates, requirements, conflicts) | coordinador, síntesis, auditoría | al cerrar, citar o auditar | **según §12, G6** — append-only o marcable |
| `<registry>/STATUS.md` | tablero de estado del programa; el noveno registry y el único que no es record | humano y coordinador | al planificar y al lanzar | **vista derivada** — regenerable, jamás editada a mano, jamás autoritativa (§12, G6) |
| índice puerta-de-entrada | `id → slug → objetivo en una línea → status` (§1.2) | quien necesita saber sin abrir cada unidad | al orientarse en el corpus | **vista derivada generada** — la genera el kit; hoy no existe (preguntas al final, #1) |
| `SPEC.md` (en el kit) | esta spec: la constitution del framework | toda sesión, humano o script que opere bajo el framework | antes de crear, cerrar o migrar cualquier artefacto | evergreen **clase constitution**; **vive en el kit y en ningún repo consumidor** — un repo la referencia por la versión de kit que declara su config |

Los archivos de una unidad (`00-protocol`, `payload`, `raw/`, `01-report`,
`02-findings`, `03-sources`) no son repo-level: los norma §5, y por diseño viven
dentro de la carpeta de su unidad (principio de diseño #5).

Tampoco entra el **tooling que el kit instala** —las skills vendorizadas, el hook
de integridad y su shim—: es maquinaria versionada por el kit, no conocimiento
del repo. No aloja reglas, se reemplaza en cada bump, y por eso ni ocupa fila ni
abre la taxonomía.

Como esos artefactos de nombre fijo, **los del roster no declaran `class:` en su
frontmatter**: su clase la fija esta tabla y su consumidor es el framework (§4.2).
La constitution del proyecto es la excepción esperable — declara lo que exige su
protocolo de enmienda (`version:`, changelog), no su clase.

**Taxonomía cerrada.** La tabla es el set completo. **Un archivo repo-level
nuevo exige enmienda de esta spec** — con su fila declarada, como los prefijos de
unidad exigen entrada de config y de glosario (§1.3). Un archivo repo-level que
no esté en la tabla no es "una excepción": es una violación que el flujo de
normalización trata como tal.

**Regla de entrada: el conocimiento vive UNA vez.** Los archivos de entrada
(`README.md`, `CLAUDE.md`, el índice) son **punteros delgados o vistas
generadas** — jamás segundas casas de una regla. Apuntan a donde la regla vive
(esta spec, la constitution, la config) y no la repiten, ni siquiera "resumida":
un resumen es una copia que deriva en silencio (principio de diseño #4,
principio de operación #1).

*Prueba:* si se borra un archivo de entrada, **no se pierde ninguna regla** —
solo el atajo para encontrarla. Un archivo de entrada que no pasa la prueba está
albergando conocimiento que le pertenece a otra casa, y se corrige moviéndolo,
no duplicándolo.

**Dos constancias que esta tabla deja por escrito:**

- **`briefing.md` no existe como archivo.** El briefing es la Parte II del
  documento de plan que comisiona las unidades, y el protocol lo apunta con
  `plan:` (§12, G1). No hay, ni habrá, un briefing top-level.
- **`AGENTS.md` no es parte del framework.** Ninguna fila lo declara y ninguna
  regla vive ahí. Si un harness externo lo exige, se **genera** desde la misma
  fuente que `CLAUDE.md` — nunca se redacta aparte, porque un segundo archivo de
  instrucciones escrito a mano es exactamente la segunda casa que la regla de
  entrada prohíbe.

#### Regla de activación

La spec **norma** el roster; verificarlo (archivo repo-level fuera de la tabla,
archivo de entrada engordado a segunda casa) es trabajo del chequeo de integridad
del **kit 0.2.0**, junto con el resto de su bump (§9.4).

---

## 5. Estructura estándar de unidad

*Origen: Fase 2 ítem 5.*

**La carpeta de la unidad contiene TODO lo suyo.**

```
<investigations>/<id>-<slug>/
├── 00-protocol.md          record (desde `frozen`)
├── payload.md              record (desde el sello de launch)
├── raw/                    bronze — verbatim, jamás editado ni QA'd
│   ├── run-01.md
│   └── <binario>.<ext> + <binario>.<ext>.meta.yaml   (sidecar de procedencia)
├── 01-report.md            silver
├── 02-findings.md          gold — el único que viaja entre unidades
└── 03-sources.md           bitácora de búsqueda
```

**Estándar de artefactos.** Qué es cada archivo, en qué capa vive y bajo qué
régimen:

| Archivo | Capa | Régimen | Contenido |
|---|---|---|---|
| `00-protocol.md` | — | record (desde `frozen`) | la comisión: objetivo, `needs`, fuera de alcance, kill criteria, mapa de áreas |
| `payload.md` | — | record (desde el sello) | el sobre exacto que recibió la sesión |
| `raw/run-NN.md` | bronze | record | exports verbatim; jamás editados, jamás QA'd |
| `01-report.md` | silver | record | hallazgos completos validados contra plantilla |
| `02-findings.md` | gold | record | resumen ≤2 páginas — el único que viaja entre unidades |
| `03-sources.md` | — | record | bitácora de búsqueda |

Los reports y findings llevan frontmatter mínimo: `id`, `unit`, `date`.

- Las versiones por supersesión (`01-report.v2.md`, …) viven **en la misma
  carpeta**, junto al record que superan. La versión vigente es la de mayor
  `.vN`, o la base si no hay ninguna.
- El bronze no textual vive en `raw/` como cualquier otro bronze, con su
  sidecar al lado (§2.2).
- **El repo no crea carpetas genéricas top-level nuevas.** Los nombres son
  inequívocos entre proyectos que comparten el framework: nada que se llame
  `payloads/`, `docs-varios/` o similar.

**Rutas del repo.** Las declara `framework.config.yaml` (`paths`), y solo ahí:
`research`, `investigations`, `registry`, `decisions`, `evidence`, `hard_docs`,
`constitution`. **`inbox` ya no es una de ellas** (§2.6): `evidence` es la casa
del bronze con clase pero sin unidad, y `hard_docs` la casa especial de la
documentación dura (§2.3). Los **archivos** de nivel repo los cierra §4.5, igual
que estas rutas cierran las carpetas.

**Statuses de una unidad:** `pending → frozen → running → qa → done`, solo hacia
adelante. `pending` es lo único con cuerpo editable; desde `frozen` el cuerpo del
protocol es record y solo se sellan campos de frontmatter (`status`, `session`,
`constitution`, `runs`, `mode`, `context`).

---

## 6. Frescura y recurrencia

*Origen: Fase 2 ítem 6.* Dos capas de **UN** mecanismo: el conocimiento deja de
valer, y el panorama se mantiene fresco por diseño, no por memoria del humano.

### 6.1 Capa pasiva — `review_by` (caducidad)

`review_by` **se deriva, jamás se almacena**:

```
review_by = fecha del record + horizonte(volatility)
```

Horizontes por defecto, en meses: `high` 6 · `medium` 18 · `low` 36 (o
solo-por-disparador). Viven en `framework.config.yaml` (§12, G4).

**Disparadores de re-verificación:** venció `review_by`, o entró evidencia
material nueva (fuentes significativas o un resultado que cambia la
conclusión). **Un hallazgo vencido sin re-verificar baja un nivel de madurez
automáticamente**: se refresca o entra degradado a la síntesis — jamás lavado.

Cuando un hallazgo menciona más de una volatilidad, **rige la más volátil**.

### 6.2 Capa activa — `refresh:` (recurrencia)

Una unidad puede declarar una **cadencia** de re-ejecución en el frontmatter de
su protocol:

```yaml
refresh: 18m        # <N><w|m|y> — semanas, meses o años
```

Al vencer la cadencia, se programa la re-ejecución: **una corrida o versión
nueva que supersede a la vencida, jamás una edición**. La cadencia se declara,
nunca la fecha: la fecha se deriva de la cadencia más la fecha del último
cierre — un valor derivado almacenado se pudre.

**La diferencia entre las dos capas.** `review_by` dice *"esto ya no se puede
afirmar con esta madurez"*; `refresh:` dice *"esto se vuelve a investigar cada
tanto, haya vencido o no"*. Ambas resuelven a una fecha, ambas alimentan el
pre-flight de síntesis, y ninguna edita nada: producen supersesión.

### 6.3 Disparadores del proyecto

Un proyecto puede declarar **disparadores** propios en su constitution:
condiciones fechadas o eventuales que fuerzan re-verificación aunque el
horizonte no haya vencido (p. ej. la entrada en vigor de una norma que sustituye
a la citada). Los disparadores son reglas ratificadas, no números: por eso viven
en la constitution y no en la config (§12, G4).

### 6.4 Re-síntesis

Cuando entra material relevante para una síntesis ya emitida, la síntesis se
**re-emite por supersesión declarada**, jamás editando la anterior.

---

## 7. Reglas heredadas del v1

*Origen: Fase 2 ítem 7 — los cinco puntos de la retro que v0.3 canoniza sin
cambio de fondo.*

### 7.1 Cierres de sesión pre-registrados (retro #7)

La fase más frágil del ciclo es el cierre: las sesiones autónomas entregan
informes, no logs, y la bitácora nace incompleta si se reconstruye al final.

**Regla.** El registro de consultas se hace **en vivo, dentro de la sesión**, no
se reconstruye al cerrar. La bitácora (`03-sources.md`) separa explícitamente:

- **consultas con texto verbatim conservado** — en tabla, con su resultado
  (hallazgo o ausencia);
- **accesos reportados sin string exacto** — listados aparte y **declarados como
  limitación**;
- **fallas de acceso** (404, paywall, bloqueo) — registradas como eventos.

**Jamás se reconstruye una consulta de memoria.** Una ausencia documentada es
evidencia; una consulta inventada es contaminación.

### 7.2 Namespaces de supersesión (retro #8)

Los IDs jamás se reutilizan — pero hasta ahora la spec no decía cómo evitar la
colisión cuando un record superado y su versión nueva conviven.

**Regla.** Un record `.vN` elige uno de dos caminos, y lo declara:

- **conserva el espacio de sub-IDs de la base** — los IDs siguen siendo los
  mismos y siguen siendo válidos; o
- **declara un espacio nuevo unificado** — y entonces el ID externo de cada
  sub-ID lleva el namespace de la versión: **`<unit>-v<N>-<kind><NN>`**. La
  fila de supersesión **declara el retiro del espacio viejo**: los sub-IDs del
  record superado quedan retirados junto con él, y nada en el registry los cita.

En ningún caso se renumera en el lugar ni se reutiliza un ID retirado.

### 7.3 Peso de evidencia: quién lo asigna y cuándo (retro #9)

Sobre un mismo conflicto pueden pronunciarse tres niveles distintos, y hasta
ahora la spec no definía precedencia.

**Precedencia, de mayor a menor:**

1. **Directriz humana** — fijada en un gate o en la constitution.
2. **Juicio del coordinador** — al cerrar la unidad.
3. **Juicio de la sesión** — en su propio report o consolidación.

**Un nivel inferior jamás revierte en silencio a uno superior.** Si la sesión o
el coordinador discrepan de un peso ya fijado en un gate, eso **no se reconcilia
con una nota**: se abre la fila de conflicto (`con-NN`) y la adjudica el gate
que corresponda.

**Una sesión no adjudica contradicciones entre sus propios runs.** Reporta las
dos versiones; el peso lo asigna el coordinador o el humano. Toda asignación de
peso se registra en la columna correspondiente de la fila de conflicto, con el
nivel que la fijó y su fecha.

### 7.4 Gates agrupables y registro de consumo (retro #11)

Los gates conversacionales funcionan pero no escalan: con latencia real, el
programa se frena.

**Regla.** Los gates pueden agruparse en un **acta de ratificación**: una lista
enumerada donde cada ítem trae su propuesta de resolución y las alternativas
descartadas en una línea, de modo que el humano resuelva el lote **leyendo solo
el acta**. Un acta no cambia la autoridad de ningún gate: la agrupa.

**Todo gate consumido se registra** — cuál, cuándo, qué se decidió y qué
enmendó — en el registry de gates (§12, G6). Hoy ese rastro está disperso entre
CLAUDE.md y changelogs; a partir de v0.3 tiene una casa.

### 7.5 Retro obligatoria (retro #12)

**Todo proyecto que adopte el framework produce una retro como record estándar
tras su implantación.** No es opcional ni depende de que el humano se acuerde de
pedirla: el framework mejora con la misma disciplina de evidencia que impone.
La retro es un record con consumidor declarado — quien redacte la siguiente
versión de esta spec.

---

## 8. Postura de contexto por unidad

*Origen: Fase 2 ítem 8.* La segunda cara del sesgo. La primera es la
contaminación por la tesis; esta es el **eco por frecuencia**: lo repetido en un
corpus se vuelve verdad para el modelo por acumulación, no por evidencia. El
caso patológico está documentado: documentación mala no solo confundió — **redefinió
el producto**.

### 8.1 El campo

En el frontmatter del protocol:

```yaml
context: clean-room | scoped
```

El default del proyecto se declara en `framework.config.yaml`
(`context.default`); el default del kit es `scoped`.

### 8.2 Qué viaja en cada postura

| `context` | Composición del payload |
|---|---|
| `scoped` | preflight + **briefing** + `02-findings` vigentes de sus `needs` + protocol |
| `clean-room` | preflight + protocol. **Nada más.** |

**Jamás viajan, en ninguna postura:** la semilla o tesis del proyecto, la
constitution completa, reports o raws de otras unidades, ni material de
unidades ausentes de `needs`.

- **`scoped`** es para integración: recibe lo que sus `needs` declaran y las
  decisiones vigentes, nada más.
- **`clean-room`** es para exploración, competencia de ideas y etapas
  tempranas, y para toda unidad **sensible a falsificación** — aquella donde
  conocer la tesis sesgaría la búsqueda. Generaliza dos reglas ya probadas: la
  sala limpia y "la semilla nunca viaja".

### 8.3 Guardas

- **`clean-room` exige `needs: []`.** Si una unidad necesita findings ajenos, no
  es sala limpia. La secuenciación por presupuesto o por orden humano no es un
  `need`: es cuándo se congela y se lanza.
- **Corpus solo-vigente como precondición estructural.** Lo que viaja es siempre
  la versión vigente (mayor `.vN`); un record superado jamás entra a un payload.
  Un corpus donde conviven tres versiones sin vigente declarado produce eco por
  construcción.
- **La evidencia de qué recibió una unidad es su `payload.md` sellado**, no un
  campo. El campo `constitution:` sella la **versión de gobernanza vigente al
  lanzar** (procedencia de las reglas bajo las que corrió), no lo que la unidad
  leyó.

**Deuda declarada:** la fila de contrato existe desde antes que su mecanismo.
Esta sección **define** el mecanismo; el kit lo implementa después (§12, G2).

---

## 9. Migración por capas

*Origen: Fase 2 ítem 9 · principio de diseño #7.* El legado que solo aplica a
una parte del repo confunde a modelos y a mantenedores. Cuando el framework
mejora, un proyecto puede y debería migrar TODO a la versión vigente — y si eso
implica trabajo extra, se hace.

### 9.1 Qué capa se toca cómo

| Capa | Qué se hace | Cómo se verifica |
|---|---|---|
| **evergreen** | se actualiza **in-place** | revisión normal |
| **derivados** (tablero, `review_by`, vistas, índices) | se **regeneran** | regenerar y comparar |
| **records de lectura** (findings vigentes, reports) | **supersesión mecánica**: relabel por script, motivo declarado `migración a <versión>` | **el diff es la evidencia**; round-trip cuando el pase es puramente mecánico |
| **verbatim bronze** (`raw/`, `evidence/`, la casa de `hard-doc`, payloads sellados, y los `inbox/` legados) | **JAMÁS se reescribe** | se lee con glosario (§13.2) |

**Por qué el verbatim es intocable:** es el rastro de auditoría. Un byte añadido
rompe la cadena `sha256` que hace auditable cada afirmación que lo cita.

**Opt-in humano.** El pase de supersesión mecánica sobre records de lectura se
ofrece con el diff a la vista; el humano decide. Una migración jamás produce
supersesiones vacías: un record ya canónico no se supersede "por consistencia".

**Reubicar no es reescribir.** Llevar un `inbox/` legado a las casas reales
(§2.6) mueve archivos sin tocar su contenido: el `sha256` de cada uno sigue
siendo el mismo — que es justamente lo que hace verificable el pase. Es opt-in
del humano como cualquier otro, deja el rastro doble de §9.2, y **no habilita
ninguna edición del verbatim**.

### 9.2 Rastro obligatorio

Toda migración deja **doble anotación**:

1. **Entrada en el log de migraciones del registry** — qué cambió, cuándo, a qué
   versión, y cómo se verificó (incluido lo que quedó **fuera de alcance y por
   qué**).
2. **Anotación en el sidecar** de cada record afectado — "vocabulario histórico;
   glosario en spec §13".

**La incisión va SIEMPRE al sidecar, jamás dentro del verbatim.**

### 9.3 Sintonía como estado verificable

Un proyecto **sintonizado** tiene todo en formato vigente salvo el bronze, que
se lee con glosario.

**Un repo cuya versión de kit declarada no coincide con la del kit instalado
está desincronizado, y eso es un error de integridad — no una advertencia.**
El chequeo de integridad lo reporta como problema y el repo no se considera
sano hasta correr el runner de migraciones.

### 9.4 Regla de activación de esta sección

Los pases que esta spec habilita se ejecutan **con el bump de versión del kit
que los implementa**, nunca sueltos. En particular, la migración del enum
(§1.6) es un pase indivisible: parsers, plantillas, claves de `horizons` y
corpus nuevo, juntos.

---

## 10. Modelo de ejecución y pipelines

*Origen: v0.2 §4 y §5, arrastradas; enmendadas solo donde los ítems 3, 8 y la
laguna G3 las tocan.*

### 10.1 Modelo de ejecución

- **Regla de readiness.** Lo que está ready se lanza — todo, en paralelo. Las
  "olas" son una descripción emergente de lo que quedó ready junto, no un
  mecanismo. La ceguera entre unidades concurrentes es lo que hace seguro el
  lanzamiento en bloque: **todo acoplamiento legítimo ya está en `needs`**, así
  que dos unidades vivas no pueden depender entre sí, y los chequeos de colisión
  son innecesarios por construcción. El escalonamiento aparece solo donde una
  restricción real lo impone (cuotas de plataforma), jamás a priori.
- **Canary (una vez).** El primer report del programa se valida contra la
  plantilla antes del lanzamiento masivo. Una vez que pasa, la plantilla es
  confiable.
- **Sesión = frontera de aislamiento.** Un chat por unidad, titulado
  `rNN — slug`. Varios runs dentro de una sesión siguen siendo **una** unidad.
- **Encadenamiento.** Dejó de ser una nota sobre una sesión compartida: es
  `mode: chained` declarado en el protocol (§3.2). La URL de `session` sigue
  siendo prueba de qué corrió dónde, pero ya no es el único registro de la
  no-independencia.
- **Escritor único.** Solo el coordinador escribe al repo. El pipeline de cierre
  serializa la entrada.
- **Caducidad.** Rige §6: el pre-flight de síntesis falla ante cualquier hallazgo
  vencido sin re-verificar — se refresca o entra degradado, jamás lavado.

### 10.2 Las pipelines

**`/inception`** — de idea cruda a programa congelado.

1. Entrevista de elicitación sobre la idea, por vaga que sea.
2. Redactar la **constitution** del proyecto: supuestos refutables, dominio,
   techo de gasto, umbrales de QA y disparadores (§6.3). Los horizontes de
   caducidad **no se escriben acá**: viven en el bloque ratificado de la config
   (§12, G4). Se emite como v1 con changelog de enmiendas vacío, estructurada
   para ser compatible con la constitution del desarrollo dirigido por
   especificación que la síntesis sembrará. **Gate: el humano ratifica.**
3. Redactar el **mapa de investigación** (unidades, objetivos, fuera de alcance,
   `needs`, kill criteria) y el **briefing** del programa como Parte II del plan
   (§12, G1). **Gate: el humano ratifica — acá es donde el juicio humano se gana
   el sueldo.**
4. Scaffold + freeze: scripteado, determinista, aburrido a propósito. El
   scaffold siembra la config del repo — incluido su `language` (§1.8),
   confirmado con el humano, no adivinado.

**`/launch rNN`** — cuando una unidad está ready.

Armar el payload según su postura de contexto (§8.2) → chat nuevo titulado
`rNN — slug` → **sellar `session`, `constitution` y `status: frozen → running`,
y commitear el payload como record** → correr los N runs del contrato (§3) →
antes de cerrar el chat, pedir **ahí mismo** el report en plantilla, el borrador
de findings y la bitácora (esa sesión tiene el contexto completo: es el mejor
lugar para destilar) → los exports verbatim aterrizan directo en
`raw/run-NN.md`, por ingesta con destino declarado (§2.6; §12, G3).

**`/close rNN`** — el gate de QA y todo lo que sigue. Los pasos 1–3 son el
status `qa`.

1. **Validación de formato** — scripteada: columnas de la tabla de requisitos,
   IDs, y madurez + volatilidad + fecha + ID de fuente en cada afirmación.
   **La validación estricta es la norma.** Existe un modo *lenient* que baja
   todo error a advertencia; está **reservado al retro-parse de corpus
   artesanal** del flujo de adopción (fuera del alcance de v0.3), un cierre
   normal jamás lo usa, y todo cierre lenient anota su desviación por escrito.
   Lo que no valida se corrige **en origen** — jamás se maquilla un export.
2. **Auditoría de afirmaciones** — script + prompt: verificación de existencia
   de la fuente sobre una muestra determinista, chequeo de soporte
   afirmación↔fuente, y detección de eco (las fuentes de un mismo origen
   colapsan a una). Si participan jueces LLM: intercambio de posición, ≥2
   jueces, y muestreo periódico de acuerdo contra el gate humano. **Fuente
   inexistente o afirmación sin soporte ⇒ STOP: gate humano.** Todo queda
   trazado en el registry de auditorías.
3. **Kill criteria**, propios y ajenos — cualquier disparo va al gate humano de
   inmediato.
4. **Commit de records** inmutables; registro de fuentes.
5. **Extracción al registry:** requisitos marcados (`new` / `duplicate` /
   `contradicts`) y conflictos anotados — que solo se anotan: se resuelven en la
   síntesis. Una entrada que contradice a otra existente **sin `supersedes:` se
   rechaza** (principio de operación #2).
6. **Métricas** — una fila por cierre, con valores **medidos** en los pasos 1–2.
   Nada estimado; lo no medido se declara con su token. QA que no mide nada es
   ceremonia.
7. **Finalizar los findings** sobre el borrador de la sesión, conservando la
   atribución por `run-NN` cuando hubo varios runs.
8. **Cerrar** — `status: qa → done`, recomputar ready y anunciar qué se abrió y
   cuál es el próximo gate humano.

**`/synthesis`** — fan-in sobre todas las unidades del alcance.

Pre-flight: todas las unidades en `done`, IDs únicos, conflictos anotados,
findings escritos, ningún kill criterion sin resolver, **ningún hallazgo vencido
sin re-verificar**, y constitution ratificada (draft ⇒ FAIL bloqueante). El
fan-in respeta la jerarquía de independencia y la precedencia de peso de
evidencia (§7.3); un conjunto `chained` cuenta como **UNA** unidad epistémica.
Salidas: siembra de `decisions/` (los primeros ADRs citan findings), de
`architecture/`, y de la **constitution de desarrollo** — que hereda los
invariantes ratificados con sus `review_by` sellados. **La síntesis misma es
gate humano**, y si supera a una síntesis anterior entra por supersesión
declarada.

Cerrada la implantación, la **retro es obligatoria** (§7.5).

---

## 11. Gates

*Origen: v0.2 §6 y §7, arrastradas; ampliadas por la retro #11 (§7.4) y por la
enmienda del bloque ratificado (§12, G4).*

### 11.1 Los gates son datos

El esquema es el kernel:
`{trigger, check, authority: human | script | prompt | threshold, evidence in,
record out}`. **Qué** gates existen, y con qué autoridad, es un playbook por
tipo de flujo. Esta spec instancia el playbook de inception.

| Gate | Disparador | Chequeo | Autoridad | Evidencia de entrada | Record de salida |
|---|---|---|---|---|---|
| Ratificación de la constitution | `/inception` paso 2 | supuestos, dominio, techo de gasto, umbrales, disparadores | humano | borrador de constitution | `constitution.md` v1 |
| Ratificación del mapa | `/inception` paso 3 | alcance de unidades, `needs`, kill criteria, briefing | humano | borrador de mapa | protocols congelados |
| QA del report | `/close` pasos 1–2 | plantilla, etiquetas, auditoría de afirmaciones | script + prompt | report + sources | fila de métricas + registry de auditorías |
| Disparo de kill criteria | cualquier hallazgo, cualquier unidad | la decisión afectada se revisa de inmediato | humano | hallazgo disparador | enmienda / ADR |
| Decisiones de síntesis | `/synthesis` | todo lo que la síntesis decide | humano | registry completo | ADRs · arquitectura · constitution de desarrollo |
| Enmienda del bloque ratificado | cambio en `horizons`, `runs`, `ids`, `metrics` o `context` | ¿sube `version:` de la constitution en el mismo commit? | humano + script | diff de la config | bump + changelog |

**Todo gate consumido deja además su fila en el registry de gates** (§7.4,
§12 G6): cuál, cuándo, qué se decidió y qué enmendó.

### 11.2 Agrupación

Los gates de esta tabla pueden presentarse agrupados en un **acta de
ratificación** (§7.4) sin que ninguno pierda su autoridad. Agrupar es una
concesión a la latencia humana, no una rebaja del control.

### 11.3 Fuera de alcance en 0.3 — modo continuo (declarado, diferido)

Sigue diferido, como en la v0.2: retroalimentación producción→investigación
(telemetría e incidentes como clase de fuente que dispara re-investigación,
enmienda findings y supersede ADRs); gates de vigencia automáticos sobre
documentos evergreen; y tipos de flujo más allá de inception —feature,
mantenimiento, incidente— instanciando los mismos artefactos y plantillas con
distintos parámetros de gate sobre el esquema de §11.1. **Declarar el hueco le
gana a fingir que se cubre.**

---

## 12. Resolución de las lagunas de la extracción (G1–G6)

*Origen: Fase 2 ítem 10 — agenda obligatoria. Una decisión por laguna.*

### G1 — Dónde vive el briefing (Bloque Común) en un repo genérico

**Decisión.** El briefing vive como **Parte II del documento de plan** que
comisiona las unidades, y el protocol lo apunta con el campo **`plan:`** de su
frontmatter, que queda **ratificado como contrato**. `/launch` resuelve el
briefing siguiendo ese puntero; si el protocol no lo declara, **pregunta al
humano — jamás lo adivina**.

**Por qué.** Un repo puede correr varios programas con briefings distintos; un
`briefing.md` genérico top-level sería mentira o derivaría (principios de diseño
#1 y #5). La separación que la retro exigía se logra **por nombre y por casa**,
no por archivo suelto: `constitution` = gobernanza del repo, **`briefing`** =
bloque común de payload. El término "constitution" pasa a nombrar exactamente
una cosa, que es lo que la retro pedía.

**Consecuencia sobre la v0.2.** Esta decisión **amenda** la v0.2: allí el
payload incluía la constitution. En v0.3 **la constitution completa jamás viaja
en un payload**; lo que viaja es el briefing (§8.2).

### G2 — Mecanismo de `context: clean-room | scoped`

**Decisión.** El mecanismo queda definido en **§8**: campo en el frontmatter del
protocol, default por proyecto en la config, composición de payload por postura,
y tres guardas (`clean-room` exige `needs: []`; corpus solo-vigente; el payload
sellado es la evidencia). **La spec lo define; el kit lo implementa en 0.2.0.**
Hasta entonces la fila de contrato es deuda declarada, no una regla incumplida.

### G3 — Quién mueve `inbox/` → `raw/run-NN.md`

**Decisión.** **Nadie lo mueve: el verbatim de un run aterriza directo en la
carpeta de su unidad.** La operación de ingesta acepta destino de unidad y run
(`--unit <UNIT_ID> --run <N>`) y escribe en `<unit>/raw/run-NN.md`, registrando
la fila de procedencia igual que cualquier ingesta. `/close` **solo verifica**
que existan los N raws del contrato: no mueve nada.

**Generalizada por la enmienda E1 (§2.6): no hay tramo, porque no hay bandeja.**
La resolución original dejaba el inbox vivo "para todo lo demás"; esa mitad
**muere**. El destino es obligatorio para toda ingesta y solo puede ser uno de
tres —unidad, clase sin unidad (`<research>/evidence/<class>/`) o `hard-doc`—, y
ante ambigüedad la ingesta pregunta y no avanza. `inbox` sale de `paths` y de la
guarda; la protección de rutas pasa a las casas reales (§4.4, §5).

**Por qué esta y no las alternativas.** Que `/close` mueva desde el inbox es
**estructuralmente imposible sin debilitar la guarda de integridad**: el inbox
era record inmutable, y la guarda rechaza mover, renombrar o borrar esas rutas.
Asignar el paso al mover exigiría una excepción en la guarda; asignarlo a la
ingesta no exige ninguna. Y conservar el inbox como casa de lo que no es un run
sostenía una segunda estación sin dueño para material que **igual** hay que
clasificar: si toda llegada es atendida, clasificar al ingerir cuesta lo mismo y
cumple colocación por unidad (principio de diseño #5) desde el primer segundo.

### G4 — Dónde viven los horizontes de caducidad

**Decisión — un valor, una casa; la autoridad, otra:**

- **Los números viven en `framework.config.yaml`** (`horizons`) y **en ningún
  otro lado**. El tooling los lee de ahí. La constitution **no los repite**:
  apunta a la config.
- **La autoridad sigue siendo humana.** `horizons` pertenece al **bloque
  ratificado** de la config, junto con `runs`, `ids`, `metrics` y `context`.
  Cambiar cualquier clave del bloque ratificado es una **enmienda**: exige subir
  `version:` de la constitution en el mismo commit y anotar su changelog. El
  resto de la config (`paths`, `language`, `kit_version`, rutas inmutables
  extra) es operativo y no exige enmienda — lo que no significa gratis: mover una
  ruta o cambiar `language` arrastra migración (§1.8, §9).
- **Los disparadores del proyecto viven en la constitution** (§6.3): son reglas
  ratificadas, no números, y no tienen representación en la config.

**Por qué.** Dos casas para el mismo número es exactamente el drift que el
framework existe para evitar (principio de diseño #4), y el riesgo es concreto:
el mismo trío de horizontes está hoy escrito a mano en una constitution de
proyecto **y** como default en la config del kit — el día que ese proyecto
adopte el kit, tendría dos casas para el mismo número. Poner el valor en la
config sin más habría dejado un número epistémico editable sin gate; el bloque
ratificado resuelve las dos mitades.

*Implementación: el chequeo "bloque ratificado cambiado sin enmienda" es trabajo
del kit 0.2.0.*

### G5 — Ancho de los sub-IDs

**Decisión.** **Ratificado: un solo `ids.width` gobierna todo** — IDs de unidad,
sub-IDs (`srcNN`, `reqNN`, `conNN`) e IDs de registry (`con-NN`). Mismas reglas
de desborde (el ancho es mínimo, crece, nada se renumera) y mismo orden
numérico. Única excepción documentada: `adr-NNNN`, por convención MADR externa
(§1.5).

**Por qué.** Un mecanismo por problema (principio de diseño #1): un segundo
knob de ancho sería una perilla por proyecto que nadie necesita.

### G6 — Qué registries son append-only

**Decisión — tabla normativa.** Los registries son un set cerrado que fija esta
spec, no el proyecto:

| Registry | Archivo | Régimen |
|---|---|---|
| Metrics | `metrics.md` | **append-only** |
| Ingest log | `ingest-log.md` | **append-only** |
| Supersessions | `supersessions.md` | **append-only** |
| Migrations | `migrations.md` | **append-only** |
| QA audits | `qa-audits.md` | **append-only** |
| **Gates** | `gates.md` | **append-only** — un registro por gate consumido (§7.4) |
| Requirements (RTM) | `requirements.md` | record **marcable**: las filas jamás se borran; una fila superada se marca `SUPERSEDED by <id>`, y una enmienda propaga marca de invalidación |
| Conflicts | `conflicts.md` | record **marcable**: la fila evoluciona en sus columnas de resolución y status; el ID y el origen no cambian |
| Status | `STATUS.md` | **vista derivada** — regenerable, jamás editada a mano, jamás autoritativa. No es un record |

**Append-only significa que el contenido previo no se pisa**: se agrega al
final, y el encabezado del propio archivo lo declara. **Marcable** significa que
la fila se edita solo para marcarla, nunca para borrarla ni para cambiar lo que
afirmó.

*Estado de implementación: ocho de los nueve existen en el kit 0.1.0.
**`gates.md` es nuevo** — lo exige §7.4 y lo siembra el kit 0.2.0. La spec lo
declara; no lo implementa.*

---

## 13. Glosario

### 13.1 Vocabulario vigente, en llano

| Término | Qué es |
|---|---|
| **unit** | una pregunta acotada = una sesión = un objetivo enunciable en una línea |
| **run** | una corrida de investigación dentro de la sesión de una unidad |
| **protocol** | la comisión de la unidad, pre-registrada y congelada antes de investigar |
| **briefing** | el bloque común que viaja en todo payload de un programa (Parte II del plan) |
| **constitution** | las reglas de gobernanza del repo, ratificadas por el humano |
| **payload** | el sobre exacto que recibió una sesión; record desde el sello |
| **report** | el informe completo de la unidad, validado contra plantilla |
| **findings** | el resumen ≤2 páginas; el único artefacto que viaja entre unidades |
| **sources** | la bitácora de búsqueda de la sesión |
| **RTM** | la tabla maestra de requisitos del registry |
| **kill criteria** | condiciones medibles que detienen una unidad y disparan gate humano |
| **expiry** | caducidad: `review_by` derivado de fecha + horizonte de volatilidad |
| **refresh** | cadencia de re-ejecución declarada por la unidad |
| **chain of evidence** | la cadena de trazabilidad `source → … → code`, solo hacia arriba |
| **medallion** | bronze (verbatim) → silver (re-derivable) → gold (findings) |
| **supersession** | operación por la que un record queda superado por otro, con puntero y sin borrarse |
| **clean-room** | postura de contexto donde solo viaja el protocol |
| **acta** | lote de gates presentado para que el humano lo resuelva de una sola lectura |
| **evidence** | la casa del bronze que tiene clase de fuente pero no pertenece a ninguna unidad: `<research>/evidence/<class>/` |
| **language** | el idioma de prosa del repo, declarado en la config; los nombres del framework siguen en inglés (§1.8) |

### 13.2 Vocabulario histórico — contrato de lectura del corpus viejo

El bronze jamás se reescribe (§9.1). Estas equivalencias son **parte del
contrato**: quien lea un record histórico las necesita, y quien migre no las
aplica al verbatim.

| Histórico | Significaba | Canónico v0.3 |
|---|---|---|
| `C1`, `C2`, `CN` | "Corrida N" (híbrido español) | `run-01`, `run-02`, `run-NN` |
| `PI` | "pasada inicial" — la primera corrida de la unidad | `run-01` |
| `S` | verificación hecha dentro del chat, no una corrida | no es un run: es una verificación, y va a `03-sources` y al registry de auditorías |
| `K1`..`K7` | temas o conflictos clave levantados por una sesión | `<unit>-conNN`, y `con-NN` si es load-bearing |
| `CONTRA-NN`, `CONTRA-rNN-NN` | contradicción anotada por unidad | `<unit>-conNN` |
| `establecido / respaldado / plausible / especulativo` | enum de madurez, dialecto canónico español | `established / supported / plausible / speculative` |
| `est / sup / pla / esp` | el mismo enum, abreviado por una sesión | ídem |
| `established / supported` (parcial) | el mismo enum, en inglés a medias | ídem, completo |
| `alta / media / baja` | enum de volatilidad en español | `high / medium / low` |
| `<unit>-v2-srcNN` | espacio de fuentes de un record superado | **vigente** — es el namespace de supersesión (§7.2) |
| "Bloque Común" | el bloque común del payload | **briefing** |
| `inbox/` | la bandeja de entrada dentro del repo (v0.2 y kit 0.1.x) | **no existe**: el staging es externo y la ingesta clasifica en la puerta (§2.6). Los `inbox/` de repos adoptados son bronze congelado que `/migrate` reconcilia |

### 13.3 Legado español → estándar

paquete → **protocol** · brief → **report** · hallazgos clave → **findings** ·
registro de fuentes → **sources** · tabla maestra de requisitos → **RTM** ·
registro de contradicciones → **conflicts** · pool → **repo** · tablero →
**STATUS** (derivado) · criterio de muerte → **kill criteria** · Bloque Común →
**briefing** · cadena de trazabilidad → **chain of evidence** · caducidad →
**expiry**

*La trampa que esta gramática evita: en inglés un "brief" es la comisión, no el
resultado — por eso la comisión se llama **protocol** (más fuerte: implica
pre-registro) y el resultado es el **report**.*

---

## 14. Changelog y trazabilidad

### 14.1 v0.2 → v0.3

Insumo: retro de campo del framework v0.2 (12 puntos), benchmark contra fuentes
primarias, auditoría de nomenclatura del corpus, y las 6 lagunas de la sesión de
extracción del kit 0.1.0.

| Δ | Cambio | Ítem de Fase 2 |
|---|---|---|
| Δ1 | Nomenclatura: gramática de IDs sin semántica, prefijos como set cerrado, ancho y orden, gramática de conflictos unificada, enum en inglés con regla de activación, prueba del lector frío | 1 |
| Δ2 | Seis clases de fuente de evidencia con propiedad medallion; **documentación dura** como clase que jamás se borra; destilación declarada o deuda | 2 |
| Δ3 | Contrato de runs: `runs: N` + `mode: independent \| chained`, etiquetas `run-NN`, validación por modo al cerrar; `needs` como único canal | 3 |
| Δ4 | Política de MDs: record / evergreen / efímero, chat-primero, clase constitution, enforcement por clase sumado al de rutas | 4 |
| Δ5 | Estructura estándar de unidad; cero carpetas genéricas top-level nuevas | 5 |
| Δ6 | Frescura y recurrencia como dos capas de un mecanismo (`review_by` + `refresh:`); disparadores del proyecto; re-síntesis por supersesión | 6 |
| Δ7 | Reglas heredadas canonizadas: bitácora pre-registrada, namespaces de supersesión, precedencia del peso de evidencia, gates agrupables con registro, retro obligatoria | 7 |
| Δ8 | `context: clean-room \| scoped` con composición de payload por postura y guardas | 8 |
| Δ9 | Migración por capas con rastro obligatorio; sintonía como estado verificable | 9 |
| Δ10 | Resolución normativa de las 6 lagunas de la extracción (G1–G6) | 10 |

### 14.2 Qué se arrastró de la v0.2 sin cambio de fondo

Va **redactado dentro de este documento**, no por referencia: v0.3 es
autocontenida y ningún lector necesita abrir la v0.2.

| Contenido arrastrado | Dónde vive ahora | Enmiendas que recibió |
|---|---|---|
| Principios de operación (los 8) | §0.2 | madurez y volatilidad pasan al enum inglés (§1.6) |
| Rúbrica de calidad de fuente A–D, regla cruzada y regla de eco | §2.5 | ninguna |
| Estándar de artefactos y sus regímenes | §5 | se agrega `payload.md` como record sellado |
| Modelo de ejecución (readiness, canary, sesión, escritor único) | §10.1 | el encadenamiento pasa de nota a `mode: chained` (§3.2) |
| Pipelines `/inception`, `/launch`, `/close`, `/synthesis` | §10.2 | horizontes salen de la constitution (G4); briefing reemplaza a la constitution en el payload (G1); los raws aterrizan directo (G3) y toda ingesta clasifica en la puerta (§2.6) |
| Gates como datos, y su tabla | §11.1 | se agrega el gate de enmienda del bloque ratificado; todo gate deja fila en el registry de gates |
| Modo continuo declarado fuera de alcance | §11.3 | ninguna |

### 14.3 Enmiendas pre-gate (2026-08-19)

Ratificadas en conversación **antes** del gate y por eso integradas a esta misma
versión, sin bump (§"Cómo se lee y cómo se enmienda este documento"). Cada una
lleva su ítem con alternativa descartada en el acta (Sección B.4).

| Δ | Enmienda | Qué cambia | Secciones tocadas | Ítems del acta |
|---|---|---|---|---|
| Δ11 | **E1 — ingesta clasificada en la puerta; el `inbox` desaparece** | el único staging es externo al repo; toda ingesta declara **destino obligatorio** (unidad · clase sin unidad en `evidence/<class>/` · `hard-doc`) y pregunta ante ambigüedad; `inbox` sale de `paths` y de la guarda, que pasa a proteger las casas reales; el ingest-log queda idéntico; los `inbox/` legados son bronze congelado que `/migrate` reconcilia | §2.3, **§2.6 (nueva)**, §4.4, §5, §9.1, §10.2, §12 G3, §13.2 | B3 (ajustado), B24–B26 |
| Δ12 | **E2 — roster normativo de archivos repo-level** | tabla cerrada de todo archivo de nivel repo con rol, lector, momento de lectura y clase; archivo nuevo = enmienda de spec; regla de entrada (punteros delgados o vistas generadas, jamás segundas casas); constancias de `briefing.md` y `AGENTS.md` | **§4.5 (nueva)**, §5 | B27–B29 |
| Δ13 | **E3 — idioma de prosa como parámetro** | `language:` en la config; el framework sigue en inglés (nombres, enums, campos) y la prosa se escribe en el idioma declarado; una sola versión de cada skill, jamás copias traducidas; cambiar el idioma es migración; los renders para terceros son vistas derivadas fuera del KB | §0.1 #6, **§1.8 (nueva)**, §10.2, §12 G4, §13.1 | B30–B32 |

**Regla de auditoría del alcance:** todo párrafo normativo de v0.3 traza a la
tabla §14.1, a la §14.2 o a la §14.3. Si algo no traza a ninguna, es scope creep
y se borra.

---

### 14.4 Ratificación (2026-08-19)

**Gate humano consumado el 2026-08-19:** Sección A del acta confirmada (A1–A14)
y Sección B aprobada completa (B1–B32). Adjudicación tomada en el gate: la fila
del puntero externo de un `hard-doc` vive en el **ingest-log** (§2.3, §2.6) —
ya la escribía de facto, y no se crea un registry nuevo para una sola clase de
fila. `status:` sube a **ratified**; desde este acto rige el protocolo duro de
enmienda (§ "Cómo se lee y cómo se enmienda"): todo cambio posterior bumpea
`version:` y pasa por gate. La activación del tooling (enums, ingesta con
destino obligatorio, `language:`, enforcement de `context` y del bloque
ratificado) llega con el **kit 0.2.0**, migrando junto — jamás a medias.

---

# ACTA DE GATE — spec v0.3

*Esta acta es el gate. Está diseñada para resolverse **leyendo solo el acta**:
cada ítem trae qué se decide, la resolución propuesta y la alternativa
descartada. Ratificar el acta ratifica la spec; rechazar un ítem obliga a
enmendar la sección que lo implementa antes de subir `status:` a ratificada.*

*Actualizada el **2026-08-19** con las tres enmiendas pre-gate ratificadas en
conversación (§14.3): entran como **Sección B.4, ítems B24–B32**, y **B3 queda
ajustado** por la primera de ellas. No bumpean `version:` porque la spec aún no
está en vigor — se ratifican en este mismo acto, con el mismo estándar que todo
lo demás: resolución propuesta + alternativa descartada.*

## Sección A — Consolidación (ya pre-ratificado; solo confirmar)

Nada de esta sección es nuevo: son decisiones ya tomadas en conversación que la
spec convierte en texto normativo. Confirmar que el texto dice lo ratificado.

| # | Decisión ya ratificada | Dónde quedó normada |
|---|---|---|
| A1 | Enum de madurez y volatilidad **en inglés**: `established/supported/plausible/speculative` · `high/medium/low` | §1.6 |
| A2 | El enum entra **con el kit 0.2.0**, migrando parsers + plantillas + claves de `horizons` + corpus nuevo **juntos, jamás a medias** | §1.6, §9.4 |
| A3 | Etiquetas de run unificadas `run-01..run-NN`; `C1/C2`, `PI`, `S` quedan como vocabulario histórico con glosario | §3.1, §13.2 |
| A4 | Contrato de runs `runs: N` + `mode: independent \| chained` (default `independent`); `chained` = una unidad epistémica | §3 |
| A5 | Veredicto de IDs: llave estable + slug + índice; smart codes rechazados; `id_width` configurable, desborde crece, orden numérico, hex rechazado | §1.2, §1.4 |
| A6 | Gramática de conflictos unificada: `<unit>-conNN` local, `con-NN` registry; `CONTRA-*` y `K*` históricos | §1.5 |
| A7 | Prefijos = set cerrado por clase en config (`r`, `f`); extensión solo por config, con glosario | §1.3 |
| A8 | Migración por capas (principio #7): evergreen in-place · derivados regenerados · records de lectura por supersesión mecánica · **verbatim jamás** | §9.1 |
| A9 | Rastro de migración obligatorio: log del registry + sidecar; la incisión jamás dentro del verbatim | §9.2 |
| A10 | `context: clean-room \| scoped` como postura declarable por unidad | §8 |
| A11 | Documentación dura: jamás se borra, casa especial, puntero + sha256 + sidecar | §2.3 |
| A12 | Política de MDs en tres clases por mutabilidad + regla chat-primero | §4 |
| A13 | Nomenclatura en inglés para todo nombre de skill, comando, campo, operación y enum (principio #6) | §0.1, §1 |
| A14 | La spec vive en el kit y es la casa única de estas reglas | frontmatter, §0.1 #4 |

## Sección B — Decisiones nuevas de esta redacción (requieren ratificación)

Cada ítem: **decisión → resolución propuesta → alternativa descartada.**

### B.1 — Las seis lagunas de la extracción (G1–G6)

| # | Decisión | Resolución propuesta | Alternativa descartada |
|---|---|---|---|
| B1 | **G1 — casa del briefing.** ¿`plan:` es contrato o hace falta otro mecanismo? | **`plan:` ratificado como contrato**: el briefing es la Parte II del plan que comisiona la unidad; `/launch` lo resuelve por ese puntero y pregunta si falta (§12 G1) | Un `briefing.md` genérico top-level — un repo corre varios programas con briefings distintos: sería mentira o derivaría |
| B2 | **G2 — mecanismo de `context`.** | **Definido en §8**: campo en protocol, default en config (`scoped`), composición de payload por postura, tres guardas. Implementa el kit 0.2.0 | Dejar la fila como deuda sin mecanismo — perpetúa un campo que nadie sabe honrar |
| B3 | **G3 — dueño del tramo `inbox/` → `raw/`.** *(ajustado por E1: ver B24)* | **La ingesta aterriza directo**: `--unit <UNIT_ID> --run <N>` escribe en `<unit>/raw/run-NN.md`; `/close` solo verifica (§12 G3). La otra mitad de la resolución original —"el inbox sigue siendo la casa de todo lo demás"— **queda derogada por B24**: no hay tramo porque no hay bandeja | Que `/close` mueva desde el inbox — el inbox es record inmutable y la guarda rechaza mover/renombrar: exigiría debilitarla |
| B4 | **G4 — casa de los horizontes.** | **Valor en la config** (`horizons`, casa única); **autoridad en la constitution** vía **bloque ratificado** (`horizons`, `runs`, `ids`, `metrics`, `context`): cambiarlo exige enmienda con bump; los **disparadores** del proyecto siguen en la constitution (§12 G4) | (a) Solo constitution — el tooling leería de dos lados; (b) solo config — dejaría un número epistémico editable sin gate humano |
| B5 | **G5 — ancho de sub-IDs.** | **Ratificado: un solo `ids.width` gobierna todo**, con `adr-NNNN` como única excepción documentada (convención MADR) (§12 G5) | Ancho independiente por tipo de sub-ID — perilla por proyecto que nadie necesita |
| B6 | **G6 — registries append-only.** | **Tabla normativa de 9 registries** con tres regímenes: append-only (6), marcable (2), vista derivada (1) (§12 G6) | Dejarlo a la convención de cada encabezado — es exactamente el vacío que la laguna reporta |

### B.2 — Las seis decisiones de la sesión de extracción (kit 0.1.0)

| # | Decisión de la sesión | Resolución propuesta en texto normativo | Alternativa descartada |
|---|---|---|---|
| B7 | Enum español intacto y **fuera** de la config | **Ratificada**: el enum es contrato de spec, no perilla por proyecto; vive en el kit y jamás en la config (§1.6) | Enum configurable por proyecto — rompería la comparabilidad del corpus entre proyectos |
| B8 | Gramática de marks y columnas de la RTM **en inglés** | **Ratificada** (principio #6): nombres de campo, columnas y gramática de marks en inglés; la prosa del corpus sigue siendo la del proyecto (§0.1 #6, §1.1) | Columnas en español — híbrido que ya causó drift de esquema entre repos |
| B9 | Registries append-only **enumerados** | **Ratificada y ampliada**: la tabla de §12 G6 los enumera, y agrega `gates.md` que exige la retro #11 | Enumeración implícita en cada encabezado — no auditable |
| B10 | `kit_version` desincronizado = **error** de doctor | **Ratificada**: la desincronía es **error de integridad**, no advertencia; el repo no está sano hasta migrar (§9.3) | Advertencia — un repo a medias es precisamente lo que el principio #7 prohíbe |
| B11 | Sin dependencia de PyYAML (lector propio del subconjunto) | **Elevada a invariante de spec**: la guarda de integridad corre con git + Python estándar, sin el kit de skills ni paquetes externos; el subconjunto YAML del contrato es **escalares y listas inline** (§4.4) | Exigir PyYAML — ataría la guarda a un entorno con pip, y el hook debe correr en cualquier clon |
| B12 | `--lenient` conservado sin skill que lo invoque | **Ratificada**: estricto es la norma; lenient existe solo para el retro-parse de corpus artesanal del flujo de adopción, y todo cierre lenient anota su desviación (§10.2, `/close` paso 1) | Eliminar la flag — dejaría sin herramienta al flujo de adopción, que llega en Fase 3 |

### B.3 — Decisiones de redacción que la spec tuvo que tomar

| # | Decisión | Resolución propuesta | Alternativa descartada |
|---|---|---|---|
| B13 | **`constitution.md` NO se renombra a `governance.md`** pese a la letra de la retro #2 | Se conserva el nombre `constitution` para la gobernanza del repo; la ambigüedad se elimina nombrando **briefing** a la otra cosa | Renombrar a `governance.md` — costaría migración de config, tooling y corpus, y rompería la interoperabilidad declarada con la constitution del desarrollo dirigido por especificación |
| B14 | **La constitution completa deja de viajar en el payload** (amienda la v0.2) | Viaja el **briefing**; la constitution jamás viaja entera (§8.2) | Mantener la v0.2 — es la causa raíz documentada de la ambigüedad del término |
| B15 | **Significado del campo `constitution:`** del protocol | Sella la **versión de gobernanza vigente al lanzar** (procedencia). Lo que la unidad recibió lo evidencia el `payload.md` sellado; la postura la declara `context:` (§8.3) | Seguir usando `constitution: null` como marcador de sala limpia — sobrecarga un campo con dos significados |
| B16 | **Dos listas de principios** con el mismo nombre | Se renombran: **principios de diseño** (cómo se construye el framework) y **principios de operación** (cómo se trabaja bajo él) (§0) | Fusionarlas — gobiernan cosas distintas; fusionarlas perdería reglas |
| B17 | **Clase constitution** dentro de la política de MDs de tres clases | Es evergreen con protocolo de enmienda duro (bump + changelog + gate), no una cuarta clase (§4.3) | Declarar una cuarta clase — contradiría "tres clases por mutabilidad" del plan |
| B18 | **Nombre inglés de "documentación dura"** | **`hard-doc`** como valor de la clase de fuente (§2.1) | `permanent-doc`, `legal-doc` — menos abarcadores: la clase incluye archivos clave que no son legales |
| B19 | **Gramática de `refresh:`** | Cadencia corta `<N><w\|m\|y>` (p. ej. `18m`); la fecha se deriva de cadencia + último cierre (§6.2) | `refresh_by: <fecha>` — almacenaría un valor derivado, que se pudre (viola principio de operación #1) |
| B20 | **`clean-room` exige `needs: []`** | Una unidad que necesita findings ajenos no es sala limpia; la secuenciación no es un `need` (§8.3) | Permitir `needs` cuyos findings no viajen — `needs` significaría dos cosas según el contexto |
| B21 | **`gates.md` como registry nuevo** | Lo exige la retro #11 ("registro de qué gate se consumió cuándo"), hoy disperso en CLAUDE.md y changelogs (§7.4, §12 G6) | Seguir sin registro — el rastro disperso es el síntoma reportado |
| B22 | **`adr-NNNN` mantiene ancho 4** fuera de `ids.width` | Única excepción documentada, por convención MADR externa (§1.5) | Forzar `adr-NN` bajo `ids.width` — rompería la convención MADR con la que interopera |
| B23 | **Alcance de v0.3 = v0.2 arrastrada + los 10 ítems** *(ampliado por las enmiendas pre-gate: ver §14.3)* | La spec es autocontenida y toda regla traza a §14.1, §14.2 o §14.3 | Redactar v0.3 como delta sobre v0.2 — no sería una constitution: obligaría a leer dos documentos |

### B.4 — Enmiendas pre-gate ratificadas en conversación (2026-08-19)

Tres enmiendas entraron **antes** de este gate, a la misma versión y con el mismo
estándar de acta. Se agrupan por enmienda; §14.3 las traza a las secciones.

**E1 — Ingesta clasificada en la puerta; el inbox desaparece.**

| # | Decisión | Resolución propuesta | Alternativa descartada |
|---|---|---|---|
| B24 | **¿Existe una bandeja de entrada dentro del repo?** | **No.** El único staging es **externo** (la carpeta de descargas del humano) y se vacía solo tras ingesta verificada contra el remoto; `inbox/` deja de existir como ruta, como casa y como concepto (§2.6) | Conservar el inbox "para todo lo que no es un run" — es una casa sin dueño que reproduce el tramo huérfano que G3 reportó: toda llegada es atendida, así que nada tiene por qué esperar adentro |
| B25 | **¿Qué exige la ingesta al recibir material?** | **Destino obligatorio, tres formas:** unidad (`<unit>/raw/`) · clase sin unidad (`<research>/evidence/<class>/` con sidecar de procedencia) · `hard-doc` (su casa especial, §2.3). **Ante ambigüedad pregunta y no avanza**; el ingest-log queda idéntico (§2.6) | Un destino por defecto (`evidence/misc/`, o la vieja bandeja) para no frenar la operación — adivinar la casa es exactamente el drift que el destino obligatorio existe para impedir |
| B26 | **Qué pasa con `paths`, la guarda y los inbox que ya existen.** | `inbox` **sale de `paths`**; entran `evidence` y `hard_docs` como casas declaradas; **la protección de rutas pasa a las casas reales** (§4.4, §5). Los `inbox/` de proyectos adoptados son **legado congelado** —bronze que se lee y jamás se reescribe— y `/migrate` los reconcilia moviendo, nunca editando (§2.6, §9.1) | (a) Dejar `inbox` en `paths` como ruta protegida vacía — casa fantasma en el contrato; (b) borrar los inbox legados al adoptar — destruiría bronze, que es justamente lo que jamás se toca |

**E2 — Roster normativo de archivos repo-level.**

| # | Decisión | Resolución propuesta | Alternativa descartada |
|---|---|---|---|
| B27 | **¿Qué archivos de nivel repo reconoce el framework?** | **Tabla cerrada** (§4.5) con rol, lector, momento de lectura y clase de cada uno: `README.md`, `CLAUDE.md`, `framework.config.yaml`, `constitution.md`, los registries y `STATUS.md`, el índice generado, y la `SPEC.md` del kit. **Un archivo repo-level nuevo exige enmienda de esta spec**, como los prefijos exigen config + glosario | Dejarlo a la convención de cada repo — es el mismo vacío que G6 reportó para los registries, un nivel más arriba: nadie sabe qué archivo es legítimo ni quién lo lee |
| B28 | **Qué puede contener un archivo de entrada.** | **El conocimiento vive UNA vez:** `README.md`, `CLAUDE.md` y el índice son **punteros delgados o vistas generadas**, jamás segundas casas. Prueba: si se borran, no se pierde ninguna regla — solo el atajo (§4.5) | Permitir que el archivo de entrada resuma las reglas "para comodidad del lector" — un resumen es una copia que deriva en silencio (principio de diseño #4) |
| B29 | **Dos archivos que la gente espera encontrar y no existen.** | **`briefing.md` no existe** (el briefing es la Parte II del plan, B1/§12 G1) y **`AGENTS.md` no es parte del framework**: si un harness lo exige, se **genera** desde la misma fuente que `CLAUDE.md` (§4.5) | Redactar `AGENTS.md` a mano junto a `CLAUDE.md` — dos archivos de instrucciones escritos por separado divergen; es la segunda casa con otro nombre |

**E3 — Idioma de prosa como parámetro.**

| # | Decisión | Resolución propuesta | Alternativa descartada |
|---|---|---|---|
| B30 | **¿En qué idioma se escribe lo que el framework produce?** | **`language:` en la config** (§1.8): el framework es inglés —nombres, comandos, campos, enums, etiquetas, columnas— y la **prosa** de salidas y plantillas se escribe en el idioma declarado del proyecto | (a) Todo en inglés, incluida la prosa — obligaría a un corpus en un idioma que el equipo no habla, y la evidencia se lee, no se decora; (b) idioma implícito por convención — es como nacieron los híbridos que el principio #6 vino a matar |
| B31 | **¿Cómo soporta una skill dos idiomas?** | **Una sola versión de cada skill y plantilla** (nombres y mecánica en inglés) que escribe su prosa en el idioma configurado; **jamás copias traducidas**. Los renderizados para terceros (PDF, deck) son **vistas derivadas fuera del KB** (§1.8) | Skills o plantillas duplicadas por idioma — dos casas del mismo contrato que divergen al primer cambio (principio de diseño #4) |
| B32 | **¿Dónde vive `language` y qué cuesta cambiarlo?** | **Config operativa**, fuera del bloque ratificado —no porta autoridad epistémica (§12, G4)—, pero **cambiarlo tras el primer artefacto es migración** (§9), no edición: evergreen se actualiza, los derivados se regeneran y **los records no se reescriben** (§1.8) | (a) Meterlo al bloque ratificado — cargaría el gate humano con una perilla de forma; (b) tratarlo como edición libre — implicaría reescribir records para "dejar el repo uniforme", que es falsificar evidencia |

---

## Preguntas al final (NO redactadas en la spec)

*Cosas que la redacción encontró y que **no** entraron al texto normativo por no
estar en la agenda de la Fase 2. Se anotan, no se deciden.*

1. **Índice puerta-de-entrada.** §1.2 se apoya en él para la experiencia de
   "saber sin abrir", pero su generación es Fase 3.2. Hasta que exista, la regla
   de prosa `rNN (slug-corto)` carga sola con ese peso.
2. **Registries como datos** (YAML/JSON con schema + vistas generadas) es Fase
   3.2. La tabla de §12 G6 norma el **régimen** de cada registry, no su formato:
   cuando el formato cambie, el régimen no debería cambiar.
3. **`/migrate` y el cron de recurrencia** son Fase 3.5 y 3.3. §6.2 define el
   primitivo `refresh:` pero nada lo dispara todavía; §9 define los pases pero
   quien los ejecuta llega después.
4. **Skill de destilación** para el bronze no investigativo (§2.4 la nombra como
   la que salda la deuda) es Fase 3.4.
5. **Los tres flujos de entrada** (`/inception`, `/adopt`, `/normalize`) son
   Fase 3.1. §10.2 redacta `/inception` porque venía de la v0.2; los otros dos
   **no se redactaron**, y por eso §10.2 los nombra como "flujo de adopción,
   fuera del alcance de v0.3" en vez de definirlos.
6. **Quién ejecuta el chequeo del bloque ratificado** (§12, G4) y el del
   `context` (§12, G2). La spec declara la regla; el kit 0.2.0 la implementa
   junto con la migración del enum. Si el gate humano rechaza esa resolución, el
   trabajo de 0.2.0 cambia — por eso conviene resolverla antes del bump.

*Agregadas por las enmiendas pre-gate del 2026-08-19:*

7. **Reconciliación de los `inbox/` legados** (§2.6). La asigna `/migrate`, que
   es Fase 3.5. Hasta que exista, un repo adoptado convive con su bandeja
   congelada: se lee como bronze, se cita, y no recibe nada nuevo.
8. **Generación de `AGENTS.md`** desde la misma fuente que `CLAUDE.md` (§4.5).
   La spec fija la regla — el generador no existe todavía, así que hasta que
   exista el archivo simplemente no se crea.
9. **Dónde se registra el puntero de un `hard-doc` que vive fuera del repo.**
   §2.3 exige puntero + `sha256` + sidecar "en el registry", pero ningún
   registry de la tabla de §12 G6 se declara dueño de esa fila; hoy la deja el
   log de ingesta, que es donde `--keep` la escribe. Se anota: normar el dueño
   explícito es enmienda, no redacción.
