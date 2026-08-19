---
name: status
description: Regenera y muestra el tablero derivado del programa + caducidad de hallazgos + integridad del repo, y cierra con la próxima acción concreta. Uso — /inception-kit:status
---

# /inception-kit:status

1. **`derive-status`** — regenera el tablero desde los frontmatter de los
   protocols (jamás se edita a mano) y lo muestra.
2. **`derive-review-by`** — resumir hallazgos vigentes vs vencidos. Si hay
   vencidos: refrescar o degradar un nivel de madurez, **jamás lavar**.
3. **`doctor`** — reportar su veredicto en una línea; si falla, listar los
   problemas tal cual y no maquillar ninguno.
4. **Cerrar con la próxima acción concreta:** qué unidad está lanzable, cuál
   quedó a medio cerrar, y qué **gate humano** está pendiente. Un gate
   pendiente se nombra: no se resuelve acá.
