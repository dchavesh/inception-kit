---
id: inception-framework-spec
type: constitution
version: 0.4
status: proposed — pendiente de ratificación humana
date: 2026-08-20
supersedes: inception-framework-v0.3
home: inception-kit (este repo)
consumer: toda sesión, humano o script que opere bajo el inception-framework
reading-moment: antes de crear, cerrar o migrar cualquier artefacto del framework
---

# Inception Framework — spec v0.4

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
registra en la tabla de enmiendas pre-gate de la versión en curso y se agrega
como ítem con alternativa descartada al acta. Ratificado el acta, la versión
queda congelada y todo cambio posterior vuelve al protocolo duro.

**Esa regla no es privativa de esta spec.** Es la regla de la **clase
constitution**, y por eso desde la v0.4 vive en §4.3 y gobierna también la
`constitution.md` de un proyecto: mientras su `status:` es `draft` o `proposed`
no hay nada vigente que superar, y ratificarla entra a su propia v1.

**Qué es v0.4.** Esta versión supersede a la v0.3 y la reemplaza como
constitution vigente: es autocontenida, y ningún lector necesita la v0.3 para
operar. Se construyó bajo una regla dura de alcance: **v0.4 = v0.3 ratificada
arrastrada sin cambio + los 10 ítems del batch v0.4 del plan de mejoras vigente**
— ocho enmiendas encoladas por las sesiones de implementación, la canonización de
los cuatro flujos que el kit 0.4.0 ya implementa, y las adjudicaciones de tooling
ya aceptadas. Todo párrafo normativo de este documento traza a §14.1, §14.2,
§14.3 o §14.5; las tablas de trazabilidad de §14 lo hacen auditable. Nada nació
por iniciativa del redactor: **la agenda es cerrada**, y lo que la redacción
encontró fuera de ella se anota en el acta, no se escribe acá.

**Qué NO es v0.4.** No es un rediseño. Los cuatro flujos que §10.2 canoniza
existen, están implementados en el kit 0.4.0 y están validados: la spec
**describe la práctica**, no la propone. Donde la letra y la práctica divergen,
eso es una laguna declarada en el acta — jamás una mejora colada por la puerta de
atrás.

**Estado.** `proposed`. Esta spec **no está en vigor** hasta que el humano
ratifique el ACTA DE GATE del final; hasta entonces rige la v0.3. Las reglas que
exigen migración de tooling declaran además su **regla de activación** (§1.6,
§9.4): la spec declara, el kit implementa después.

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

