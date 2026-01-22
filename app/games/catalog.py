"""Utilite: modeles catalogue; fonctionnement: structures de donnees pour jeux/releases."""

from dataclasses import dataclass


@dataclass
class FileRef:
    name: str
    url: str


@dataclass
class Release:
    version: str
    files: list[FileRef]


@dataclass
class Game:
    name: str
    releases: list[Release]
