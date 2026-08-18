# inception-kit

El **inception-framework** completo en una sola casa: spec, scripts, skills, plantillas y hook, empaquetado como **plugin de Claude Code** (este repo es también su marketplace) y consumido por los proyectos blite.

**Estado: pre-0.1** — el repo nace con el contrato ratificado; el contenido llega con la extracción (Fase 1 del plan de mejoras — versión vigente en `meridian/docs/research/` vía su `registry/supersessions.md`; el plan y la spec migran acá — la v0.3 se redacta en este repo). Ya viven acá las skills de claude.ai (`claude-ai-skills/`).

## Contrato ratificado (2026-08-18)

| Decisión | Valor |
|---|---|
| Hogar remoto | `gitlab.com/blite-systems/tools/inception-kit` (subgrupo `tools` = categoría local — mapeo 1:1, misma descripción que el manifest) |
| Hogar local | `~/projects/blite/tools/inception-kit` (categoría `blite/tools`) |
| Nombre | `inception-kit` — repo, plugin y namespace de skills (`/inception-kit:…`); jamás se renombra |
| Spec | Vive ACÁ (una casa por cosa): la v0.3 se redacta en este repo; daedalus pasa a consumidor |
| Distribución | Plugin de Claude Code + marketplace en este mismo repo; instalación/updates por https (credencial oauth de la máquina, verificada; el alias SSH `gitlab-blite` queda para uso interactivo) |
| Versionado | Semver explícito desde `0.1.0` + `CHANGELOG.md`; update = bump del kit, jamás cirugía por repo; `autoUpdate` encendido en consumidores |
| Contenido v0.1 | 10 scripts generalizados (`bin/`) · **6 skills**: `launch`, `close`, `synthesis`, `status`, `ingest`, `plan` (el cierre retro-lenient no es skill: lo absorbe el flujo `/adopt`) · plantillas internas al plugin · hook de inmutabilidad + `kit-init` idempotente (única costura por-repo) · skills de claude.ai: `research-preflight`, `research-close`, `new-run` (en `claude-ai-skills/`; el humano las copia a su cuenta) · `framework.config.yaml` por proyecto |
| Nomenclatura | **Inglés** para todo nombre de skill, comando y campo de contrato (ratificado 2026-08-18); un solo idioma, cero híbridos |
| Corridas | `runs: N` + `mode: independent \| chained` en el protocol (default `independent`); `chained` = partes deliberadas, una unidad epistémica; el contexto se declara, jamás se improvisa |
| Migración de prueba | daedalus primero, meridian después |

## Principios (heredados del plan de mejoras — no negociables)

Simplicidad — un mecanismo por problema; los edge cases se adaptan al framework, jamás al revés. Skills sin lógica de negocio. Procesos endurecidos, investigación libre. Un contrato, un lugar, varios lectores. Colocación por unidad. El norte: **coordinación · organización · extracción**.
