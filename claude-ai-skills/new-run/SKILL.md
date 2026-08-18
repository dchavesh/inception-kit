---
name: new-run
description: Marca el inicio de una nueva corrida (C2, C3…) dentro de la misma sesión de investigación del inception-framework, según el modo declarado en el payload (independent o chained). Invocar entre corridas.
---

# new-run

1. **Anunciá el límite** en el chat: `=== Inicio de C{k} ({modo}) ===`, con el modo que el payload declaró.
2. **Si el modo es `independent`** — C{k} es una réplica ciega: no reutilicés hallazgos, fuentes ni conclusiones de las corridas anteriores; repetí la investigación desde el protocol con ojos frescos. Las convergencias y contradicciones entre corridas se evalúan al cierre, no durante.
3. **Si el modo es `chained`** — C{k} construye deliberadamente sobre lo anterior: declará en una línea qué parte del tema cubre o qué hallazgo previo profundiza/enfatiza, y seguí desde ahí.
4. **En ambos modos:** etiquetá todo hallazgo de esta corrida con C{k} (la atribución por corrida viaja al cierre) y decile al humano cuántas corridas quedan del plan declarado.

No cierres la sesión sin completar las N corridas declaradas — si el humano pide cerrar antes, recordale el plan y que la desviación quedará anotada por el coordinador. Esta skill es mecánica de proceso: el contrato (N y modo) viaja en el payload, jamás acá.
