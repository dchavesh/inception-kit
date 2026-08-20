---
name: research-preflight
description: Ritual de arranque de una sesión de investigación del inception-framework — verifica las precondiciones (modo Research, payload completo, plan de corridas) y se detiene ante cualquier fallo. Invocar al inicio del chat, ANTES de investigar.
---

# research-preflight

Ejecutá este ritual en tu primer mensaje, antes de cualquier búsqueda:

1. **Modo Research activo.** Si este chat no tiene el modo de investigación activado, detenete y avisale al humano — no investigues sin él (es la causa histórica de sesiones duplicadas).
2. **Payload completo y correcto.** El payload pegado debe terminar en un protocol titulado `# rNN — <slug>` y traer su bloque de preflight al inicio. Si no hay payload, falta una parte, o hay documentos adjuntos que no corresponden a esta unidad: detenete y avisá.
3. **Plan de runs anunciado.** Leé del payload cuántos runs exige la unidad (`runs: N`) y en qué modo:
   - `independent` — réplicas ciegas `run-01..run-NN`: cada run repite la investigación desde el protocol sin reutilizar hallazgos ni fuentes de los anteriores.
   - `chained` — partes deliberadas `run-01..run-NN`: cada run construye sobre el anterior (tema amplio por partes, o énfasis en lo recién hallado).
   Anunciá el plan al humano en una línea ("esta sesión exige N runs en modo X"). Si el payload no lo declara: preguntá y esperá la respuesta — no asumás. (En records históricos del corpus verás "C1/C2" — vocabulario viejo por "corrida"; el vigente es `run-NN`.)
4. **Postura de contexto.** El preflight declara `context: scoped | clean-room`. En `clean-room` recibiste solo el preflight y el protocol, y eso es **deliberado**: la tesis del proyecto no viaja para que tu búsqueda no quede sesgada. No la pidas, no la supongas y no la reconstruyas.
5. **Contrato de etiquetas e idioma.** Maturity `established` / `supported` / `plausible` / `speculative`; volatility `high` / `medium` / `low` — **en inglés y sin dialecto**, tal como los pinnea el payload. La prosa la escribís en el idioma que el payload declare (`language`).

Ante cualquier precondición incumplida: **NO investigues** — avisá y esperá a que el humano la resuelva. Esta skill no porta reglas de la investigación misma: esas viajan en el payload, que es el contrato.
