"""La costura por-repo: dónde vive el kit dentro de un repo consumidor.

Una sola costura, en un solo lugar. `kit-init` la escribe; `doctor` la
verifica.

Dos reglas duras del plan viven acá:

1. **El shim va a la RUTA EFECTIVA de hooks**, no a `.git/hooks` a ciegas:
   se resuelve con `git rev-parse --git-path hooks`, que honra
   `core.hooksPath` (meridian, por ejemplo, lo tiene en `scripts/hooks`).
2. **Nada apunta al caché del plugin.** `${CLAUDE_PLUGIN_ROOT}` cambia en cada
   update y el hook tiene que correr sin Claude Code instalado: por eso el
   hook y su librería se **vendorizan** dentro del repo, versionados, y el
   shim solo los invoca.
"""
from __future__ import annotations

import subprocess
from pathlib import Path

from .config import KIT_DIR
from .errors import fail

HOOK_NAME = "pre-commit"
LOCAL_HOOK_NAME = "pre-commit.local"

SHIM = f"""#!/bin/sh
# inception-kit — shim del hook {HOOK_NAME}. Lo genera `kit-init`; no editar.
#
# La lógica vive versionada en el repo ({KIT_DIR}/hooks/{HOOK_NAME}) y NO en el
# caché del plugin: el hook debe correr sin Claude Code instalado y sobrevivir a
# cada update del kit. Si este repo ya tenía un {HOOK_NAME} propio, `kit-init` lo
# conservó como `{LOCAL_HOOK_NAME}` acá al lado y se ejecuta primero.
set -e
here=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
root=$(git rev-parse --show-toplevel)
if [ -x "$here/{LOCAL_HOOK_NAME}" ]; then
  "$here/{LOCAL_HOOK_NAME}" "$@"
fi
exec "$root/{KIT_DIR}/hooks/{HOOK_NAME}" "$@"
"""


class Installation:
    """Rutas de la instalación del kit dentro de un repo."""

    def __init__(self, root: Path):
        self.root = Path(root)

    @property
    def kit_dir(self) -> Path:
        return self.root / KIT_DIR

    @property
    def vendored_lib(self) -> Path:
        return self.kit_dir / "lib"

    @property
    def vendored_hook(self) -> Path:
        return self.kit_dir / "hooks" / HOOK_NAME

    @property
    def version_file(self) -> Path:
        return self.kit_dir / "VERSION"

    def git(self, *args: str) -> str:
        result = subprocess.run(["git", "-C", str(self.root), *args],
                                capture_output=True, text=True)
        if result.returncode != 0:
            fail(f"git {' '.join(args)}: {result.stderr.strip() or result.stdout.strip()}")
        return result.stdout.strip()

    def hooks_dir(self) -> Path:
        """Ruta EFECTIVA de hooks — honra `core.hooksPath`, jamás asume `.git/hooks`."""
        raw = Path(self.git("rev-parse", "--git-path", "hooks"))
        return raw if raw.is_absolute() else (self.root / raw)

    def hooks_dir_relative(self) -> str:
        directory = self.hooks_dir()
        try:
            return str(directory.resolve().relative_to(self.root.resolve()))
        except ValueError:
            return str(directory)

    def shim_path(self) -> Path:
        return self.hooks_dir() / HOOK_NAME

    def local_hook_path(self) -> Path:
        return self.hooks_dir() / LOCAL_HOOK_NAME

    def shim_is_installed(self) -> bool:
        shim = self.shim_path()
        return shim.is_file() and shim.read_text(encoding="utf-8") == SHIM

    def installed_version(self) -> str | None:
        if not self.version_file.is_file():
            return None
        return self.version_file.read_text(encoding="utf-8").strip() or None
