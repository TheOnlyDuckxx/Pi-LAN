"""Utilite: centraliser la config; fonctionnement: lit env et valide via Pydantic Settings."""

from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    host_files_smb: str | None = Field(default=None, alias="LANHUB_HOST_FILES_SMB")
    host_files_http: str | None = Field(default=None, alias="LANHUB_HOST_FILES_HTTP")
    scan_subnet: str = Field(default="192.168.1.0/24", alias="LANHUB_SCAN_SUBNET")
    port_presets: str = Field(default="80,443", alias="LANHUB_PORT_PRESETS")
    db_path: str = Field(default="/var/lib/lanhub/lanhub.db", alias="LANHUB_DB_PATH")

    class Config:
        env_file = ".env"
        extra = "ignore"


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    settings = Settings()
    if not settings.host_files_smb and not settings.host_files_http:
        # Pas de source de jeux configurable, le dashboard affichera un warning.
        pass
    return settings
