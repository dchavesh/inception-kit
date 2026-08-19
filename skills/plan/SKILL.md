---
name: plan
description: Diseña un plan de investigación (mapa de unidades + Bloque Común + protocols en pending) desde una necesidad de conocimiento, listo para el gate humano de ratificación. Uso — /inception-kit:plan <necesidad u objetivo>
---

# /inception-kit:plan \<necesidad\>

Convierte una necesidad de conocimiento en un plan ejecutable bajo el
framework. **El plan que produce queda en draft: el mapa lo ratifica el humano
y el freeze es su orden — esta skill jamás congela ni lanza.**

## Pasos

1. **Anti-duplicación primero.** Inventariar qué ya está respondido: findings
   vigentes de las unidades `done`, la RTM, los ADRs y los conflictos abiertos.
   Lo ya investigado **se consume vía `needs`**, jamás se re-investiga (una
   ausencia documentada es evidencia, no un defecto). Listar explícitamente
   "ya cubierto por \<unit\>" vs "genuinamente sin decidir".
2. **Delimitar las preguntas sin decidir** y agruparlas en unidades chicas:
   3–6 por subprograma; **una unidad = una sesión = un objetivo enunciable en
   una línea**. Asignar clase según los prefijos que declare
   `ids.classes` de `framework.config.yaml`; si hace falta una clase nueva, es
   decisión del humano y entra por config con su entrada de glosario. Los IDs
   siguen el ancho configurado, jamás se renumeran y jamás se reutilizan.
3. **Escribir el plan** en `<research>/plan-<slug>-v1.md` con
   `templates/plan.md` de esta skill (frontmatter con
   `status: draft — mapa pendiente de ratificación`).
4. **Extraer los protocols** desde la Parte III del plan — **verbatim, sin
   parafrasear** — a `<investigations>/<id>-<slug>/00-protocol.md`, usando
   `templates/protocol.md`. Frontmatter completo, `status: pending`.
5. **Correr `derive-status`.** El tablero debe mostrar las nuevas como
   "ready — falta freeze (gate humano)" o "espera a …".
6. **Entregar al humano:** el mapa en una tabla, qué queda ready tras el freeze,
   y los gates pendientes en orden (ratificar mapa → `freeze-protocols
   --confirm` a su orden → `/inception-kit:launch`). Commit del plan y los
   protocols en draft/pending.

## Reglas

- **Anti-sprawl:** ninguna unidad sin un objetivo que cambie una decisión
  concreta. Si un documento u OSS existente ya responde la pregunta, no es una
  unidad: es una fuente.
- **`needs` mínimos:** solo lo que la unidad de verdad consume — el payload
  crece con cada uno.
- **Sin lógica de proyecto en las preguntas:** lo que no esté claro se ratifica
  con el humano mediante preguntas generadoras, nunca se asume.
- **Los encadenamientos se declaran en el plan** (`mode: chained`), no se
  improvisan al lanzar.
- Unidades sensibles a falsificación llevan payload mínimo: solo el protocol,
  sin briefing (la semilla nunca viaja).
