---
name: status
description: Regenera y muestra las vistas derivadas del repo (tablero e índice puerta-de-entrada) + caducidad y recurrencia + integridad, y cierra con la próxima acción concreta. Uso — /inception-kit:status
---

# /inception-kit:status

1. **`derive-status`** — regenera el tablero desde los frontmatter de los
   protocols (jamás se edita a mano) y lo muestra.
2. **`derive-index`** — regenera el índice puerta-de-entrada: estado, decisiones
   vigentes, conflictos abiertos, síntesis vigente y dónde vive cada cosa, en
   una página. También derivado, también jamás a mano.
3. **`check-recurrence`** — qué `review_by` venció y qué cadencia `refresh:` se
   cumplió, con las relanzamientos que **propone**. Nombrar las propuestas; no
   ejecutar ninguna: el gate es humano. Vencido sin re-verificar baja un nivel
   de madurez — jamás se lava.
4. **`doctor`** — reportar su veredicto en una línea; si falla, listar los
   problemas tal cual y no maquillar ninguno. Si aparece `kit_version`
   desincronizado, eso es **error**: correr `kit-init` y `/inception-kit:migrate`.
5. **Cerrar con la próxima acción concreta:** qué unidad está lanzable, cuál
   quedó a medio cerrar, y qué **gate humano** está pendiente. Un gate
   pendiente se nombra: no se resuelve acá.
