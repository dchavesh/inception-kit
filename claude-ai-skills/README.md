# Skills de claude.ai

Las tres skills que corren **del otro lado de la frontera**: en el chat de
claude.ai donde vive la sesión de investigación, no en el repo. El kit no puede
instalarlas — Claude Code y claude.ai son cuentas distintas —, así que el
humano las copia una vez y quedan disponibles para todas las sesiones.

| Skill | Cuándo se invoca | Qué hace |
|---|---|---|
| `research-preflight` | primer mensaje del chat, **antes** de investigar | verifica modo Research, payload completo y plan de corridas; se detiene ante cualquier fallo |
| `new-run` | entre corridas | marca el límite `run-{k}` y aplica el modo declarado (`independent` = réplica ciega · `chained` = parte deliberada) |
| `research-close` | antes de cerrar el chat | genera los tres documentos de cierre: report en plantilla estricta, borrador de findings y bitácora de búsquedas |

## Instalación (una vez por cuenta de claude.ai)

1. Entrar a claude.ai → **Settings → Capabilities → Skills** → *Create skill*.
2. Por cada carpeta de acá (`research-preflight/`, `research-close/`,
   `new-run/`): copiar el contenido de su `SKILL.md` — **incluido el
   frontmatter** (`name`, `description`), que es lo que decide cuándo se
   activa.
3. Verificar que las tres aparecen habilitadas antes de lanzar una unidad:
   `/inception-kit:launch` le dice a la sesión que las use.

## Reglas

- **El contrato viaja en el payload, jamás en la skill.** Cuántas corridas, en
  qué modo y qué investigar sale del payload que arma `/inception-kit:launch`.
  Estas skills son mecánica de proceso: ritual de arranque, límite entre
  corridas y formato de cierre. Si una empieza a portar contenido del proyecto,
  está mal escrita.
- **Se actualizan con el kit.** Son parte de la versión: al subir el kit,
  re-copiar las que hayan cambiado (el `CHANGELOG.md` lo dice).
- **Etiquetas `run-01..run-NN`.** `C1`/`C2` es vocabulario histórico del corpus
  viejo: se lee con glosario, jamás se emite.
- **Enum en inglés, sin dialecto** (desde el kit 0.2.0): madurez `established` ·
  `supported` · `plausible` · `speculative`; volatilidad `high` · `medium` ·
  `low`. Sin fuente ⇒ `speculative`, por definición. El payload pinnea el enum
  exacto: la sesión no inventa etiquetas locales.
- **Idioma.** Nombres de sección, columnas, IDs, campos y valores de enum van
  **siempre en inglés**; la prosa, en el idioma que el payload declare
  (`language`). Hay **una sola versión** de cada skill: jamás copias traducidas.
