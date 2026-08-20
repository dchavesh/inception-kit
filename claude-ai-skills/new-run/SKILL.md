---
name: new-run
description: Marca el inicio de un nuevo run (run-02, run-03…) dentro de la misma sesión de investigación del inception-framework, según el modo declarado en el payload (independent o chained). Invocar entre runs.
---

# new-run

1. **Anunciá el límite** en el chat: `=== Inicio de run-{k} ({mode}) ===`, con el modo que el payload declaró.
2. **Si el modo es `independent`** — run-{k} es una réplica ciega: no reutilicés hallazgos, fuentes ni conclusiones de los runs anteriores; repetí la investigación desde el protocol con ojos frescos. Las convergencias y contradicciones entre runs se evalúan al cierre, no durante.
3. **Si el modo es `chained`** — run-{k} construye deliberadamente sobre lo anterior: declará en una línea qué parte del tema cubre o qué hallazgo previo profundiza/enfatiza, y seguí desde ahí.
4. **En ambos modos:** etiquetá todo hallazgo de este run con `run-{k}` (la atribución por run viaja al cierre), con su maturity (`established` / `supported` / `plausible` / `speculative`) y volatility (`high` / `medium` / `low`) en inglés y sin dialecto, y decile al humano cuántos runs quedan del plan declarado.

No cierres la sesión sin completar los N runs declarados — si el humano pide cerrar antes, recordale el plan y que la desviación quedará anotada por el coordinador. Esta skill es mecánica de proceso: el contrato (N y modo) viaja en el payload, jamás acá.
