---
name: adopt
description: Trae al framework un corpus artesanal que ya existe y nunca tuvo repo — retro-parse de las corridas, protocols retroactivos, jerarquía de independencia declarada y cierre retro-lenient anotado, dejando la supersesión preparada. Uso — /inception-kit:adopt <dónde vive el corpus>
---

# /inception-kit:adopt \<dónde vive el corpus\>

El flujo de entrada de una investigación que **ya se hizo** y nunca tuvo casa:
chats sueltos, informes en una carpeta de descargas, un documento largo que
alguien escribió a mano. Adoptar es traerla al framework **sin falsificar qué
pasó**: el corpus entra como es, con sus huecos declarados, no como nos hubiera
gustado que fuera.

**La regla que gobierna todo este flujo:** una adopción jamás mejora el pasado.
No completa una bitácora de memoria, no inventa un kill criterion que nadie
pre-registró, no sube una madurez porque el texto suene seguro. Lo que falta se
declara como limitación — **una ausencia documentada es evidencia; una consulta
inventada es contaminación** (spec §7.1).

## 1. Inventario del corpus — antes de tocar nada

Con el humano, y sin escribir un archivo todavía:

| Qué se pregunta | Por qué |
|---|---|
| ¿Qué corridas hubo y qué produjo cada una? | cada corrida es un `run-NN`; el conteo es contrato, no estimación |
| ¿Se conserva el **verbatim** de cada una? | sin verbatim no hay bronze, y sin bronze la afirmación no es auditable |
| ¿Alguna corrida vio el resultado de otra? | eso es `mode: chained`, y se declara |
| ¿Hay versiones del mismo documento conviviendo? | hay que adjudicar vigente — gate humano |
| ¿Qué material es documentación dura? | tiene casa especial y **jamás se borra** (spec §2.3) |
| ¿En qué idioma está escrito el corpus? | ese es el `language` del repo: adoptar **no traduce** |

Devolver el inventario en una tabla y pedir corrección. Lo que el humano no
confirmó, no se adopta: se pregunta.

## 2. Sembrar el repo y declarar el idioma

`kit-init` si el repo es nuevo. Declarar `language:` con el idioma en que el
corpus **ya está escrito** — cambiarlo después es migración, y los records no se
reescriben (spec §1.8). Si el corpus está en dos idiomas, eso es una decisión
humana, no una que la skill tome.

## 3. El verbatim entra por la puerta, con destino declarado

Cada export, audio o PDF entra con **`/inception-kit:ingest`** y su destino
obligatorio (spec §2.6): `--unit UNIT --run N` para el verbatim de una corrida,
`--unit UNIT --class C` para otro bronze de la unidad, `--class C` para el que
no pertenece a ninguna, `--hard-doc` para la documentación dura. **Ante
ambigüedad, preguntá y no avances.**

### Costura declarada — de dónde salen las filas de procedencia

**`/adopt` no agrega un escritor del ingest-log, y no fabrica filas.** El
ingest-log registra **llegadas**: fecha, origen externo y desenlace del original
(spec §2.6). Para el material que efectivamente llega de afuera, esa fila la
escribe `ingest` por construcción — y por eso todo verbatim adoptado pasa por
ahí. Para el material que **ya vivía dentro del repo**, no hubo llegada: llenar
esas columnas sería inventar una ingesta que no ocurrió, y una migración jamás
falsifica evidencia (spec §9). Ese material se reubica con `migrate relocate`,
que tampoco escribe ingest-log —**reubicar no es ingerir**— y deja su rastro
donde corresponde.

La procedencia del corpus adoptado queda entonces registrada en tres lugares que
ya existen, ninguno nuevo: el **ingest-log** por lo que entró de afuera, el
**registry de migraciones** por el pase de adopción (con lo que quedó fuera de
alcance y por qué), y el **sidecar** de cada record adoptado.

## 4. Protocols retroactivos

Un protocol reconstruido **describe la comisión que la corrida efectivamente
tuvo**, no la que hubiera sido correcta. Se escribe con `templates/protocol.md`
de la skill `plan`, y en el cuerpo lleva su marca: *reconstruido
retroactivamente el \<fecha\> a partir de \<qué evidencia\>*.

- `runs:` es **cuántas corridas hubo**. Si hubo una, es `1` — no se completa
  investigando de más para llegar al default.
- `mode:` es lo que pasó: `chained` si una corrida vio a la otra.
- **Los kill criteria retroactivos se declaran vacíos si no existieron.** Es
  perfectamente legal y es la verdad; inventarlos es lo que no lo es.
- El campo `plan:` apunta al documento de plan si existe; si no existe, se
  redacta uno mínimo con el briefing real que la sesión recibió — o se declara
  que no hubo briefing, que también es un hecho.

