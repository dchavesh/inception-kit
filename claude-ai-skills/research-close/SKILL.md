---
name: research-close
description: Cierre de una sesión de investigación del inception-framework — genera los TRES documentos de cierre (report en plantilla estricta, borrador de findings, bitácora de búsquedas). Invocar ANTES de cerrar el chat, con las N corridas declaradas completas.
---

# research-close

Antes de cerrar esta sesión, generá los TRES documentos de cierre de la unidad (usá el `id` del protocol recibido, p. ej. `rNN`), como tres markdown descargables separados. Consolidá SOLO lo investigado en esta sesión — sin investigación nueva, sin rellenar huecos de memoria. Si las N corridas declaradas no están completas: avisá antes de generar (la desviación quedará anotada por el coordinador).

## Documento 1 — `01-report.md` (informe completo). Estructura EXACTA:

```
---
id: rNN-report
unit: rNN
date: AAAA-MM-DD
---
## 1. Resumen        (máximo 1 página)
## 2. Hallazgos por área
## 3. Fuentes
## 4. Contradicciones detectadas
## 5. Implicaciones de diseño
## 6. Huecos y preguntas abiertas
## 7. Tabla consolidada de requisitos
```

Reglas duras:

- En §2, CADA afirmación es un ítem de lista y termina con su etiqueta y fuente: `- **Afirmación.** (madurez · volatilidad · AAAA-MM) — rNN-srcNN`. Madurez: establecido / respaldado / plausible / especulativo (sin fuente = especulativo, y solo entonces puede ir sin src-ID). Volatilidad: alta / media / baja. Siempre con año. Si hubo varias corridas, conservá la **atribución por corrida** (C1, C2…) en cada afirmación.
- §3 es una tabla con columnas EXACTAS: `| ID | Título | Autor/Org | Fecha | Tipo | Calidad | Volatilidad |`. IDs con gramática `rNN-src01, rNN-src02…` (dos dígitos, sin huecos); Calidad = una letra A–D (rúbrica del Bloque Común); URL dentro de Título o Tipo si la tenés; si no quedó registrada, escribí "URL n/r" — jamás la reconstruyas de memoria.
- §7 es una tabla con columnas EXACTAS y sin celdas vacías: `| ID | Requirement | Why | Evidence & maturity | Core or Playbook | Area |`. IDs `rNN-req01, rNN-req02…` (Core = invariante; Playbook = específico de fuente/sector). Evidence siempre con madurez; si no hay evidencia: "sin evidencia" + especulativo.
- §4: contradicciones entre fuentes **o entre corridas** reportadas como conflicto, sin resolverlas en silencio.

## Documento 2 — `02-findings.md` (borrador de síntesis, máximo 2 páginas)

Los 5–10 hallazgos que más cambian una decisión de diseño, numerados: `1. **Título.** Desarrollo breve. (madurez · volatilidad · AAAA-MM-DD)`. Cerrá con: tablas-insumo que quedan en el report (solo referencia) y los huecos clave.

## Documento 3 — `03-sources.md` (bitácora de búsqueda)

- Las consultas con texto EXACTO registrado, en tabla: `| # | Consulta verbatim | Resultado (hallazgo/ausencia) |`.
- Lo que no tenga string exacto conservado: listalo como "accesos reportados", separado y declarado como limitación — no reconstruyas consultas de memoria.
- Fallas de acceso (404, paywall, bloqueo) registradas como eventos.
