"""Utilite: checksums; fonctionnement: calcule SHA256 pour fichiers locaux."""

import hashlib
from pathlib import Path


def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()
