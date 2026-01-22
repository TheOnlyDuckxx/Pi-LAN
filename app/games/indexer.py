"""Utilite: construire le catalogue; fonctionnement: lit manifests et genere liens host."""

from pathlib import Path


def build_catalog() -> list[dict]:
    # Placeholder: lit des manifests JSON/YAML si presents.
    manifests_dir = Path("/srv/lanhub/manifests")
    if not manifests_dir.exists():
        return []
    return []
