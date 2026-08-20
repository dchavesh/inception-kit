---
id: plan-<slug>-v1
type: plan de investigación
date: <YYYY-MM-DD>
status: draft — mapa pendiente de ratificación
consumer: el coordinador al lanzar cada unidad; el humano ratifica el mapa
---

# Plan de investigación — \<slug\> v1

## Parte I — encuadre y mapa

**Propósito:** qué decisión del proyecto depende de este plan. Citar la
constitution y los ADRs vigentes que lo encuadran.

**Grafo de unidades:**

| ID | Slug | Objetivo (una línea) | Needs | Runs · modo | Context |
|---|---|---|---|---|---|
| | | | | | |

*`context`: `scoped` (integración) o `clean-room` (exploración, competencia de
ideas y toda unidad sensible a falsificación — exige `needs: []`).*

**Reglas de ejecución:** cómo se arma el payload, qué QA aplica al cierre, y
qué corridas exige cada unidad (y por qué).

**Kill criteria globales:** condiciones medibles que detienen el subprograma
entero. Se pre-registran acá — un kill criterion inventado al cerrar no es un
kill criterion.

**Qué produce la síntesis:** los artefactos concretos que el fan-in debe
entregar cuando todas las unidades cierren.

## Parte II — briefing

*El **briefing** es el bloque común que viaja en TODO payload de este plan
(spec §12, G1) — y vive acá, no en un archivo suelto: el protocol lo apunta con
su campo `plan:`. Es el contrato con la sesión: si el formato correcto no sale
de acá, no sale de ningún lado. **La constitution del repo jamás viaja entera
en un payload**; lo que viaja es esto.*

*Sale en el payload de las unidades `scoped`. Una unidad `clean-room` NO lo
recibe: solo preflight + protocol (spec §8.2).*

- **Contexto neutral del proyecto** — qué es, para quién, en qué dominio.
  **Sin semilla, sin tesis, sin la respuesta esperada.**
- **Restricciones ratificadas** que la investigación debe respetar.
- **Reglas de evidencia:** el enum de madurez (`established` · `supported` ·
  `plausible` · `speculative`) y el de volatilidad (`high` · `medium` · `low`),
  la rúbrica de calidad de fuente A–D, y la gramática de IDs de fuente
  (`<unit>-srcNN`). Sin fuente ⇒ `speculative`, por definición. **El payload
  pinnea el enum exacto: la sesión no inventa dialectos ni etiquetas locales.**
- **Formato de salida completo:** las 7 secciones del report y las columnas
  exactas de sus tablas — copiadas de la skill `research-close` de claude.ai,
  que es la que la sesión ejecuta al cerrar.
- **Idioma de prosa:** el que declare `language` en la config. Los nombres de
  sección, columnas, IDs, campos y valores de enum van siempre en inglés.

## Parte III — una sección por unidad

### \<unit-id\> — \<slug\>

**Objetivo:** …
**Áreas:** (a) … (b) … (c) …
**Fuera de alcance:** …
**Kill criteria propios:** …

*(Esta sección se extrae verbatim al `00-protocol.md` de la unidad. Si hay que
cambiar el texto, se cambia acá y se re-extrae — no se parafrasea del otro
lado.)*
