---
name: inception
description: De una idea cruda a un programa listo para congelar — entrevista de elicitación, idioma de prosa confirmado, repo sembrado, constitution neutral en borrador para el gate humano y protocols R0 en pending. Uso — /inception-kit:inception
---

# /inception-kit:inception

El flujo de entrada de un **proyecto nuevo**: existe una idea y no existe nada
más. Termina con el repo sembrado, la constitution en borrador esperando el gate
humano y las unidades preliminares en `pending` — **listas para congelar, jamás
congeladas acá** (spec §10.2).

**Esta skill no porta ninguna idea de proyecto.** Sus preguntas son
generadoras y aclaradoras, y son las mismas cualquiera sea la idea: no traen
hipótesis, no sugieren mercados, no proponen arquitecturas. Lo que no esté claro
**se le pregunta al humano** — jamás se asume (principio de diseño #2).

## 1. Elicitación — preguntar, no proponer

Entrevista sobre la idea **por vaga que sea**. Preguntas indiferentes al
dominio, en el idioma en que el humano viene escribiendo:

- **Qué decisión depende de esto** y quién la toma. Si no hay decisión que
  cambie, no hay programa que arrancar.
- **Qué está dado y qué está en disputa**: qué se da por cierto hoy, y con qué
  evidencia.
- **Qué haría que la idea NO valga la pena.** Son los kill criteria, y se
  pre-registran ahora: un kill criterion inventado al cerrar no es un kill
  criterion.
- **Dominio y restricciones**: geografía, regulación, plazos, plataforma.
- **Techo de gasto** del programa y **umbrales de QA** que el humano exige.
- **Disparadores** propios: qué evento fuerza re-verificar aunque nada haya
  vencido (spec §6.3).
- **Qué NO es esto** — el fuera de alcance explícito.

Devolver lo entendido **en una lista corta y pedir corrección**. Una elicitación
que el humano no corrigió es una elicitación que nadie leyó.

## 2. Confirmar `language` — ANTES del primer artefacto

Preguntar en qué idioma escribe el equipo la **prosa** del corpus, y declararlo
en `framework.config.yaml` (`language:`, ISO 639-1). El kit arranca en `en`.

Se hace acá y no después porque **cambiar `language` con artefactos ya escritos
es migración, no edición** (spec §1.8): los evergreen se actualizan, los
derivados se regeneran y los records **no se reescriben** — el corpus histórico
se lee en el idioma en que nació.

La frontera es dura y no se negocia: nombres de skill y comando, campos de
contrato, claves de config, **valores de enum**, etiquetas, marks, columnas de
tabla e IDs van **siempre en inglés**. En `language` va el cuerpo de los
documentos y lo que las skills le dicen al humano.

## 3. Sembrar el repo

`kit-init` — idempotente. Siembra la config ancla, las casas de spec §5, los
nueve registries como datos con sus vistas, el hook de inmutabilidad y su shim.
Ajustar `language:` en la config **en este momento**, si el humano declaró otro.

Los números del **bloque ratificado** (`horizons`, `runs`, `ids`, `metrics`,
`context`) quedan en la config con los defaults del kit: el humano los ratifica
—o los cambia— en el gate del paso siguiente, y desde entonces tocarlos es una
enmienda (spec §12 G4).

## 4. Constitution neutral → **GATE HUMANO**

Redactar `<research>/constitution.md` con `templates/constitution.md` de esta
skill: supuestos refutables, dominio, techo de gasto, umbrales de QA,
disparadores y jerarquía de independencia. `version: 1`, `status: draft`,
changelog de enmiendas vacío.

- **Neutral quiere decir sin la semilla.** La constitution gobierna el repo; no
  contiene la tesis del proyecto ni la respuesta esperada, porque lo que
  gobierna tiene que sobrevivir a que la idea se caiga. Y jamás viaja entera en
  un payload: lo que viaja es el briefing (spec §12 G1, §8.2).
- **Los horizontes de caducidad NO se escriben acá**: viven en la config y la
  constitution los **apunta** (spec §12 G4). Dos casas para el mismo número es
  el drift que el framework existe para evitar.
- Estructurada para ser compatible con la **constitution de desarrollo** que la
  síntesis sembrará más adelante.

**Parar y presentar el gate.** El humano ratifica el borrador **y** los valores
del bloque ratificado tal como están en la config. Consumido el gate:
`registry add gates --gate constitution-ratification --decision «…»
--record_out «constitution.md v1»`, y recién entonces `status: ratified`.

## 5. Unidades R0 — las que deciden si el programa va

Las unidades preliminares llevan la **convención de fase** de spec §1.3:
`X00` más sufijo alfabético (`r00a`, `r00b`, …). `X01+` es el programa, y no se
planifica todavía: se planifica cuando las R0 hayan hablado.

Su objetivo es uno solo, y es el que hace de esta fase una fase: **validar la
idea — continuar, pivotar o descartar**. Cada R0 lleva por eso kill criteria
propios que resuelven a una de esas tres salidas.

- **`context: clean-room`** por defecto en esta etapa: son exploración y son
  sensibles a falsificación — conocer la tesis sesgaría la búsqueda. Exige
  `needs: []`, y una R0 que necesita findings ajenos no es una R0 (spec §8.3).
- El mapa y el briefing se escriben con **`/inception-kit:plan`**, que es donde
  vive esa mecánica: mapa en la Parte I, briefing en la Parte II, una sección
  por unidad en la Parte III, y protocols extraídos verbatim en `pending`.
- **Anti-sprawl:** ninguna R0 sin un objetivo que cambie una decisión concreta.
  Si un documento existente ya responde la pregunta, no es una unidad: es una
  fuente, y entra por `/inception-kit:ingest`.

## 6. Cerrar el flujo

`derive-status`, `derive-index` y `doctor`. Reportar el veredicto tal cual.

Entregar al humano, en una tabla: qué R0 quedaron en `pending`, qué decide cada
una, y **los gates pendientes en orden** — ratificar el mapa →
`freeze-protocols --confirm` a su orden → `/inception-kit:launch`. Cada gate que
se consuma deja su fila con `registry add gates`.

## Reglas

- **El freeze es orden humana.** Esta skill jamás corre `freeze-protocols`, y
  jamás lanza.
- **La semilla nunca viaja.** Ni en el briefing, ni en un payload, ni en un
  protocol: lo que la sesión recibe es la pregunta, no la respuesta esperada.
- **Nada se asume.** Si falta un número, un umbral o un límite, se pregunta. Un
  default inventado por la skill es lógica de negocio contrabandeada.
- **La prosa va en `language`**; los campos, enums, IDs y columnas, en inglés.
- Si el repo ya tiene corpus, esta no es la puerta: un corpus artesanal entra
  por **`/inception-kit:adopt`** y un repo con documentación existente por
  **`/inception-kit:normalize`**.
