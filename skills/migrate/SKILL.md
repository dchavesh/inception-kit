---
name: migrate
description: Pone el repo en sintonía con la versión vigente del kit y de la spec — actualiza evergreen, regenera derivados y ofrece los pases opt-in de supersesión mecánica y de reubicación de bronze legado, con el diff como evidencia y rastro doble siempre. Uso — /inception-kit:migrate [plan]
---

# /inception-kit:migrate

La migración es **por capas y jamás falsifica evidencia** (spec §9). Un repo
*sintonizado* tiene todo en formato vigente salvo el bronze, que se lee con
glosario. **Determinismo en el script, juicio acá, autoridad en el humano:**
ningún pase que escriba corre sin `--apply`, y `--apply` se pide después de
mostrar el diff.

| Capa | Qué se hace | Con qué |
|---|---|---|
| **evergreen** (config) | se actualiza **in-place** | `kit-init` — el runner de versiones |
| **derivados** (tablero, vistas de registry, índice) | se **regeneran** | `migrate derived --apply` |
| **records de lectura** (findings, reports, sources) | **supersesión mecánica**, opt-in | `migrate relabel UNIT --pass vocab\|runs --apply` |
| **verbatim bronze** (`raw/`, `evidence/`, hard-docs, payloads, `inbox/` legados) | **JAMÁS se reescribe**; a lo sumo se **mueve** | `migrate relocate SRC --class C --apply` |

## 1. Diagnosticar primero — siempre

`migrate plan`. No escribe nada: lista qué frente tiene trabajo (config
desincronizada, derivados viejos, records con vocabulario histórico, bandejas
legadas con contenido) y qué comando lo atiende. **Reportar el plan al humano
antes de tocar nada.**

Si la config está desincronizada (`kit_version` ≠ kit instalado), eso se arregla
con **`kit-init`**, que es el runner entre versiones y deja su propio rastro.
Un repo desincronizado no está sano (spec §9.3): es error, no advertencia.

## 2. Derivados — se regeneran, no se discuten

`migrate derived --apply`. Un derivado no afirma nada propio: es caché
regenerable (spec §0.2 #1). No hace falta gate, no deja fila en el registry de
migraciones, y **jamás se edita a mano** ninguno de ellos.

## 3. Supersesión mecánica — **opt-in del humano, con el diff a la vista**

`migrate relabel UNIT [--record 02-findings] [--pass vocab|runs]` imprime el
diff y el resultado del **round-trip**: la prueba de que el texto nuevo
reconstruye el original byte a byte desde el registro de sustituciones, o sea
que **no cambió ningún otro byte**. Recién con `--apply` se emite el `.vN`.

- El pase `vocab` toca etiquetas de madurez y volatilidad **solo dentro de una
  anotación**; `alta` o `media` en prosa no se tocan. El pase `runs` traduce
  `C1`/`CN`/`PI` a `run-NN`; `S` no entra — no era una corrida (spec §13.2).
- **El record viejo no se toca:** queda superado, con su fila en el registry de
  supersesiones y la anotación en su sidecar.
- **Nunca hay supersesiones vacías:** si el record ya es canónico, el comando
  lo dice y no supersede nada «por consistencia» (spec §9.1).
- Si el round-trip falla, el pase se aborta. No es negociable: sin evidencia no
  se toca un record.

**Preguntá antes de aplicar.** Mostrale el diff al humano y esperá su orden.
Un `.vN` es una supersesión declarada, no una corrección de estilo.

## 4. Bronze legado — **reubicar no es reescribir**

`migrate relocate <dir> --class <clase>` (o `--hard-doc`) lleva un `inbox/`
legado —o cualquier bronze sin casa— a la casa real que manda spec §2.6. Mueve
el archivo; el `sha256` es el mismo antes y después, y **eso** es lo que hace
verificable el pase. Con `--apply` mueve, escribe el sidecar de procedencia y
commitea con su rastro.

- **La clase no se adivina.** Sale del enum cerrado de spec §2.1 y, ante
  ambigüedad —no se sabe la clase, o el mismo archivo podría ser
  `document-drop` o `hard-doc`—, **preguntá al humano y no avances**.
- La guarda de integridad acepta la reubicación **solo** si el contenido queda
  idéntico, el destino es otra casa protegida y el mismo commit deja la entrada
  en el registry de migraciones. Mover un record a mano se rechaza.
- La ruta legada sigue declarada en `records.extra_immutable_paths` hasta que
  el humano decida retirarla: la casa vacía no estorba, y retirarla es su call.

## 5. Cerrar

Correr `doctor` y reportar su veredicto tal cual. Anunciar, en una tabla: qué
capa se tocó, con qué pase, qué quedó **fuera de alcance y por qué**. Eso
mismo quedó escrito en el registry de migraciones — el rastro no es el reporte
al humano, es el record.

## Reglas

- **Rastro doble, siempre** (spec §9.2): entrada en el registry de migraciones
  **y** anotación en el sidecar de cada record afectado. La incisión va al
  sidecar, jamás dentro del verbatim: un byte añadido rompe la cadena `sha256`
  que hace auditable cada afirmación que lo cita.
- **La frescura no es migración.** Un hallazgo vencido o una cadencia cumplida
  piden investigación nueva, no relabel: eso es `check-recurrence` (spec §6), y
  el gate es humano.
- **Cambiar `language` arrastra este mismo trabajo** (spec §1.8): evergreen se
  actualiza, los derivados se regeneran y **los records no se reescriben** — el
  corpus histórico se lee en el idioma en que se escribió.