**La casa de cada capa.** El bronze tiene dos casas posibles según §2.6 —
`<unit>/raw/` cuando pertenece a una unidad, `<research>/evidence/<class>/`
cuando tiene clase pero no pertenece a ninguna—; **el silver y el gold tienen
una sola: la carpeta de una unidad** (`01-report.md` y `02-findings.md`, §5).
No existe un silver fuera de una unidad, porque no existe un `02-findings` fuera
de una unidad (principio de diseño #5).

**Destilar bronze sin unidad no lo muda de casa.** Cuando lo que se destila vive
en `evidence/<class>/`, **una unidad aloja la destilación** — cuál, lo decide el
humano, porque elegirla es juicio— y el bronze **se queda donde está**: la unidad
lo cita por **ruta y `sha256`**, no se lo lleva. Mover ese bronze a `raw/` es una
operación distinta, es opt-in del humano y es de la migración por capas (§9.1);
la destilación jamás la dispara sola. Así el material que sirve a más de una
unidad no necesita duplicarse ni elegir dueño, y el `sha256` que lo hace
auditable sigue apuntando a un único archivo.

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

**El protocolo duro gobierna un documento EN VIGOR.** Mientras el `status:` de
una constitution es `draft` o `proposed`, el documento todavía es **la propuesta
que el gate va a ratificar**: editarlo —**incluido ratificarlo**— entra a esa
misma versión y **no la bumpea, porque no hay nada vigente que superar**.
Consumido el gate, la versión queda congelada y todo cambio posterior vuelve al
protocolo duro. La regla vale para las dos constitutions de la clase: esta spec
la aplica sobre sí misma (§"Cómo se lee y cómo se enmienda este documento") y la
`constitution.md` de un proyecto la aplica sobre su v1.

Corolario sobre el **bloque ratificado** de la config (§12, G4): pre-gate, esos
valores **se ratifican CON la constitution** en el mismo acto, así que cambiarlos
mientras el documento no está en vigor tampoco exige bump. El gate que los
ratifica es el mismo que ratifica el borrador.

**La regla falla del lado seguro.** Si la constitution todavía no existe en el
historial, no hay nada vigente que superar. Si existe y **no declara `status:`**,
se la trata como **vigente** y rige el protocolo duro: la ausencia de declaración
jamás compra una excepción.

*Por qué está escrito:* sin esta regla, ratificar una v1 exige inventar una v2
que nunca existió — el flujo de entrada de un proyecto nuevo (§10.2,
`/inception`) no puede cerrar su primer gate.

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
| documento de **plan** | la comisión de un conjunto de unidades: mapa (Parte I) + **briefing** (Parte II) + una sección por unidad (Parte III). Lo apunta el campo `plan:` del protocol (§12, G1) | el coordinador al comisionar y al lanzar; el humano en el gate del mapa | al ratificar el mapa y al armar cada payload | **record** — fechado y no editable: la comisión que se ratificó no cambia después. Un plan nuevo supersede al anterior (§0.2 #2) |
| `<registry>/data/*` | **los datos** de los ocho registries que son record (metrics, ingest-log, supersessions, migrations, qa-audits, gates, requirements, conflicts) | los scripts del kit; la auditoría | al escribir una fila, al renderizar y al auditar | **record** — régimen por registry **según §12, G6**: append-only o marcable. Es la fuente; se escribe solo por la puerta del kit, jamás a mano. La casa la norma esta spec; el formato lo elige el kit (§12, G6) |
| `<registry>/*.md` | **la vista** de cada uno de esos ocho registries, renderizada desde sus datos | coordinador, síntesis, auditoría, humano | al cerrar, citar o auditar | **vista derivada** — regenerable, jamás editada a mano, jamás autoritativa (§12, G6) |
| `<registry>/STATUS.md` | tablero de estado del programa; el noveno registry y el único sin datos propios | humano y coordinador | al planificar y al lanzar | **vista derivada** — deriva de los protocols; jamás editada a mano, jamás autoritativa (§12, G6) |
| `INDEX.md` (raíz) | el **índice puerta-de-entrada**: `id → slug → objetivo en una línea → status`, más decisiones vigentes, conflictos abiertos, síntesis vigente y dónde vive cada clase de cosa (§1.2) | quien necesita saber sin abrir cada unidad | al orientarse en el corpus | **vista derivada generada** — la genera el kit; **puntero delgado**: ninguna regla vive ahí |
| `LICENSE` · `NOTICE` · `CITATION.cff` (raíz) | los archivos que **exige el ecosistema**, no el framework: términos de uso, atribuciones y forma de citar el repo | quien consume, redistribuye o cita el repo desde afuera | antes de reutilizar o citar | evergreen — **fuera del KB**: no portan reglas del framework, no son citables como evidencia y ninguna capa de la cadena de evidencia los recorre |
| `SPEC.md` (en el kit) | esta spec: la constitution del framework | toda sesión, humano o script que opere bajo el framework | antes de crear, cerrar o migrar cualquier artefacto | evergreen **clase constitution**; **vive en el kit y en ningún repo consumidor** — un repo la referencia por la versión de kit que declara su config |

Los archivos de una unidad (`00-protocol`, `payload`, `raw/`, `01-report`,
`02-findings`, `03-sources`) no son repo-level: los norma §5, y por diseño viven
dentro de la carpeta de su unidad (principio de diseño #5).

Tampoco entra el **tooling que el kit instala** —las skills vendorizadas, el hook
de integridad y su shim—: es maquinaria versionada por el kit, no conocimiento
del repo. No aloja reglas, se reemplaza en cada bump, y por eso ni ocupa fila ni
abre la taxonomía. Lo mismo vale para los archivos de configuración de
herramientas ajenas (`.gitignore`, `.editorconfig` y sus pares): son del entorno,
no del framework.

**Por qué los archivos del ecosistema ocupan fila y no una excepción.** `LICENSE`,
`NOTICE` y `CITATION.cff` no los pide el framework: los pide el mundo donde el
repo vive, y aparecen en su raíz sin que ninguna regla de esta spec los haya
convocado. Con la taxonomía cerrada, un archivo sin fila es una violación — así
que un repo que hace lo correcto legalmente quedaría en falta con su propia
constitution. La fila resuelve las dos mitades: **existen legítimamente** y
**están fuera del KB**. No son records de nada, no entran a la cadena de
evidencia, no se citan como fuente, y el ciclo de vida de borrado no los alcanza
porque su dueño no es el framework. La lista de la fila es **ilustrativa de la
categoría, no exhaustiva**: lo que la define es el criterio —exigido por el
ecosistema, sin regla del framework adentro—, y un archivo que pretenda entrar
por esta puerta portando reglas del repo no es un archivo del ecosistema: es una
segunda casa con disfraz.

**Por qué el documento de plan es record.** Es la comisión que un gate humano
ratificó, y el `plan:` de cada protocol la apunta como procedencia de lo que esa
unidad recibió (§12, G1): editarlo después cambiaría, retroactivamente, el sobre
que una sesión ya abrió. Comisionar de nuevo es **un plan nuevo que supersede al
anterior**, con su fila (§0.2 #2) — jamás una edición del que ya comisionó.

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
(`README.md`, `CLAUDE.md`, `INDEX.md`) son **punteros delgados o vistas
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

#### Quién verifica el roster

La spec **norma** el roster; verificarlo —archivo repo-level fuera de la tabla,
archivo de entrada engordado a segunda casa— **no es trabajo del chequeo de
integridad**, y esa asimetría es deliberada (adjudicada el 2026-08-19). El
chequeo corre en cada push y tiene que poder fallar sin ambigüedad: censar la
raíz lo obligaría a asumir filas que esta tabla no declara, y clasificar un
documento suelto es juicio. Por eso **el chequeo de integridad censa solo el
registry**, y el censo de la raíz y de `<research>/` vive en el flujo de
normalización (§10.2, `/normalize`), que **propone y pide gate humano** con un
humano mirando. La prueba del puntero delgado se **mide** ahí mismo: una línea
de un archivo de entrada que también vive en la constitution o en la config es
una segunda casa.

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
├── 03-sources.md           bitácora de búsqueda
└── retro-lenient-deviations.md   record — solo si el cierre fue lenient (§10.2)
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
| `retro-lenient-deviations.md` | — | record | **solo en un cierre lenient** (§10.2, `/close` paso 1): la lista completa de lo que no validó, **tal cual la imprimió la validación** —sin resumir y sin maquillar—, y por qué se acepta |

Los reports y findings llevan frontmatter mínimo: `id`, `unit`, `date`.

- Las versiones por supersesión (`01-report.v2.md`, …) viven **en la misma
  carpeta**, junto al record que superan. La versión vigente es la de mayor
  `.vN`, o la base si no hay ninguna.
- El bronze no textual vive en `raw/` como cualquier otro bronze, con su
  sidecar al lado (§2.2).
- **El silver y el gold de un bronze sin unidad viven acá también** (§2.2): la
  unidad que aloja la destilación es su casa, y el bronze se queda en
  `evidence/<class>/` citado por ruta y `sha256`.
- **El repo no crea carpetas genéricas top-level nuevas.** Los nombres son
  inequívocos entre proyectos que comparten el framework: nada que se llame
  `payloads/`, `docs-varios/` o similar.

**Taxonomía cerrada, igual que §4.5 un nivel más arriba.** La tabla de arriba es
el **set completo** de lo que puede vivir en la carpeta de una unidad, contando
sus versiones por supersesión (`<archivo>.vN.md`) y el contenido de `raw/`
(verbatim de corridas, bronze binario y sus sidecares). Un archivo que no
corresponde a ninguna fila **no es "una excepción"**: o se mueve a la casa que le
toca, o entra por enmienda de esta spec con su fila declarada — es la misma
prueba que §4.5 aplica a la raíz, y el flujo de normalización la trata como
violación.

*Por qué `retro-lenient-deviations.md` ocupa fila y no un comentario.* Es la
constancia de que un cierre bajó sus errores a advertencias, y el consumidor es
quien lea después ese report: sin fila, la desviación viviría como prosa dentro
de un record —que no se edita— o como memoria de la sesión —que no existe—. Vive
en la carpeta de la unidad porque es de ella (principio de diseño #5), y declara
lo que §4.2 le exige a todo archivo: `class`, `consumer`, `reading-moment`,
`date`. El nombre va en inglés como todo nombre del framework; el cuerpo, en
`language` (§1.8).

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

**Reubicar no es reescribir.** Llevar un `inbox/` legado —o cualquier bronze sin
casa— a las casas reales (§2.6) mueve archivos sin tocar su contenido: el
`sha256` de cada uno sigue siendo el mismo, que es justamente lo que hace
verificable el pase. Es opt-in del humano como cualquier otro y **no habilita
ninguna edición del verbatim**.

**La reubicación es contrato de esta sección, no una excepción que el tooling
concede.** La guarda de integridad (§4.4) la acepta **solo** si se cumplen las
tres condiciones, juntas y verificables sin juicio:

1. **Contenido byte a byte idéntico.** El objeto que sale y el que entra son el
   mismo: un movimiento con cambios no es una reubicación, es una reescritura de
   record, y se rechaza como tal.
2. **Destino en otra casa protegida.** Un record no sale del régimen de record.
   Mover verbatim a una ruta desprotegida sería sacarlo del contrato por la
   puerta de atrás, así que el destino tiene que estar bajo las mismas rutas que
   §4.4 protege.
3. **Rastro en el MISMO commit.** La entrada en el log de migraciones (§9.2)
   viaja con el movimiento. Sin rastro no hay pase: un record que aparece en otra
   ruta sin explicación es indistinguible de una manipulación.

**Que falte una sola, y no es reubicación.** Escritas acá y no en el código,
ningún tooling futuro puede aflojarlas sin enmendar esta spec — que es
exactamente lo que se busca: la excepción que se concede una vez, se concede
siempre.

*Constancia: esto no contradice §12 G3.* La ingesta sigue aterrizando directo en
la casa de destino, y el cierre sigue sin mover nada. La reubicación no es un
tramo del flujo normal: es una operación de **migración**, sobre legado, con
opt-in humano y con las tres condiciones encima.

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

#### Las tres entradas — y no hay más

Un proyecto entra al framework por **exactamente una** de tres puertas, según en
qué estado está lo que ya existe:

| Entrada | Estado de partida | Qué produce |
|---|---|---|
| **`/inception`** | una idea, y nada más | repo sembrado, constitution ratificada y unidades preliminares en `pending` |
| **`/adopt`** | investigación que **ya se hizo** y nunca tuvo repo | ese corpus adentro del framework, con sus huecos declarados |
| **`/normalize`** | un repo que **ya existe**, con documentación | ese repo en el formato vigente, con retención declarada |

**El set es cerrado**, y esa es una decisión de diseño, no una casualidad de
implementación: **un edge case no se le agrega al framework — se normaliza hacia
él** (principio de diseño #1). Las tres puertas son pipelines de normalización:
toman el proyecto en el estado en que esté y lo llevan al estado que esta spec
dicta. Una cuarta puerta sería un dialecto de entrada, y un dialecto de entrada
produce un repo que solo se parece a los demás.

**Cada puerta reconoce cuándo no es la suya y deriva.** Si al arrancar aparece
que el estado de partida es otro —hay corpus donde se esperaba una idea, hay un
repo donde se esperaba una carpeta suelta—, el flujo lo dice y manda al que
corresponde, en vez de estirarse para cubrirlo.

Tres invariantes gobiernan las tres, y ninguna es negociable:

- **Ninguna porta lógica de negocio.** Las preguntas de un flujo de entrada son
  generadoras y aclaradoras, y son **las mismas cualquiera sea la idea**: no
  traen hipótesis, no sugieren mercados, no proponen arquitecturas (principio de
  diseño #2).
- **Ninguna congela ni lanza.** Congelar un protocol y lanzar una unidad son
  órdenes humanas, y siguen siéndolo después de cualquier entrada.
- **Ninguna elige por el humano.** Ni una clase dudosa, ni cuál versión es la
  vigente, ni un borrado, ni un número que falta: **se pregunta**, y un default
  inventado por el flujo es lógica de negocio contrabandeada. Lo que el humano no
  confirmó, no entra.

**El idioma se fija al principio o no se fija.** Los dos flujos que **crean** el
primer artefacto —`/inception` y `/adopt`— confirman `language` antes de
escribirlo (§1.8). El que entra a un repo que **ya tiene prosa** no lo elige:
ahí el idioma ya está, y cambiarlo es migración por capas encadenada después
(§9), jamás parte de normalizar.

**`/inception`** — de idea cruda a programa listo para congelar.

1. **Elicitación** sobre la idea, por vaga que sea, con preguntas indiferentes
   al dominio: qué decisión depende de esto y quién la toma; qué está dado y qué
   está en disputa; **qué haría que la idea no valga la pena** —son los kill
   criteria y se **pre-registran acá**, porque un kill criterion inventado al
   cerrar no es un kill criterion—; dominio y restricciones; techo de gasto y
   umbrales de QA; disparadores propios (§6.3); y qué **no** es esto. Lo
   entendido se devuelve y **se pide corrección**: una elicitación que el humano
   no corrigió es una elicitación que nadie leyó.
2. **Confirmar `language`** y declararlo en la config (§1.8), antes de escribir
   el primer artefacto.
3. **Sembrar el repo**: scripteado, determinista, aburrido a propósito e
   idempotente. Siembra la config ancla, las casas de §5, los registries de
   §12 G6 y la guarda de integridad. Los valores del **bloque ratificado**
   quedan con los defaults del kit — el humano los ratifica, o los cambia, en el
   gate del paso siguiente (§12, G4).
4. Redactar la **constitution** del proyecto: supuestos refutables, dominio,
   techo de gasto, umbrales de QA, disparadores (§6.3) y jerarquía de
   independencia. Se emite como **v1, en borrador**, con changelog de enmiendas
   vacío, estructurada para ser compatible con la constitution del desarrollo
   dirigido por especificación que la síntesis sembrará. Los horizontes de
   caducidad **no se escriben acá**: viven en el bloque ratificado de la config y
   la constitution los apunta (§12, G4). **Neutral quiere decir sin la semilla:**
   la constitution gobierna el repo, no contiene la tesis ni la respuesta
   esperada, porque lo que gobierna tiene que sobrevivir a que la idea se caiga.
   **Gate: el humano ratifica el borrador *y* los valores del bloque ratificado
   tal como están** — pre-gate se ratifican juntos, y por eso ese acto no bumpea
   nada (§4.3).
5. **Unidades preliminares** con la convención de fase de §1.3 (`X00` más sufijo:
   `r00a`, `r00b`, …). Su objetivo es uno solo, y es el que hace de esta fase una
   fase: **validar la idea — continuar, pivotar o descartar**; cada una lleva por
   eso kill criteria que resuelven a una de esas tres salidas. Nacen
   **`clean-room`**: son exploración y son sensibles a falsificación, así que
   exigen `needs: []` (§8.3). El programa (`X01+`) **no se planifica todavía**:
   se planifica cuando las preliminares hayan hablado.
   **Anti-sprawl:** ninguna unidad sin un objetivo que cambie una decisión
   concreta — si un documento existente ya responde la pregunta, no es una
   unidad: es una fuente, y entra por la ingesta (§2.6).
6. Redactar el **mapa** (unidades, objetivos, fuera de alcance, `needs`, kill
   criteria) y el **briefing** del programa como Parte II del plan (§12, G1;
   §4.5 le declara su fila). Es la mecánica del flujo de planificación, y vive
   ahí: `/inception` la delega, no la duplica. **Gate: el humano ratifica — acá
   es donde el juicio humano se gana el sueldo.**
7. Cerrar: regenerar los derivados, correr el chequeo de integridad y entregar
   al humano qué unidades quedaron en `pending`, qué decide cada una y **los
   gates pendientes en orden**. El freeze es la orden siguiente, y es suya.

**`/adopt`** — investigación que ya se hizo, traída al framework.

**La regla que gobierna todo el flujo: una adopción jamás mejora el pasado.** No
completa una bitácora de memoria, no inventa un kill criterion que nadie
pre-registró, no sube una madurez porque el texto suene seguro. Lo que falta se
declara como limitación: **una ausencia documentada es evidencia; una consulta
inventada es contaminación** (§7.1).

1. **Inventario del corpus, antes de escribir un archivo**: qué corridas hubo y
   qué produjo cada una; si se conserva el **verbatim** de cada una (sin
   verbatim no hay bronze, y sin bronze la afirmación no es auditable); si alguna
   corrida vio el resultado de otra; si hay versiones del mismo documento
   conviviendo; qué material es documentación dura (§2.3); y en qué idioma está
   escrito el corpus. Se devuelve en una tabla y **se pide corrección**.
2. **Sembrar el repo y declarar el idioma** con el que el corpus **ya está
   escrito**: adoptar **no traduce** (§1.8).
3. **El verbatim entra por la puerta, con destino declarado** (§2.6), y ante
   ambigüedad la ingesta se detiene y pregunta.
   *Costura declarada — de dónde sale la procedencia.* El log de ingesta registra
   **llegadas**: fecha, origen externo y desenlace del original. Para lo que
   efectivamente llega de afuera, la fila nace ahí por construcción. Para el
   material que **ya vivía dentro del repo no hubo llegada**, y llenar esas
   columnas sería inventar una ingesta que no ocurrió — eso se **reubica** (§9.1),
   y reubicar no es ingerir. La procedencia del corpus adoptado queda entonces en
   tres casas que ya existen, y **la adopción no abre ninguna nueva**: el log de
   ingesta, el log de migraciones y el sidecar de cada record adoptado.
4. **Protocols retroactivos.** Un protocol reconstruido **describe la comisión
   que la corrida efectivamente tuvo**, no la que hubiera sido correcta, y lleva
   en el cuerpo su marca de reconstrucción con la fecha y la evidencia de la que
   salió. `runs:` es **cuántas corridas hubo** —si hubo una, es `1`: jamás se
   completa investigando de más para llegar al default (§3.3)— y `mode:` es lo
   que pasó. **Los kill criteria que no existieron se declaran vacíos:** es
   perfectamente legal y es la verdad; inventarlos es lo que no lo es. El `plan:`
   apunta al documento de plan si existe; si no existe, se redacta uno mínimo con
   el briefing real que la sesión recibió, o **se declara que no hubo briefing**,
   que también es un hecho.
5. **Jerarquía de independencia, declarada y no supuesta**: qué corrida fue
   réplica ciega y cuál compartió contexto. **El pecado no es el contexto: es el
   contexto no declarado** (§3.2). Un conjunto `chained` cuenta como **UNA**
   unidad epistémica y su replicación se declara `n/a` — jamás se le acredita
   convergencia a dos corridas que se leyeron entre sí. La jerarquía va a la
   constitution: es la que la síntesis aplicará.
6. **Cierre retro-lenient — el único lugar donde vive el modo lenient**, y
   siempre anotado. El corpus artesanal no fue escrito contra la plantilla, así
   que no la va a pasar. La desviación se anota por escrito en tres lugares y la
   anotación **es parte del cierre**, no un comentario: el record
   `<unit>/retro-lenient-deviations.md` (§5), la fila del gate de QA, y la
   anotación en el **sidecar** del verbatim adoptado (§9.2). **Lo lenient no lava
   nada:** una afirmación sin fuente sigue siendo `speculative` por definición y
   ninguna etiqueta sube porque el cierre haya sido tolerante. El resto del cierre
   corre igual que en `/close`.
7. **Adjudicar vigentes y dejar la supersesión preparada.** Si el corpus trae
   versiones del mismo documento conviviendo, **el vigente lo elige el humano** —
   ningún mecanismo elige solo—, y cada versión no vigente deja su fila de
   supersesión: el corpus solo-vigente es precondición estructural del payload
   (§8.3). Adoptado el corpus, cada record vigente queda como **base de su
   familia**, sin `.vN`, con su sidecar declarando que es corpus artesanal
   adoptado y que se lee con el glosario de §13.2 — de modo que cuando la primera
   investigación nueva lo supere, superarlo sea mecánico.
8. Cerrar. **La retro es obligatoria** (§7.5).

**`/normalize`** — el repo que ya existe, llevado al formato vigente.

**Nada se borra sin confirmación explícita, y la confirmación se pide con el
inventario a la vista.** La adjudicación de qué está vigente es **gate humano
siempre**.

1. **Inventario read-only, primero y completo.** No escribe un solo archivo, y
   **describe sin clasificar ni adjudicar**: qué archivo repo-level está en el
   roster §4.5 y cuál está fuera; qué archivo de entrada **engordó** hasta
   albergar reglas de otra casa (la prueba del puntero delgado, medida); qué
   documentos hay que clasificar; qué **monolitos** concentran el eco; qué
   **épocas conviven como carpetas**; qué **familias de versión** no tienen
   vigente declarado; qué queda **huérfano** —lo que nadie enlaza, ni desde los
   findings ni desde el registry—; y qué es **higiene operativa** —entornos,
   cachés, salida de build—, que **se nombra y no se toca**: normalizar
   documentación no es limpiar el entorno. El inventario se reporta **tal cual**,
   sin resumirlo.
2. **Clasificar**: cada documento en **exactamente una** clase de §4.1 —record,
   evergreen, efímero— o como `hard-doc` (§2.3), preguntando ante duda. Un
   documento sin consumidor ni momento de lectura declarados no es un documento:
   es chat que se solidificó (§4.2).
3. **Triturar los monolitos.** Un archivo append-heavy que ningún agente puede
   dejar de leer es **eco por frecuencia en su forma pura** (§8): la corrección
   se agrega al final y el texto viejo sigue ahí, pesando. El triturado usa dos
   mecanismos que ya existen: lo **vigente** sale como filas de registry y
   records individuales —cada decisión a su ADR, cada requisito a la RTM, cada
   conflicto a su fila—, y el **original queda congelado EN SU LUGAR**, declarado
   como ruta inmutable extra. No se mueve, no se edita, no pierde un byte: sale
   del contexto de lectura porque ya nada lo apunta, no porque se lo haya tocado.
4. **Adjudicar vigentes — GATE HUMANO, sin excepción.** Las familias de versión y
   las épocas conviviendo se resuelven eligiendo **una** vigente por concepto, y
   esa elección **no la toma el flujo**: ante tres arquitecturas simultáneas
   ningún mecanismo elige solo. Cada versión superada deja su fila de supersesión
   y su anotación de sidecar.
5. **Retención declarada y borrado.** Un borrado sin retención declarada es una
   pérdida, no una normalización: se declara **qué se retira, por qué ya no
   aplica y dónde vive lo que lo reemplaza**. Un evergreen muerto **se BORRA, no
   se archiva** (§4.1): el historial ya vive en git, y una carpeta de archivo es
   una época más conviviendo en el contexto de todo agente que lea la carpeta
   padre. **Tres cosas este flujo no borra nunca, y se planta antes de
   proponerlas:** la **documentación dura** (§2.3), los **records** —no se podan:
   se enmiendan o se superseden— y los archivos del **roster §4.5**.
6. Cerrar: regenerar derivados, correr integridad, y anunciar qué se clasificó,
   qué se congeló, qué se retiró y **qué quedó fuera de alcance y por qué**. Todo
   pase que escribe deja su entrada en el log de migraciones (§9.2).

**Lo que este flujo NO hace:** *idioma y nomenclatura* —son migración por capas
encadenada después (§1.8, §9), no normalización—; *higiene operativa* —se flagea
y no se toca—; *investigar* —una pregunta sin responder es una unidad y se
planifica—; y *elegir por el humano* —ninguna adjudicación, ninguna clase dudosa,
ningún borrado.

#### Las pipelines de operación

Entrado el proyecto por una de las tres puertas, el ciclo es el mismo para todos:
se lanza una unidad, se destila lo que no es una corrida, se cierra con QA y se
sintetiza.

**`/launch rNN`** — cuando una unidad está ready.

Armar el payload según su postura de contexto (§8.2) → chat nuevo titulado
`rNN — slug` → **sellar `session`, `constitution` y `status: frozen → running`,
y commitear el payload como record** → correr los N runs del contrato (§3) →
antes de cerrar el chat, pedir **ahí mismo** el report en plantilla, el borrador
de findings y la bitácora (esa sesión tiene el contexto completo: es el mejor
lugar para destilar) → los exports verbatim aterrizan directo en
`raw/run-NN.md`, por ingesta con destino declarado (§2.6; §12, G3).

**`/distill`** — el bronze que no es una corrida, hasta el conocimiento.

Es la contraparte de `/launch` para las cinco clases de fuente que no producen
una corrida de investigación (§2.1): el material ya está adentro y hay que
llevarlo a silver y a gold **sin re-investigar nada**. Salda la deuda que §2.4
declara — material cargado sin destilación declarada.

1. **Verificar la cadena antes de declarar nada.** El bronze tiene que tener
   **sidecar de procedencia**: no se destila lo que no tiene procedencia. Se
   re-verifica su `sha256` contra lo que el sidecar declaró, y **si no coincide,
   el bronze cambió**: la destilación se detiene. Un byte añadido rompe la cadena
   de auditoría de toda afirmación que lo cite (§2.2).
2. **Resolver la unidad que aloja la destilación** (§2.2): el silver y el gold
   viven en la carpeta de una unidad, siempre. Si el bronze no pertenece a
   ninguna, **cuál lo destila lo decide el humano**, y el bronze se queda donde
   está, citado por ruta y `sha256`.
3. **Escribir el silver — extracción, no interpretación.** Es el `01-report` de
   esa unidad y se valida contra **la misma plantilla de siempre**: no hay una
   plantilla aparte para destilar (principio de diseño #4). Lo que este flujo
   agrega es **cómo se cita un bronze que no es una corrida**: una fila de fuente
   **por pasaje citado**, con su `<unit>-srcNN` y su **locator** —página y párrafo
   del documento, `mm:ss` del audio o el video, ID de respuesta y columna de la
   tanda, encuadre de la imagen—, porque **sin locator la afirmación no es
   verificable y por lo tanto no es re-derivable**. La calidad A–D (§2.5) se
   aplica a **quién produjo el bronze**, no a lo bien presentado que esté: el
   dictamen de un proveedor sobre su propio producto es **C** aunque venga
   membretado. Lo que el bronze **no dice** va a la sección de huecos: un silver
   que rellena con contexto propio dejó de ser re-derivable.
4. **Escribir el borrador de gold**, con el techo de madurez de §0.2 #4 puesto y
   sin negociación: **una sola fuente no da `established`** —la madurez sube por
   triangulación o por replicación entre corridas, y un documento suelto no es
   ninguna de las dos— y **sin ID de fuente la afirmación es `speculative`**. Es
   un borrador y se entrega como tal: quien lo finaliza y lo asienta es el
   coordinador, en el cierre.
5. **Sellar la destilación** como anotación **append-only** del sidecar del
   bronze: qué salió de él, dónde vive y con qué hash se verificó. La incisión va
   ahí y **jamás dentro del verbatim** (§9.2). Con la destilación declarada, ese
   bronze deja de figurar como deuda.

**Datos personales y consentimiento viven en el sidecar** (§2.2): si el bronze
los tiene y el sidecar no lo declara, la destilación se detiene y pregunta.
**La documentación dura no debe silver ni gold** (§2.3): es fuente de record.

**`/close rNN`** — el gate de QA y todo lo que sigue. Los pasos 1–3 son el
status `qa`.

1. **Validación de formato** — scripteada: columnas de la tabla de requisitos,
   IDs, y madurez + volatilidad + fecha + ID de fuente en cada afirmación.
   **La validación estricta es la norma.** Existe un modo *lenient* que baja
   todo error a advertencia; está **reservado al retro-parse de corpus artesanal
   de `/adopt`** (§10.2, paso 6), un cierre normal jamás lo usa, y todo cierre
   lenient anota su desviación por escrito en el record que §5 le declara. Si
   aparece en un cierre normal, es un error de proceso, no un atajo.
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
| Ratificación de la constitution | `/inception` paso 4 | supuestos, dominio, techo de gasto, umbrales, disparadores **y los valores del bloque ratificado** (§4.3) | humano | borrador de constitution | `constitution.md` v1 |
| Ratificación del mapa | `/inception` paso 6 | alcance de unidades, `needs`, kill criteria, briefing | humano | borrador de mapa | protocols congelados |
| **Adjudicación de vigentes** | `/normalize` paso 4 · `/adopt` paso 7 | cuál versión de cada concepto es la vigente, entre familias de versión o épocas conviviendo | humano | inventario de familias y épocas | filas de supersesión de lo superado |
| QA del report | `/close` pasos 1–2 | plantilla, etiquetas, auditoría de afirmaciones | script + prompt | report + sources | fila de métricas + registry de auditorías |
| Disparo de kill criteria | cualquier hallazgo, cualquier unidad | la decisión afectada se revisa de inmediato | humano | hallazgo disparador | enmienda / ADR |
| Decisiones de síntesis | `/synthesis` | todo lo que la síntesis decide | humano | registry completo | ADRs · arquitectura · constitution de desarrollo |
| Enmienda del bloque ratificado | cambio en `horizons`, `runs`, `ids`, `metrics` o `context` **de una constitution en vigor** (§4.3) | ¿sube `version:` de la constitution en el mismo commit? | humano + script | diff de la config | bump + changelog |

**Los nombres de gate NO son un enum cerrado.** El primer párrafo lo dice y esta
tabla lo respeta: **el kernel es el esquema**, y *qué* gates existen es un
playbook por tipo de flujo. Esta tabla instancia el playbook de inception — es el
**set de nombres canónicos recomendados**, no el universo de lo declarable. Un
flujo que instancie el esquema con otro gate no está violando la spec; congelar
la lista sí violaría §11.1, porque los tipos de flujo que §11.3 declara fuera de
alcance traerán los suyos. En consecuencia, **quien lea el registry de gates
resuelve por alias**: una fila histórica escrita con otro texto se lee igual —el
registry es append-only y no se reescribe (§13.2)—, y quien escriba una fila usa
el nombre canónico cuando lo hay.

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

| Registry | Datos — **el record** | Vista — **derivada** | Régimen de los datos |
|---|---|---|---|
| Metrics | `data/metrics` | `metrics.md` | **append-only** |
| Ingest log | `data/ingest-log` | `ingest-log.md` | **append-only** |
| Supersessions | `data/supersessions` | `supersessions.md` | **append-only** |
| Migrations | `data/migrations` | `migrations.md` | **append-only** |
| QA audits | `data/qa-audits` | `qa-audits.md` | **append-only** |
| **Gates** | `data/gates` | `gates.md` | **append-only** — un registro por gate consumido (§7.4) |
| Requirements (RTM) | `data/requirements` | `requirements.md` | record **marcable**: las filas jamás se borran; una fila superada se marca `SUPERSEDED by <id>`, y una enmienda propaga marca de invalidación |
| Conflicts | `data/conflicts` | `conflicts.md` | record **marcable**: la fila evoluciona en sus columnas de resolución y status; el ID y el origen no cambian |
| Status | — *(sin datos propios)* | `STATUS.md` | **vista derivada** — deriva de los protocols; regenerable, jamás editada a mano, jamás autoritativa. No es un record |

Las rutas son relativas a `<registry>/`. **La casa es normativa; la extensión, no**
— ver más abajo.

**El dato es el record; el `.md` es su vista.** Las dos mitades cargan reglas
distintas, y confundirlas es lo que esta fila separa:

- **Los datos son el record.** Ahí vive lo que la fila afirmó, ahí se hace
  cumplir el régimen, y ahí —y solo ahí— se escribe. **Nadie edita un registry a
  mano:** se escribe por la puerta que el kit expone, que es la que garantiza el
  régimen.
- **La vista es derivada** (principio de operación #1): tiene que ser
  **exactamente** la regeneración de sus datos. Editarla a mano es escribir una
  afirmación que ninguna fuente respalda, y por eso se rechaza aunque el texto
  sea correcto: una vista que se editó dejó de ser una vista.

**Esta tabla norma la casa y el régimen, no el formato.** `<registry>/data/` es
la casa de los datos y esta tabla nombra el dataset de cada registry; **qué
serialización usan es decisión del kit**, con una sola exigencia de esta spec:
que el régimen se pueda verificar **sin parser de terceros**, porque la guarda
corre con git y Python estándar (§4.4). El formato puede cambiar en un bump —
**el régimen no cambia con él**, y ese cambio no es enmienda de esta spec.

**Append-only significa que el contenido previo no se pisa**: se agrega al
final, y la vista lo declara en su encabezado. **Marcable** significa que la fila
se edita solo para marcarla, nunca para borrarla ni para cambiar lo que afirmó —
y solo mutan las columnas declaradas marcables.

**El `status` de una fila de conflicto es `open | resolved`**, en inglés como
todo valor de enum (principio de diseño #6). La spec ya declaraba la **columna**
—"la fila evoluciona en sus columnas de resolución y status"— pero no su
vocabulario, y un vocabulario sin declarar es un dialecto esperando a nacer: el
dialecto español que el tooling 0.1.x–0.2.x escribió se lee con glosario (§13.2)
y **jamás se emite**. `resolution` queda para la prosa de la adjudicación, en
`language`.

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
| **entry flow** | una de las tres puertas por las que un proyecto entra al framework: `/inception`, `/adopt`, `/normalize`. El set es cerrado (§10.2) |
| **retro-lenient close** | el cierre de una unidad adoptada bajo el modo lenient de validación, con su desviación anotada en el record que §5 le declara. Solo existe en `/adopt` |
| **monolith** | archivo append-heavy que nadie puede dejar de leer y donde la corrección se agrega al final sin retirar lo viejo: eco por frecuencia en su forma pura. Se tritura (§10.2, `/normalize`) |
| **thin pointer** | archivo de entrada que **apunta** a donde vive una regla sin repetirla. Su prueba: si se borra, no se pierde ninguna regla — solo el atajo (§4.5) |

### 13.2 Vocabulario histórico — contrato de lectura del corpus viejo

El bronze jamás se reescribe (§9.1). Estas equivalencias son **parte del
contrato**: quien lea un record histórico las necesita, y quien migre no las
aplica al verbatim.

| Histórico | Significaba | Canónico vigente |
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
| `abierto / resuelto` | status de una fila de conflicto, dialecto del tooling 0.1.x–0.2.x | `open / resolved` (§12, G6) |
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

**Regla de auditoría del alcance:** todo párrafo normativo traza a §14.1, §14.2,
§14.3 o §14.5. Si algo no traza a ninguna, es scope creep y se borra.

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

### 14.5 v0.3 → v0.4

Insumo: las **ocho enmiendas encoladas** por las sesiones de activación e
implementación (kit 0.2.0, 0.3.0 y 0.4.0), la **práctica implementada y validada**
del kit 0.4.0 —los cuatro flujos, con sus gates y sus guardas— y las **tres
adjudicaciones de tooling** ya aceptadas por el coordinador. Agenda **cerrada** en
diez ítems: nada más entró, y lo que la redacción encontró fuera de ella está en
el acta como laguna o como nota post-gate, no en el texto normativo.

| Δ | Cambio | Secciones tocadas | Ítem del batch |
|---|---|---|---|
| Δ14 | **La regla pre-gate es de la clase, no de esta spec.** Mientras el `status:` de una constitution es `draft`/`proposed` no está en vigor: editarla —incluido **ratificarla**— entra a su misma versión y no la bumpea. Corolario sobre el bloque ratificado (pre-gate se ratifica **con** la constitution) y fallo del lado seguro (sin `status:` declarado, se la trata como vigente) | §4.3, § "Cómo se lee y cómo se enmienda" | 1 |
| Δ15 | **`retro-lenient-deviations.md` ocupa fila en la carpeta de unidad**, y el set de esa carpeta queda **cerrado** como el roster de §4.5 cierra la raíz: un archivo sin fila no es una excepción, es una violación | §5 | 2 |
| Δ16 | **Casa del silver y del gold para el bronze sin unidad:** la aloja **una unidad**, siempre; el bronze se queda en `evidence/<class>/` y se cita por **ruta y `sha256`**. Mudarlo es migración opt-in, jamás un efecto de destilar | §2.2, §5 | 3 |
| Δ17 | **Fila para los archivos que exige el ecosistema** (`LICENSE`, `NOTICE`, `CITATION.cff`): existen legítimamente y están **fuera del KB** — no son records, no entran a la cadena de evidencia y el ciclo de borrado no los alcanza. Criterio, no lista exhaustiva | §4.5 | 4 |
| Δ18 | **Fila para el documento de plan**, que §12 G1 y §10.2 ya exigían sin declararle casa: mapa + briefing + una sección por unidad, apuntado por el `plan:` del protocol. Es **record** — comisionar de nuevo es un plan nuevo que supersede, jamás una edición | §4.5 | 5 |
| Δ19 | **Los datos del registry son el record; el `.md` es su vista derivada.** El régimen se hace cumplir sobre los datos; la vista tiene que ser exactamente su regeneración. La casa (`<registry>/data/`) es normativa; **el formato lo elige el kit** y cambiarlo no es enmienda | §4.5, §12 G6 | 6 |
| Δ20 | **`INDEX.md` en la raíz**, canonizado por nombre y por ruta: vista derivada generada y **puntero delgado**. Deja de ser "el índice, que hoy no existe" | §4.5 | 7 |
| Δ21 | **Las tres condiciones de la reubicación, en la letra:** contenido byte a byte idéntico · destino en otra casa protegida · rastro en el MISMO commit. Escritas acá, ningún tooling futuro las afloja sin enmendar esta spec | §9.1 | 8 |
| Δ22 | **Canonización de los cuatro flujos desde la práctica implementada:** las **tres entradas y no hay más** (`/inception`, `/adopt`, `/normalize`) con sus tres invariantes, y **`/distill`** para el bronze que no es una corrida. Se describe lo que el kit 0.4.0 ya implementa y validó — no se rediseña nada | §10.2, §4.5 (quién verifica el roster), §11.1 | 9 |
| Δ23 | **Adjudicaciones de tooling asentadas:** `status` de conflicto = `open \| resolved` · los **nombres de gate no son enum cerrado** (playbook por flujo, resolución por alias) · la **reubicación es contrato** de §9.1 y no una excepción que el tooling concede | §11.1, §12 G6, §9.1, §13.2 | 10 |

**Qué se arrastró de la v0.3 sin cambio:** todo lo demás. Las secciones que el
batch no toca —§0, §1, §2.1 y §2.3–§2.6, §3, §4.1–§4.2 y §4.4, §6, §7, §8, §9.2–§9.4,
§10.1, §11.2–§11.3, §12 G1–G5— quedan **verbatim**, y sus reglas de activación ya
consumidas siguen siendo el registro de cómo entraron.

### 14.6 Estado de la v0.4

`proposed`. Rige la **v0.3** hasta que el humano ratifique el ACTA DE GATE del
final. La ratificación sube `status:` a `ratified` y congela esta versión; desde
ese acto, todo cambio posterior vuelve al protocolo duro (§4.3).

**Esta enmienda no exige activación de tooling.** El kit 0.4.0 ya implementa lo
que estos diez ítems canonizan — esa es precisamente la razón de que se canonice.
Los desajustes que la redacción encontró entre la letra nueva y el tooling
existente son **ajustes menores post-gate**, están enumerados uno por uno en el
acta, y ninguno bloquea la ratificación.

---

# ACTA DE GATE — spec v0.3 · **CONSUMIDA el 2026-08-19**

> **Esta acta ya se resolvió.** Se conserva porque §14.3 traza sus enmiendas a
> ítems de esta lista (B3, B24–B32) y porque las alternativas descartadas de
> B1–B32 son el "por qué no" de reglas todavía vigentes. **El gate pendiente es
> el de la v0.4, al final de este documento** — no se resuelve nada leyendo esta
> sección. Su contenido es un record: no se edita.

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

---

# ACTA DE GATE — spec v0.4

*Esta acta es el gate, y es el **único** pendiente en este documento. Está
diseñada para resolverse **leyendo solo el acta**: cada ítem trae qué se decide,
la resolución propuesta y —cuando la decisión es nueva— la alternativa
descartada. Ratificar el acta ratifica la v0.4 y sube su `status:` a `ratified`;
rechazar un ítem obliga a enmendar la sección que lo implementa antes de subir el
estado.*

**Alcance, para que se pueda auditar de un vistazo.** v0.4 = v0.3 ratificada
arrastrada sin cambio + los **10 ítems del batch v0.4** del plan de mejoras
vigente. La agenda estaba **cerrada** antes de escribir la primera línea. La
Sección A es lo que ya se adjudicó en conversación o se entregó en el kit y esta
spec convierte en texto normativo; la Sección B es lo que la redacción tuvo que
decidir por su cuenta. Al final: las **lagunas** —lo que bloqueó a la redacción o
la obligó a asumir— y las **notas post-gate** de tooling, que no bloquean nada.

**Ningún ítem de este batch exige activación de tooling.** El kit 0.4.0 ya
implementa lo que se canoniza; por eso la v0.4 no lleva reglas de activación
nuevas.

## Sección A — Consolidación (ya adjudicado o ya entregado; solo confirmar)

Nada de esta sección es nuevo. Son decisiones tomadas en conversación por el
coordinador, o mecanismos ya construidos y validados en el kit, que la spec
convierte en letra. **Confirmar que el texto dice lo ratificado.**

| # | Decisión ya tomada | Cuándo y dónde se tomó | Dónde quedó normada |
|---|---|---|---|
| A1 | **La reubicación es contrato**, no una excepción que la guarda concede: mismo blob + destino en casa protegida + rastro en el mismo commit | adjudicación del coordinador, 2026-08-19 (sesión 3A) | §9.1 |
| A2 | **`status` de conflicto = `open \| resolved`**, en inglés | ídem | §12 G6, §13.2 |
| A3 | **Los gates NO son enum cerrado**: playbook por tipo de flujo, nombres canónicos recomendados y resolución por alias | ídem | §11.1 |
| A4 | **La regla pre-gate de §4.3 vale para la constitution del proyecto**: `draft`/`proposed` no está en vigor, ratificar entra a la misma versión, y sin `status:` se la trata como vigente | implementado y validado en la guarda, 2026-08-20 (`c603302`) | §4.3 |
| A5 | **El chequeo de integridad censa solo el registry**; el censo de la raíz y de `<research>/` vive en el flujo de normalización, donde hay un humano mirando | adjudicación de gate en vuelo, 2026-08-19 | §4.5 ("Quién verifica el roster"), §10.2 |
| A6 | **Tres entradas y no hay más** (`/inception`, `/adopt`, `/normalize`), como pipelines de normalización | ratificado en el plan de mejoras, 2026-08-13; entregado en el kit 0.4.0 | §10.2 |
| A7 | **Los registries son datos y su `.md` es la vista generada**; los tres regímenes se hacen cumplir sobre los datos | entregado en el kit 0.3.0, revisión aceptada | §4.5, §12 G6 |
| A8 | **`INDEX.md` en la raíz, generado** — el índice puerta-de-entrada que §1.2 daba por supuesto | ídem | §4.5 |
| A9 | **La desviación de un cierre lenient vive en `<unit>/retro-lenient-deviations.md`**, con la salida literal de la validación | entregado en el kit 0.4.0 (`/adopt`) | §5, §10.2 |
| A10 | **El silver lo aloja una unidad, siempre**; el bronze sin unidad se queda en `evidence/<class>/` y se cita por ruta y `sha256` | costura decidida en la sesión 3B | §2.2, §5, §10.2 |
| A11 | **La adopción no inventa filas de ingesta**: la procedencia queda en tres casas que ya existen (log de ingesta, log de migraciones, sidecar) | ídem | §10.2 (`/adopt`, paso 3) |
| A12 | **El monolito se congela EN SU LUGAR**, como ruta inmutable extra — no se mueve ni se edita | ídem | §10.2 (`/normalize`, paso 3) |
| A13 | **Todo pase que escribe de la normalización deja su entrada en el log de migraciones** | ídem | §10.2 (`/normalize`, paso 6) |

## Sección B — Decisiones nuevas de esta redacción (requieren ratificación)

Cada ítem: **decisión → resolución propuesta → alternativa descartada.**

| # | Decisión | Resolución propuesta | Alternativa descartada |
|---|---|---|---|
| B1 | **¿La spec congela el formato de los datos del registry?** El ítem 6 del batch los nombra como `data/*.jsonl` | **La casa es normativa; la extensión, no.** §12 G6 nombra `<registry>/data/` y el dataset de cada registry, y exige una sola cosa del formato: que el régimen se verifique **sin parser de terceros** (§4.4). Cambiar la serialización es un bump del kit, no una enmienda | Escribir `.jsonl` en la letra — contradiría lo que la propia G6 declara ("norma el régimen, no el formato") y convertiría una decisión de implementación en materia de gate humano |
| B2 | **¿Qué clase es el documento de plan?** | **Record.** Es la comisión que un gate ratificó y que el `plan:` de cada protocol apunta como procedencia; comisionar de nuevo es **un plan nuevo que supersede**, con su fila | Evergreen con una sola casa — editarlo cambiaría retroactivamente el sobre que una sesión ya abrió, que es exactamente lo que el régimen de record existe para impedir |
| B3 | **¿Cómo entra `LICENSE`/`NOTICE`/`CITATION` sin abrir la taxonomía cerrada?** | **Una fila definida por criterio**: archivos que **exige el ecosistema**, sin regla del framework adentro y con dueño fuera del repo. Están **fuera del KB**: no son records, no se citan, el borrado no los alcanza. La lista es ilustrativa; el criterio es la prueba, y un archivo que porta reglas del repo no entra por esta puerta | (a) Enumeración exhaustiva — cada convención nueva del ecosistema (`SECURITY.md`, `CODEOWNERS`…) exigiría enmienda de la spec; (b) dejarlos fuera de la tabla — un repo que hace lo legalmente correcto quedaría en falta con su propia constitution |
| B4 | **¿El set de la carpeta de una unidad es cerrado?** v0.3 decía "contiene TODO lo suyo", que no es una prueba | **Sí, cerrado, con la misma prueba de §4.5**: la tabla de §5 es el set completo —contando `<archivo>.vN.md` y el contenido de `raw/`—, y un archivo sin fila no es una excepción sino una violación | Dejar la carpeta abierta — es justamente lo que permitió que `retro-lenient-deviations.md` naciera sin fila y llegara a este batch como enmienda |
| B5 | **¿`/distill` es una cuarta entrada?** | **No.** Las entradas son tres; `/distill` es la pipeline de destilación, hermana de `/launch`: opera sobre bronze **que ya está adentro** | Llamarlas "cuatro entradas" — volvería falso el set cerrado de tres y diría que material ya ingresado "entra" |
| B6 | **La adjudicación de vigentes es un gate humano que dos flujos consumen y §11.1 no declaraba** | **Se le agrega su fila** a la tabla del playbook (disparador, chequeo, autoridad, evidencia, record de salida). Sin fila viviría sin declarar, que es el síntoma que la retro #11 corrigió para los demás | No agregarla y tratarla como "juicio dentro del flujo" — un gate sin fila no deja rastro, y §7.4 exige que todo gate consumido lo deje |
| B7 | **Los pasos de `/inception` en v0.3 (cuatro) no son los del flujo implementado (siete)** | **Se renumera para describir la práctica**: elicitación · `language` · siembra · constitution + gate · unidades preliminares · mapa y briefing + gate · cierre. Las referencias de §11.1 siguen a los pasos nuevos | Conservar los cuatro pasos — §11.1 seguiría apuntando a pasos que no existen, y la confirmación de `language` (§1.8) quedaría invisible en el único flujo obligado a honrarla antes del primer artefacto |
| B8 | **¿La spec escribe los umbrales del censo de normalización?** (tamaño de monolito, líneas de un puntero delgado) | **No.** La spec norma el **mecanismo y la prueba**; los umbrales son calibración de tooling y viven en el kit | Escribir los números — congelaría una calibración en un documento cuyo cambio exige gate humano, y afinar un umbral pasaría a ser una enmienda constitucional |
| B9 | **¿La spec escribe los comandos y las flags de los flujos?** | **No.** §10.2 describe pasos, gates, garantías y prohibiciones; la superficie de línea de comandos es del kit y se documenta ahí | Escribirlas — sería una segunda casa de la interfaz del kit, que deriva al primer bump (principio de diseño #4) |
| B10 | **¿Qué pasa con el acta de la v0.3, ya consumida?** | **Se conserva marcada como CONSUMIDA**, con un puntero al gate vigente. §14.3 traza sus enmiendas a ítems de esa lista y las alternativas descartadas de B1–B32 son el "por qué no" de reglas todavía vigentes | Borrarla — dejaría punteros colgando desde §14.3 y perdería el fundamento de 32 decisiones que siguen en vigor |
| B11 | **Cuatro términos que el texto nuevo usa como términos de arte y el glosario no tenía** | **Entradas nuevas en §13.1**: `entry flow`, `retro-lenient close`, `monolith`, `thin pointer`; y en §13.2, el dialecto `abierto/resuelto` del status de conflicto | Dejarlos sin entrada — un término de arte sin glosario es exactamente como nacieron los dialectos que §13 vino a cerrar (§1.7) |
| B12 | **Texto de la v0.3 que quedó falso al consumirse** | **Se retira**, y su historia queda en §14 y en el historial: la "regla de activación" de §4.5 (el chequeo no se construyó ahí, y eso se adjudicó), el "estado de implementación" de §12 G6 (`gates.md` existe desde 0.2.0), el "hoy no existe" del índice, y el "fuera del alcance de v0.3" del modo lenient | Conservarlo — una constitution que describe como pendiente lo que ya existe le enseña al lector algo falso, y es la clase de deriva que §0.2 #1 prohíbe |

## Lagunas — lo que la redacción no pudo cerrar sola

*Definición estricta: solo lo que bloqueó la redacción o la obligó a asumir. Las
ideas de mejora se descartaron; no se reportan.*

1. **El gate de adjudicación de vigentes no tiene nombre canónico.** §11.1 le
   declara la fila (B6), pero la spec no fija tokens de gate (§11.1, Δ23) y el
   kit hoy escribe esa fila bajo el nombre recomendado de otro gate. Quien
   compare el registry contra §11.1 no va a encontrar el nombre. **Se asumió**
   dejar el token sin fijar, que es lo coherente con "los gates no son enum
   cerrado". Resolverlo es ajuste de tooling —darle su nombre— o una enmienda
   futura si se prefiere fijarlo en la letra.
2. **La adopción no deja fila del gate de adjudicación de vigentes.** §7.4 exige
   —desde la v0.3— que todo gate consumido deje su fila; el flujo de adopción
   hace la adjudicación con el humano y escribe las supersesiones, pero no la
   fila del gate. La redacción **no corrigió la práctica** (habría sido rediseño)
   ni ablandó la regla: se declara acá. Es un ajuste de tooling post-gate.
3. **Un proyecto que califica para dos puertas a la vez no tiene regla.** Cada
   flujo declara cuándo *no* es la puerta y deriva a la que sí, pero ninguno dice
   qué hacer con un repo que **ya existe con documentación** *y* además trae
   corpus artesanal sin adoptar. Lo natural sería encadenarlos, y **la redacción
   escribió esa regla y después la retiró**: no está en la práctica, y
   canonizarla habría sido rediseñar. §10.2 queda diciendo solo lo que los flujos
   dicen —cada puerta deriva cuando no es la suya—, y el encadenamiento queda
   como decisión del humano caso por caso hasta que se valide.

## Notas post-gate — tooling que sigue a la letra nueva

*Ninguna bloquea la ratificación: son el trabajo que la canonización habilita, y
por regla dura de esta sesión no se tocó una sola línea de tooling.*

1. El censo del roster **no conoce los archivos del ecosistema**: con la fila de
   §4.5 ratificada, `LICENSE`/`NOTICE`/`CITATION` dejan de ser "fuera del roster".
2. El censo del roster ubica los **documentos de plan** en una canasta aparte
   —"la tabla §4.5 aún no le declara fila"—: con Δ18 pasan a ser roster.
3. El flujo de adopción lleva una **constancia de que la fila de
   `retro-lenient-deviations.md` está encolada** para este batch: con Δ15
   ratificada, se retira.
4. El flujo de destilación lleva la misma clase de constancia sobre **la casa del
   silver**: con Δ16 ratificada, se retira.
5. El gate de adjudicación de vigentes y su fila (lagunas 1 y 2).
6. `kit_version`, `README` y `CHANGELOG` del kit **referencian la spec v0.3**:
   pasan a v0.4 cuando el gate se consuma.
7. La fila del registry de gates de **esta misma ratificación** se escribe al
   consumirla, como cualquier otra (§7.4).

---

*Fin del acta. El gate pendiente es este.*
