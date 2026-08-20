---
id: <unit-id>
slug: <slug-corto-kebab>
status: pending
needs: []
inputs: []
plan: <ruta del plan al que pertenece — de ahí sale el Bloque Común del payload>
runs: 2
mode: independent
context: scoped
refresh: null
constitution: null
session: null
---

# <unit-id> — <slug-corto-kebab>

**Objetivo:** una sola línea que enuncie qué decisión cambia esta unidad.

**Áreas:** (a) … (b) … (c) … — las áreas de búsqueda, sin tesis ni respuesta
esperada.

**Fuera de alcance:** qué NO cubre y qué unidad lo cubre.

**Kill criteria propios:** condiciones medibles que, de cumplirse, detienen la
unidad y disparan gate humano.

<!--
Frontmatter — qué es cada campo:

  id / slug     llave estable + nombre legible. Jamás se renumeran ni se
                reutilizan; el significado vive en el slug y el índice, nunca
                dentro del id.
  status        pending → frozen → running → qa → done. Solo hacia adelante.
                `pending` es lo único editable: desde `frozen` el cuerpo es
                record y el hook lo hace cumplir.
  needs         unidades cuyo `02-findings` vigente viaja en el payload. Mínimos:
                el payload crece con cada uno.
  inputs        material externo ya ingerido que la unidad consume.
  plan          documento cuyo Bloque Común (Parte II) viaja en el payload.
  runs / mode   contrato de corridas: N réplicas ciegas (`independent`) o N
                partes de una sola unidad epistémica (`chained`). Etiquetas
                run-01..run-NN en ambos modos. Si se omiten, rigen los defaults
                de framework.config.yaml.
  context       postura de contexto: qué viaja en el payload.
                  scoped     — preflight + briefing + findings vigentes de sus
                               `needs` + protocol.
                  clean-room — preflight + protocol, NADA MÁS. Exige `needs: []`
                               y es la postura de exploración, competencia de
                               ideas y toda unidad sensible a falsificación.
                Si se omite, rige `context.default` de la config.
  refresh       cadencia de re-ejecución, `<N><w|m|y>` (p. ej. `18m`). Opcional.
                Se declara la CADENCIA, jamás la fecha: la fecha se deriva de la
                cadencia más el último cierre. Al cumplirse, toca una corrida o
                versión nueva que SUPERSEDE a la vencida — nunca una edición.
                `check-recurrence` la vigila y propone; el gate es humano.
  constitution  versión de la constitution vigente al lanzar. Lo sella /launch;
                es procedencia de las reglas bajo las que corrió, no lo que la
                unidad leyó (eso lo evidencia el payload.md sellado).
  session       URL del chat. Lo sella /launch; es la prueba de qué corrió dónde.

El cuerpo se redacta en el idioma que declare `language` en la config; los
campos, valores de enum y etiquetas van siempre en inglés.
-->
