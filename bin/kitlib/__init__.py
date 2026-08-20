"""Núcleo compartido de los scripts deterministas del inception-kit.

Sin juicio: config, rutas, parsing, IDs y fechas — nada más. Los scripts son
la autoridad mecánica; el juicio vive en las skills; los gates son humanos.

Se instala en dos lugares y es el mismo código en ambos: `bin/kitlib/` dentro
del plugin (lo usan los comandos) y `.inception-kit/lib/kitlib/` vendorizado
en cada repo consumidor (lo usa el hook, que debe correr sin Claude Code ni
dependencias). `kit-init` mantiene la copia en sintonía.
"""
from __future__ import annotations

from . import config, dates, ids, md, status, vocab
from .config import Config, load
from .errors import fail

__all__ = ["Config", "config", "dates", "fail", "ids", "load", "md", "status", "vocab"]

VERSION = "0.2.0"
