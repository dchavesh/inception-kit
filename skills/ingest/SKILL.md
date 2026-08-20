---
name: ingest
description: Ingiere material externo al repo declarando su destino obligatorio (unidad, clase sin unidad, o documentación dura), con hash y procedencia; borra el original solo tras verificar la copia contra el remoto. Uso — /inception-kit:ingest <rutas>
---

# /inception-kit:ingest \<rutas\>

**El único staging es externo al repo.** El material espera afuera — la carpeta
de descargas del humano, el adjunto sin abrir, el export recién bajado — y el
repo **no tiene bandeja de entrada**. La clasificación ocurre **al ingerir**, no
después: toda ingesta declara su destino, y hay exactamente tres (spec §2.6).

## 1. Resolver el destino ANTES de correr nada

| Destino | Cuándo aplica | Comando |
|---|---|---|
| **unidad** | el verbatim de una corrida | `ingest <archivo> --unit UNIT_ID --run N` → `<unit>/raw/run-NN.md` |
| **unidad** | otro bronze recogido por esa unidad (audio, foto, PDF) | `ingest <archivo> --unit UNIT_ID --class <clase>` → `<unit>/raw/` + sidecar |
| **clase sin unidad** | tiene clase de fuente pero no pertenece a ninguna unidad | `ingest <archivo> --class <clase>` → `<research>/evidence/<clase>/` + sidecar |
| **documentación dura** | documentos oficiales, licencias, contratos, archivos clave | `ingest <archivo> --hard-doc [--keep]` → `paths.hard_docs` |
| **documentación dura afuera** | su tamaño o su licencia exigen que viva fuera del repo | `ingest <archivo> --hard-doc --external <puntero>` → sidecar con puntero + sha256 |

Las clases son el enum cerrado de la spec §2.1: `research-run`,
`field-interview`, `form-batch`, `document-drop`, `media`, `hard-doc`. **No hay
carpeta de sobrantes**: `evidence/misc/` y equivalentes están prohibidos.

**Ante ambigüedad, PREGUNTÁ AL HUMANO y no avances.** Si no sabés la unidad, no
sabés la clase, o el mismo archivo podría ser `document-drop` o `hard-doc`: la
operación se detiene. Nunca elijas por defecto — adivinar la casa es el drift
que el destino obligatorio existe para impedir. El script también se planta:
sin destino declarado, falla y no toca nada.

## 2. Correr y verificar

`ingest` hace, EN ORDEN: copia al destino (nombre saneado) → sidecar de
procedencia donde corresponde → fila con sha256, clase y origen en el log de
ingesta → commit → push → **verificación contra el remoto** (`git ls-remote`: la
rama remota debe ser HEAD) → recién entonces borra el original, archivo por
archivo re-verificado por hash, jamás por carpeta.

- **`--keep`** conserva el original cuando debe seguir viviendo afuera (el caso
  normal de `hard-doc`). `--external` lo implica: el binario que vive fuera es
  la única copia, y la documentación dura **jamás se borra**.
- **`--license`, `--consent`, `--method`** se escriben al sidecar cuando aplican.
  El sidecar es record y vive en casa protegida: lo que no se declara ahora
  entra después como archivo nuevo, no como edición.
- **`--remote NOMBRE`** si el remoto no es `origin`.
- Si un nombre colisiona con contenido distinto, el script falla: resolver con
  sufijo de versión (`-v2`), **nunca pisando** — el bronze es inmutable.
- **Si el push o la verificación remota fallan: nada se borra.** Resolver el
  push y re-correr; los originales siguen en su lugar.

## 3. Después

Anunciar qué quedó ingerido, dónde aterrizó y qué se borró. Si eran los exports
de una unidad, ya están en `raw/run-NN.md`: **nadie los mueve** — el paso
siguiente es `/inception-kit:close UNIT_ID`, que solo verifica que existan los N
raws del contrato.

Un `inbox/` legado de un repo adoptado es **bronze congelado**: se lee y se
cita, jamás se reescribe, y no recibe nada nuevo. Reconciliarlo con las casas
reales es trabajo de `/migrate`.
