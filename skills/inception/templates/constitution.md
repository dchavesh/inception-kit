---
id: constitution
type: constitution
version: 1
status: draft — pendiente de ratificación (gate humano)
date: <YYYY-MM-DD>
consumer: el humano en los gates; el coordinador al comisionar unidades
reading-moment: antes de todo gate y antes de congelar unidades
---

# Constitution — \<proyecto\>

*Clase **constitution** (spec §4.3): evergreen con **protocolo de enmienda
duro**. Toda modificación sube `version:`, agrega su fila al changelog del final
y la ratifica el humano. No hay corrección exenta: si el texto normativo cambia,
la versión cambia.*

## 1. Dominio y alcance

Qué gobierna esta constitution: el dominio del programa, su geografía y su
horizonte temporal. Qué queda **explícitamente fuera**.

*Sin la semilla.* Acá va lo que gobierna, no la idea que se está validando: lo
que gobierna tiene que seguir siendo verdadero aunque la idea se caiga, y la
tesis del proyecto **jamás viaja en un payload** (spec §8.2).

## 2. Supuestos refutables

Cada supuesto con **qué evidencia lo refutaría**. Un supuesto que ninguna
evidencia puede tumbar no es un supuesto: es una creencia, y no gobierna nada.

| # | Supuesto | Qué lo refutaría | Estado |
|---|---|---|---|
| 1 | | | vigente |

## 3. Techo de gasto

El límite del programa —corridas, presupuesto, tiempo— y qué pasa al tocarlo:
quién decide si se amplía y con qué evidencia. Un techo sin consecuencia
declarada no es un techo.

## 4. Umbrales de QA

Los mínimos que un cierre debe alcanzar para pasar el gate de QA (spec §10.2
pasos 1–2): porcentaje de afirmaciones con fuente válida, tasa de eco tolerada,
qué dispara STOP. Se miden, no se estiman — lo no medido se declara con su
token.

## 5. Disparadores de re-verificación

Condiciones fechadas o eventuales que fuerzan re-verificar **aunque el horizonte
no haya vencido** (spec §6.3): la entrada en vigor de una norma que sustituye a
la citada, un cambio de proveedor, un incidente.

*Son reglas ratificadas, no números — por eso viven acá y no en la config.*

## 6. Jerarquía de independencia

Cómo pesa la evidencia en la síntesis: qué unidades cuentan como réplicas
ciegas, qué cuenta como una sola unidad epistémica (todo conjunto `chained`), y
qué precedencia se aplica ante conflicto — directriz humana > juicio del
coordinador > juicio de la sesión (spec §7.3).

## 7. Kill criteria globales

Condiciones **medibles** que detienen el subprograma entero y disparan gate
humano de inmediato. Se pre-registran acá: un kill criterion inventado al cerrar
no es un kill criterion.

## 8. Bloque ratificado — los números viven en la config

`horizons`, `runs`, `ids`, `metrics` y `context` portan autoridad epistémica y
viven en **`framework.config.yaml`**, en una sola casa. **Esta constitution no
los repite: los apunta** (spec §12 G4) — dos casas para el mismo número es
exactamente el drift que el framework existe para evitar.

Ratificar esta constitution es ratificar también **esos valores tal como están
en la config al momento del gate**. Desde entonces, cambiar cualquiera de esas
claves es una **enmienda**: exige subir `version:` de este documento en el
**mismo commit**, con su fila de changelog. La guarda de integridad lo hace
cumplir.

## Changelog de enmiendas

| Versión | Fecha | Qué cambió | Gate |
|---|---|---|---|
| 1 | \<YYYY-MM-DD\> | versión inicial | pendiente de ratificación |

<!--
Cómo se usa esta plantilla:

  · El cuerpo se redacta en el idioma que declare `language` en la config; los
    campos del frontmatter, los IDs y los valores de enum, siempre en inglés
    (spec §1.8).
  · Los horizontes de caducidad NO se escriben acá (§12 G4): están en
    `framework.config.yaml`, y §8 los apunta.
  · Una sección sin contenido no se deja con relleno: se le pregunta al humano
    qué va ahí. Un número inventado por la skill es lógica de negocio
    contrabandeada (principio de diseño #2).
  · Al ratificarse: `status: ratified — <fecha>`, fila en el changelog y
    `registry add gates --gate constitution-ratification`.
-->
