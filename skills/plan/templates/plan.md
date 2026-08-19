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

| ID | Slug | Objetivo (una línea) | Needs | Runs · modo |
|---|---|---|---|---|
| | | | | |

**Reglas de ejecución:** cómo se arma el payload, qué QA aplica al cierre, y
qué corridas exige cada unidad (y por qué).

**Kill criteria globales:** condiciones medibles que detienen el subprograma
entero. Se pre-registran acá — un kill criterion inventado al cerrar no es un
kill criterion.

**Qué produce la síntesis:** los artefactos concretos que el fan-in debe
entregar cuando todas las unidades cierren.

## Parte II — Bloque Común

*Esto es lo que viaja en TODO payload de este plan. Es el contrato con la
sesión: si el formato correcto no sale de acá, no sale de ningún lado.*

- **Contexto neutral del proyecto** — qué es, para quién, en qué dominio.
  **Sin semilla, sin tesis, sin la respuesta esperada.**
- **Restricciones ratificadas** que la investigación debe respetar.
- **Reglas de evidencia:** niveles de madurez y de volatilidad, rúbrica de
  calidad de fuente A–D, y la gramática de IDs de fuente (`<unit>-srcNN`).
- **Formato de salida completo:** las 7 secciones del report y las columnas
  exactas de sus tablas — copiadas de la skill `research-close` de claude.ai,
  que es la que la sesión ejecuta al cerrar.

## Parte III — una sección por unidad

### \<unit-id\> — \<slug\>

**Objetivo:** …
**Áreas:** (a) … (b) … (c) …
**Fuera de alcance:** …
**Kill criteria propios:** …

*(Esta sección se extrae verbatim al `00-protocol.md` de la unidad. Si hay que
cambiar el texto, se cambia acá y se re-extrae — no se parafrasea del otro
lado.)*
