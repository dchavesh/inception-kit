---
name: synthesis
description: Pre-flight de la síntesis (diagnóstico PASS/FAIL sobre el programa) y, SOLO con orden humana explícita, el fan-in que convierte evidencia en decisiones. Uso — /inception-kit:synthesis [preflight]
---

# /inception-kit:synthesis

Sintetizar sobre un repo inconsistente produce un diseño no rastreable. El
pre-flight es **diagnóstico puro**; **la síntesis misma es gate humano** —
jamás arranca sin orden explícita, y sus decisiones son todas del humano.

## Pre-flight (siempre primero, siempre completo)

| # | Chequeo | Cómo |
|---|---|---|
| 1 | **Unidades cerradas** | `derive-status`: toda unidad del alcance de la síntesis en `done` |
| 2 | **IDs únicos** | `doctor`: sin `<unit>-srcNN`, `<unit>-reqNN` ni `con-NN` duplicados |
| 3 | **Conflictos anotados** | toda contradicción con su fila en el registry de conflictos; ninguna resuelta por fuera. Un conflicto abierto no bloquea, pero **toda decisión que dependa de él se marca como condicionada** a su gate |
| 4 | **Findings escritos** | `02-findings` vigente en todas las unidades |
| 5 | **Kill criteria** | ningún disparo sin resolver |
| 6 | **Caducidad** | `derive-review-by`: nada vencido entra lavado — se refresca o entra degradado un nivel de madurez |
| 7 | **Constitution ratificada** | fuera de draft, con sus números fijados por el humano. **Draft ⇒ FAIL bloqueante** |

**Salida:** una tabla PASS/FAIL y, por cada FAIL, qué falta exactamente y quién
lo resuelve. Nada más — el pre-flight no arregla, diagnostica.

## Síntesis (solo tras PASS total y orden humana explícita)

Fan-in sobre las unidades del alcance, respetando la **jerarquía de
independencia** que declare la constitution: las unidades ciegas y replicadas
pesan más que las contextuales o encadenadas; un conjunto `chained` cuenta como
UNA unidad epistémica.

Produce: resolución de conflictos (o decisiones explícitamente condicionadas al
gate que falta), población de la RTM, ADRs nuevos, y los documentos de diseño
que el programa pedía. Todo con trazabilidad al `<unit>-reqNN` o al hallazgo
que lo sostiene.

**Nada de esto se commitea sin revisión humana del resultado.** Si la síntesis
supera una síntesis anterior, entra por supersesión declarada — jamás
editando la vieja.

**La síntesis misma es gate humano**, y como todo gate consumido deja su fila en
`registry/gates.md`: cuál, cuándo, qué se decidió y qué enmendó.
