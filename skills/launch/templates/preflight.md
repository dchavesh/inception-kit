# Preflight — va al INICIO de todo payload

*Plantilla del kit. `/inception-kit:launch` resuelve `{unit}`, `{runs}`,
`{mode}`, `{context}` y `{language}` y copia el bloque citado tal cual al
principio del payload. No se edita por unidad: si hay que cambiar el ritual, se
cambia acá.*

> ## Preflight — verificá esto ANTES de investigar
>
> En tu primer mensaje, antes de cualquier búsqueda, confirmá con el humano:
>
> 1. **Modo de investigación (Research) activo** en este chat. Si no está
>    activo: detenete y avisá.
> 2. **Payload completo y correcto**: este documento termina en un protocol
>    titulado `# {unit} — <slug>`; si falta una parte, o hay documentos
>    adjuntos que no corresponden a esta unidad: detenete y avisá.
> 3. **Corridas**: esta unidad exige **{runs} run(s)** en modo **{mode}**,
>    etiquetados `run-01`..`run-{runs}`, dentro de este mismo chat.
>    · `independent` = réplicas ciegas: cada run repite la investigación desde
>      el protocol, sin reutilizar hallazgos ni fuentes de los anteriores.
>    · `chained` = partes deliberadas: cada run declara qué continúa o
>      profundiza del anterior; las N son UNA unidad epistémica.
>    Anunciá este plan al humano en una línea.
> 4. **Postura de contexto: `{context}`.** Es lo único que recibiste, y es
>    deliberado.
>    · `scoped` = integración: este payload trae el briefing del plan y los
>      findings vigentes de los `needs` declarados. Nada más existe para vos.
>    · `clean-room` = sala limpia: solo este preflight y el protocol. Si creés
>      que te falta contexto, **eso es el diseño**: la tesis del proyecto no
>      viaja para que tu búsqueda no quede sesgada. No la pidas ni la supongas.
>    En ninguna postura viajan la semilla o tesis del proyecto, la constitution
>    completa, ni reports o raws de otras unidades.
>
> ## Contrato de escritura
>
> - **Etiquetas, siempre en inglés y sin dialecto.** Madurez:
>   `established` · `supported` · `plausible` · `speculative`. Volatilidad:
>   `high` · `medium` · `low`. Toda afirmación lleva una de cada una, con fecha
>   y con su ID de fuente `{unit}-srcNN`. **Sin fuente ⇒ `speculative`**, por
>   definición: es la única madurez que puede ir sin ID de fuente.
> - **Idioma de prosa: `{language}`** (ISO 639-1). Escribí en ese idioma el
>   cuerpo de lo que produzcas. Los nombres de sección, las columnas de tabla,
>   los IDs, los campos y los valores de enum van **siempre en inglés**.
>
> Ante cualquier precondición incumplida: **NO investigues** — avisá y esperá a
> que el humano la resuelva.
