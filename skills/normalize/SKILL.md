---
name: normalize
description: Lleva un repo con documentación existente al formato del framework — inventario, clasificación por mutabilidad, roster §4.5 y prueba del puntero delgado, triturado de monolitos, adjudicación de vigentes en gate humano, retención declarada y borrado. Uso — /inception-kit:normalize
---

# /inception-kit:normalize

El flujo de entrada de un **repo que ya existe** y tiene documentación: docs
desordenados, épocas conviviendo, ideas obsoletas haciendo eco. Un edge case no
se le agrega al framework — **se normaliza hacia él** (principio de diseño #1):
el framework toma el repo en el estado en que esté y lo lleva al estado que
dicta.

**Nada se borra sin `--apply`, y `--apply` se pide con el inventario a la
vista.** La adjudicación de qué está vigente es **gate humano siempre**: ante
tres arquitecturas simultáneas ningún mecanismo elige solo.

## 1. Inventario — read-only, primero, completo

`normalize` (o `normalize inventory`). No escribe un solo archivo. Devuelve, en
una página:

| Sección | Qué contesta |
|---|---|
| **Roster §4.5** | qué archivo repo-level está en la tabla —contando el documento de plan y los archivos del ecosistema, que tienen fila— y cuál está **fuera** |
| **Puntero delgado** | qué archivo de entrada engordó hasta albergar reglas de otra casa |
| **Documentos a clasificar** | todo markdown fuera de las casas del framework, con su peso y sus commits |
| **Monolitos** | el log append-heavy que concentra el eco |
| **Épocas como carpetas** | mismo basename en carpetas distintas |
| **Familias de versión** | pares `x` / `x-v2` sin vigente declarado |
| **Huérfanos** | lo que nadie enlaza, ni desde findings ni desde el registry |
| **Higiene operativa** | worktrees, cachés, salida de build — **fuera de alcance**, se nombra y no se toca |

**Reportar el inventario al humano tal cual, sin resumirlo.** El censo describe;
no clasifica ni adjudica.

### Acá vive el enforcement que `doctor` no hace

`doctor` censa **solo el registry**, por adjudicación explícita: censar la raíz
lo obligaría a asumir filas que la tabla §4.5 no declara, y corre en cada push —
no puede fallar sobre algo que necesita juicio. **El censo de la raíz y de
`<research>/` vive acá**, donde hay un humano mirando.

Las dos mitades de §4.5, y las dos son duras:

- **Taxonomía cerrada.** La tabla es el set completo. Un archivo repo-level que
  no esté en ella **no es «una excepción»**: o se mueve a la casa que le
  corresponde, o entra por enmienda de la spec con su fila declarada. Dos casos
  con nombre propio: `SPEC.md` **no vive en un repo consumidor** (se referencia
  por el `kit_version` de la config), y `AGENTS.md` **no es parte del
  framework** — si un harness lo exige, se genera desde la misma fuente que
  `CLAUDE.md`, jamás se redacta aparte.
- **La prueba del puntero delgado.** *Si se borra un archivo de entrada, no se
  pierde ninguna regla — solo el atajo para encontrarla.* El censo la mide: una
  línea de `README.md`, `CLAUDE.md` o `INDEX.md` que también vive en la
  constitution o en la config es una **segunda casa**. Un resumen es una copia
  que deriva en silencio, y se corrige **moviendo, no duplicando**.

## 2. Clasificar — cada documento en exactamente una clase

Con el inventario delante, y con el humano cuando haya duda (spec §4.1):

| Clase | Qué es | Qué se hace |
|---|---|---|
| **record** | se escribió una vez y describe un momento: actas, informes, resultados | se le da casa y se **congela**; se corrige por enmienda, jamás editando |
| **evergreen** | describe estado actual y hay **una sola casa por hecho** | se elige la vigente, se actualiza in-place y las demás mueren |
| **efímero** | nunca debió ser archivo | va al chat o al PR; el archivo se retira |
| **hard-doc** | licencias, contratos, documentos oficiales | a `paths.hard_docs` (o afuera con puntero + `sha256`), y **jamás se borra** |

**Un archivo nuevo exige consumidor y momento de lectura declarados** (§4.2). Un
documento que no los tiene no es un documento: es chat que se solidificó.

## 3. Triturar los monolitos

Un archivo append-heavy que ningún agente puede dejar de leer es **eco por
frecuencia en su forma pura**: la corrección se agrega al final y el texto viejo
sigue ahí, pesando. El triturado lo parte en dos, y las dos mitades son
mecanismos que ya existen:

1. **Lo vigente sale como datos y como records individuales** — cada decisión a
   su ADR, cada requisito a la RTM, cada conflicto a su fila, todo por
   `registry add`. El registry es datos y su `.md` es la vista.
2. **El original queda congelado EN SU LUGAR** — `normalize freeze <ruta>
   --apply` lo declara en `records.extra_immutable_paths` y la guarda lo protege
   desde el próximo commit. No se mueve, no se edita, no se pierde un byte: sale
   del contexto de lectura porque ya nada lo apunta, no porque se lo haya tocado.

## 4. Adjudicar vigentes — **GATE HUMANO, sin excepción**

Las familias de versión y las épocas conviviendo se resuelven eligiendo
**una** vigente por concepto. Esa elección **no la toma esta skill**: la toma el
humano, con la lista delante.

Elegido el vigente, cada versión superada deja su fila
(`registry add supersessions --superseded … --superseded_by … --reason …`) y su
anotación de sidecar. El corpus solo-vigente es **precondición estructural** del
payload (spec §8.3): un corpus con tres versiones sin vigente declarado produce
eco por construcción, y `doctor` lo reporta.

Consumido el gate: `registry add gates --gate current-adjudication --decision
«vigente de <concepto>: <cuál>, entre <n> versiones» --record_out «filas de
supersesión de lo superado»`. Es el gate de **adjudicación de vigentes** de spec
§11.1 y `current-adjudication` es el nombre del kit: la spec no fija tokens de
gate, y todo gate consumido deja su fila (§7.4).

## 5. Retención declarada y borrado

`normalize retire <rutas> --reason «…» [--apply]`.

- **`--reason` es obligatorio.** Un borrado sin retención declarada es una
  pérdida, no una normalización: qué se retira, por qué ya no aplica y dónde
  vive lo que lo reemplaza.
- **Un evergreen muerto se BORRA, no se archiva** (spec §4.1): el historial ya
  vive en git, y una carpeta de archivo es una época más conviviendo en el
  contexto de todo agente que lea la carpeta padre.
- **Tres cosas el pase no borra nunca, y se planta antes de proponerlas:** la
  **documentación dura** (única clase exenta del ciclo de vida de borrado de
  cualquier flujo, spec §2.3), los **records** (no se podan: se enmiendan o se
  superseden) y los archivos del **roster §4.5**.
- Sin `--apply` imprime el plan y para. El `--apply` se pide después.

Todo pase que escribe deja su entrada en el **registry de migraciones**, con lo
que quedó fuera de alcance y por qué (spec §9.2).

## 6. Cerrar

`derive-status`, `derive-index`, `doctor` — y el veredicto tal cual. Re-correr
`normalize` para mostrar el antes/después del censo.

Anunciar en una tabla: qué se clasificó, qué se congeló, qué se retiró, y **qué
quedó fuera de alcance y por qué**.

## Lo que este flujo NO hace

- **Idioma y nomenclatura** son `/inception-kit:migrate`, encadenado después:
  son operaciones distintas, y la de idioma arrastra su propia migración por
  capas (spec §1.8, §9).
- **Higiene operativa** —worktrees, entornos, cachés— se flagea y no se toca:
  normalizar documentación no es limpiar el entorno local.
- **Investigar.** Si al clasificar aparece una pregunta sin responder, eso es
  una unidad y se planifica con `/inception-kit:plan` — no se resuelve acá.
- **Elegir por el humano.** Ninguna adjudicación de vigente, ninguna clase
  dudosa, ningún borrado: se pregunta.
