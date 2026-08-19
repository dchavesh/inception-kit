---
name: ingest
description: Ingiere archivos externos (exports de una sesión, documentos recibidos) al inbox con hash y procedencia; borra el original solo tras verificar la copia contra el remoto. Uso — /inception-kit:ingest <rutas>
---

# /inception-kit:ingest \<rutas\>

1. Correr **`ingest <rutas>`**: copia cada archivo al `inbox/` (nombre saneado),
   registra fila con sha256 y origen en el log de ingesta del registry,
   commitea inbox+log, pushea y **verifica contra el remoto** (`git ls-remote`:
   la rama remota debe ser HEAD); recién entonces borra el original, archivo por
   archivo re-verificado por hash — jamás por carpeta.
2. **`--keep`** conserva el original (p. ej. documentación dura cuyo original
   debe vivir fuera del repo). `--remote NOMBRE` si el remoto no es `origin`.
3. Si un nombre colisiona con contenido distinto, el script falla: resolver con
   sufijo de versión (`-v2`), **nunca pisando** — el inbox es inmutable.
4. Si el push o la verificación remota fallan: **nada se borra**. Resolver el
   push y re-correr; los originales siguen en su lugar.
5. Anunciar qué quedó ingerido y borrado. Si los archivos son los exports de
   una unidad, moverlos a donde corresponde (`raw/run-NN.md` los verbatim) y
   sugerir el paso siguiente: `/inception-kit:close UNIT_ID`.
