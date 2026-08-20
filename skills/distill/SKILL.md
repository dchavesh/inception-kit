---
name: distill
description: Convierte un bronze no investigativo (documento recibido, entrevista, medio, tanda de formulario) en silver re-derivable con procedencia y en el borrador de gold que el coordinador finaliza. Uso — /inception-kit:distill <ruta del bronze>
---

# /inception-kit:distill \<ruta del bronze\>

La unidad dejó de estar acoplada a «sesión que produce markdown»: el framework
ingiere entrevistas, formularios, dictámenes y medios **con la misma disciplina
de procedencia**. Esta skill es la mitad que faltaba — la que convierte ese
material en conocimiento sin re-investigar nada.

**Toda clase declara su flujo bronze → silver → gold** (spec §2.4). Material
cargado sin destilación declarada es **deuda**: no se prohíbe cargar sin
destilar, se prohíbe olvidarlo. `check-recurrence` la lista; este flujo la salda.

| Capa | Qué es | Dónde vive |
|---|---|---|
| **bronze** | el original intacto + su `sha256` + su sidecar de procedencia | `<unit>/raw/` o `<research>/evidence/<class>/` — **jamás se edita** |
| **silver** | la **extracción re-derivable** desde el bronze | `<unit>/01-report.md`, validado contra la plantilla |
| **gold** | los hallazgos | `<unit>/02-findings.md` — lo finaliza el cierre |

**Propiedad medallion:** si cambia la plantilla del report, silver y gold se
re-derivan desde el bronze **sin re-ejecutar investigación**. Por eso el silver
no puede contener nada que no salga del bronze.

## 1. Elegir el bronze y verificar su cadena

De `check-recurrence` sale la lista de carga sin destilar. El bronze tiene que
tener **sidecar de procedencia**: no se destila lo que no tiene procedencia. Si
llegó de afuera y no lo tiene, entró mal — se ingiere con
`/inception-kit:ingest`; si ya vivía en el repo sin casa, se reubica con
`migrate relocate`.

`distill` re-verifica el `sha256` contra lo que el sidecar declaró. **Si no
coincide, el bronze cambió** y el comando se planta: un byte añadido rompe la
cadena de auditoría de toda afirmación que lo cite (spec §2.2).

## 2. Resolver la unidad que aloja la destilación

**La destilación la aloja una unidad, siempre.** El gold es un `02-findings`, y
un `02-findings` vive en la carpeta de su unidad (principio de diseño #5). Si el
bronze ya pertenece a una unidad (`<unit>/raw/`), esa es. Si vive en
`<research>/evidence/<class>/` porque no pertenecía a ninguna, **preguntá al
humano qué unidad lo destila** — y el bronze **se queda donde está**: la unidad
lo cita por ruta y `sha256`, no se lo lleva. Reubicar bronze es otra operación,
es opt-in y es de `/migrate`.

*(Constancia: la spec declara el medallion para el bronze sin unidad pero no le
declara casa al silver fuera de una unidad. Esta resolución —la unidad es la
casa, el bronze puede quedarse afuera y se cita— queda anotada para el batch de
enmiendas v0.4.)*

## 3. Escribir el silver — extracción, no interpretación

El silver es `01-report.md` y se valida contra **la misma plantilla de siempre**
(las 7 secciones del contrato del report; la gramática exacta la trae la skill
`research-close`). Un contrato, un lugar: no hay una plantilla aparte para
destilar.

Lo que este flujo agrega es **cómo se cita un bronze que no es una corrida**:

- **Una fila de fuente por pasaje citado**, con su `<unit>-srcNN` y su
  **locator**: página y párrafo del PDF, `mm:ss` del audio, fila e ID de
  respuesta del formulario, encuadre de la foto. Sin locator, la afirmación no
  es verificable y por lo tanto no es re-derivable.
- **`Quality` según la rúbrica A–D** (spec §2.5) aplicada a *quién produjo el
  bronze*, no a lo bien escrito que esté: el dictamen de un proveedor sobre su
  propio producto es **C** (parte interesada) aunque venga en PDF membretado.
- **`Volatility`** del contenido, no del archivo.
- Lo que el bronze **no dice** va a la sección de huecos. Un silver que rellena
  con contexto propio dejó de ser re-derivable.

**Por clase**, lo único que cambia es de dónde sale el locator:

| Clase | Bronze | Locator |
|---|---|---|
| `document-drop` | el archivo original | página · sección · párrafo |
| `field-interview` | audio/video/transcripción cruda | `mm:ss` (y el hablante, si lo hay) |
| `media` | foto, captura, plano, grabación | qué parte de la imagen o el `mm:ss` |
| `form-batch` | el export crudo de la tanda | ID de respuesta · columna |

**Datos personales y consentimiento viven en el sidecar**, desde el diseño y no
en la prosa (spec §2.2): la legislación de datos personales aplica al propio
repo. Si el bronze los tiene y el sidecar no lo declara, **parar y preguntar**.

## 4. Escribir el BORRADOR de gold

5–10 hallazgos numerados, cada uno con su anotación parseable:
`(<established|supported|plausible|speculative> · <high|medium|low> · fecha)` y
su `<unit>-srcNN`. **El enum va en inglés y sin dialecto; la prosa, en el idioma
que declare `language`** (spec §1.6, §1.8).

Techo de madurez, y no es negociable (spec §0.2 #4):

- **Una sola fuente no da `established`.** La madurez sube por triangulación
  —≥2 fuentes independientes A/B— o por replicación entre corridas, y un
  document-drop suelto no es ninguna de las dos.
- **Sin `<unit>-srcNN` la afirmación es `speculative`**, por definición.
- Baja por fuente única, evidencia solo de parte interesada, evidencia
  indirecta, inconsistencia entre fuentes o vencimiento.

**Es un borrador y se entrega como tal.** Quien lo finaliza y lo asienta es el
coordinador, en el paso 7 de `/inception-kit:close`, y la extracción a la RTM y
las filas del registry se escriben por `registry add` / `extract-registry` —
nunca a mano, nunca desde acá.

## 5. Sellar la destilación

`distill <bronze> --unit UNIT --silver <ruta> --apply`.

Agrega al **sidecar** del bronze la anotación que declara qué salió de él, dónde
vive y con qué hash se verificó. El sidecar es **append-only**: acá se agrega,
nunca se pisa — y la incisión va ahí y jamás dentro del verbatim (spec §9.2).

Con la destilación declarada, el bronze deja de figurar como deuda en
`check-recurrence`. **Commiteá el silver y su sidecar juntos:** el sello es
parte de la destilación, no un trámite aparte.

## 6. Después

El cierre normal: `/inception-kit:close UNIT_ID` — validación de formato,
auditoría de afirmaciones sobre muestra determinista, kill criteria, extracción
a la RTM, métricas medidas y finalización de los findings.

## Reglas

- **El bronze no se toca nunca.** Ni para corregir un typo del original, ni para
  «limpiar» una transcripción: el original intacto es lo que hace auditable todo
  lo que se derive de él.
- **La transcripción cruda de una entrevista es bronze, no silver** (spec §2.1):
  si hace falta conservarla, entra por `/inception-kit:ingest` con su propia
  procedencia, y el silver es la extracción que se hace sobre ella.
- **La documentación dura no tiene obligación de silver ni de gold** (spec
  §2.3): es fuente de record. Toda afirmación derivada de ella recorre la cadena
  de evidencia normal, pero nadie le debe una destilación.
- **Si algo no está claro —la clase, el locator, si hay consentimiento— se
  pregunta.** Adivinar es exactamente lo que la procedencia existe para impedir.
