---
name: research-close
description: Cierre de una sesión de investigación del inception-framework — genera los TRES documentos de cierre (report en plantilla estricta, borrador de findings, bitácora de búsquedas). Invocar ANTES de cerrar el chat, con las N corridas declaradas completas.
---

# research-close

Antes de cerrar esta sesión, generá los TRES documentos de cierre de la unidad (usá el `id` del protocol recibido, p. ej. `rNN`), como tres markdown descargables separados. Consolidá SOLO lo investigado en esta sesión — sin investigación nueva, sin rellenar huecos de memoria. Si las N corridas declaradas no están completas: avisá antes de generar (la desviación quedará anotada por el coordinador).

**Idioma.** Los nombres de sección, las columnas de tabla, los IDs, los campos del frontmatter y los valores de enum van **siempre en inglés**, exactamente como están acá. La **prosa** —lo que escribís debajo de cada encabezado y dentro de las celdas— va en el idioma que el preflight del payload declaró (`language`). Si el payload no lo declara, preguntá; no lo adivines.

## Documento 1 — `01-report.md` (informe completo). Estructura EXACTA:

```
---
id: rNN-report
unit: rNN
date: AAAA-MM-DD
---
## 1. Summary                      (máximo 1 página)
## 2. Findings by area
## 3. Sources
## 4. Contradictions
## 5. Design implications
## 6. Gaps and open questions
## 7. Requirements table
```

Reglas duras:

- En §2, CADA afirmación es un ítem de lista y termina con su etiqueta y fuente: `- **Afirmación.** (maturity · volatility · AAAA-MM) — rNN-srcNN`. Maturity: `established` / `supported` / `plausible` / `speculative` (**sin fuente = `speculative`**, y solo entonces puede ir sin src-ID). Volatility: `high` / `medium` / `low`. Siempre con año. **El enum es el del payload y no admite dialecto**: nada de abreviaturas, sinónimos ni etiquetas locales. Si hubo varios runs, conservá la **atribución por run** (`run-01`, `run-02`…) en cada afirmación.
- §3 es una tabla con columnas EXACTAS: `| ID | Title | Author/Org | Date | Type | Quality | Volatility |`. IDs con gramática `rNN-src01, rNN-src02…` (dos dígitos, sin huecos); Quality = una letra A–D (rúbrica del briefing); URL dentro de Title o Type si la tenés; si no quedó registrada, escribí "URL n/r" — jamás la reconstruyas de memoria.
- §7 es una tabla con columnas EXACTAS y sin celdas vacías: `| ID | Requirement | Why | Evidence & maturity | Core or Playbook | Area |`. IDs `rNN-req01, rNN-req02…` (Core = invariante; Playbook = específico de fuente/sector). Evidence siempre con su nivel de maturity; si no hay evidencia: "sin evidencia" + `speculative`.
- §4: contradicciones entre fuentes **o entre runs** reportadas como conflicto, sin resolverlas en silencio. Una sesión **no adjudica** contradicciones entre sus propios runs: reportá las dos versiones — el peso lo asigna el coordinador o el humano.

## Documento 2 — `02-findings.md` (borrador de síntesis, máximo 2 páginas)

Los 5–10 hallazgos que más cambian una decisión de diseño, numerados: `1. **Título.** Desarrollo breve. (maturity · volatility · AAAA-MM-DD)`. Cerrá con: tablas-insumo que quedan en el report (solo referencia) y los huecos clave.

## Documento 3 — `03-sources.md` (bitácora de búsqueda)

- Las consultas con texto EXACTO registrado, en tabla: `| # | Query verbatim | Result (hallazgo/ausencia) |`.
- Lo que no tenga string exacto conservado: listalo como "accesos reportados", separado y declarado como limitación — no reconstruyas consultas de memoria.
- Fallas de acceso (404, paywall, bloqueo) registradas como eventos.