Congelar sigue siendo **orden humana** (`freeze-protocols --confirm`).

## 5. Jerarquía de independencia — declarada, no supuesta

Antes de cerrar nada, dejar por escrito qué corrida fue **réplica ciega** y cuál
compartió contexto. **El pecado no es el contexto: es el contexto no declarado**
(spec §3.2). Un conjunto `chained` cuenta como **UNA** unidad epistémica y su
métrica de replicación se declara `n/a` — nunca se le acredita convergencia a
dos corridas que se leyeron entre sí.

Esa jerarquía va a la constitution del repo (§6 de su plantilla): es la que la
síntesis va a aplicar.

## 6. Cierre retro-lenient — **acá vive `--lenient`, y siempre anotado**

El corpus artesanal no fue escrito contra la plantilla, así que no la va a pasar.
Para eso —y **solo** para esto— existe el modo lenient: `validate-report UNIT
--lenient` baja todo error a advertencia (spec §10.2 paso 1). Un cierre normal
jamás lo usa.

**Todo cierre lenient anota su desviación por escrito**, y la anotación es parte
del cierre, no un comentario:

1. **`<unit>/retro-lenient-deviations.md`** — la lista completa de lo que no
   validó, **tal cual la imprimió el comando**, sin maquillar y sin resumir, más
   por qué se acepta: *corpus artesanal adoptado, anterior a la plantilla*. Es un
   record y declara lo que §4.2 exige (`class`, `consumer`, `reading-moment`,
   `date`); **§5 le declara su fila** en la carpeta de la unidad, y esa carpeta
   es un set cerrado igual que la raíz. *(El nombre va en inglés como todo
   nombre del framework; el cuerpo, en `language`.)*
2. su fila de gate: `registry add gates --gate report-qa --decision «cierre
   retro-lenient aceptado: <n> desviaciones anotadas» --record_out «<unit>
   01-report»`;
3. la anotación en el **sidecar** del verbatim adoptado — la incisión va ahí y
   jamás dentro del verbatim (spec §9.2).

**Lo lenient no lava nada.** Una afirmación sin fuente sigue siendo
`speculative` por definición, y ninguna etiqueta sube porque el cierre haya sido
tolerante. El resto del cierre —auditoría de afirmaciones, kill criteria,
extracción a la RTM, métricas medidas— corre igual que en
`/inception-kit:close`, que es de donde salen los pasos.

## 7. Adjudicar vigentes y dejar la supersesión preparada

Si el corpus trae versiones del mismo documento conviviendo, **el vigente lo
elige el humano** — ningún mecanismo elige solo. Cada versión no vigente queda
con su fila (`registry add supersessions`), porque el corpus solo-vigente es
precondición estructural del payload (spec §8.3) y `doctor` lo verifica.

Eso es el gate de **adjudicación de vigentes** (spec §11.1), el mismo que
consume `/normalize` en su paso 4 — y **todo gate consumido deja su fila**
(§7.4): `registry add gates --gate current-adjudication --decision «vigente de
<concepto>: <cuál>, entre <n> versiones» --record_out «filas de supersesión de lo
superado»`. Sin adjudicación no hay fila: si el corpus no trae versiones
conviviendo, el gate no se disparó y no se inventa.

Adoptado el corpus, la supersesión queda **preparada**: cada record vigente es
la base de su familia, sin `.vN`, con su sidecar declarando que es corpus
artesanal adoptado y que se lee con el glosario de spec §13.2. Cuando la primera
investigación nueva lo supere, superarlo es mecánico y sin ambigüedad.

## 8. Cerrar

`derive-status`, `derive-index`, `doctor` — y reportar el veredicto tal cual.

**La retro es obligatoria** (spec §7.5): todo proyecto que adopta el framework
produce una retro como record estándar tras su implantación. No depende de que
el humano se acuerde de pedirla; su consumidor es quien redacte la próxima
versión de la spec.

## Reglas

- **El verbatim jamás se edita ni se «arregla».** Ni una tilde: rompe la cadena
  `sha256` que hace auditable cada afirmación que lo cita (spec §9.1).
- **Lo que no se conserva se declara como limitación**, con su nombre, en la
  bitácora — no se reconstruye.
- **`--lenient` no sale de este flujo.** Si aparece en un cierre normal, es un
  error de proceso, no un atajo.
- **La prosa va en `language`**; enums, IDs, campos y columnas, en inglés.
- Un repo con documentación existente que hay que ordenar no entra por acá:
  entra por **`/inception-kit:normalize`**. Un proyecto sin nada, por
  **`/inception-kit:inception`**.
