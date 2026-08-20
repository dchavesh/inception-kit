# Archivo de marks — gramática

*Es el juicio de `/inception-kit:close` paso 5 hecho datos: una línea por
requisito de la sección 7 del report. `extract-registry` lo aplica sin
interpretar nada más.*

```
<unit>-reqNN new
<unit>-reqNN duplicate:<otro-id>
<unit>-reqNN contradicts:<otro-id> supersedes:<otro-id>
```

- Las líneas vacías y las que empiezan con `#` se ignoran.
- Un requisito sin línea entra como `new`.
- **`contradicts` sin `supersedes:` ⇒ rechazo total**: no se escribe nada en el
  registry. Una contradicción se declara con su ganador o se registra distinto;
  el registry no guarda ambigüedades silenciosas.
- Cada `contradicts` además marca la fila superada (`SUPERSEDED by …`, jamás la
  borra) y anota un `con-NN` en el registry de conflictos — que solo se anota:
  se resuelve en la síntesis.
- Marcar un ID que no está en el report también es rechazo total.

## Ejemplo

*IDs de ejemplo neutros: `rXX` es la unidad que cierra, `rYY` una anterior.*

```
# rXX — cierre AAAA-MM-DD
rXX-req01 new
rXX-req02 duplicate:rYY-req05
rXX-req03 contradicts:rYY-req02 supersedes:rYY-req02
```
