"""Configuração baseada em variáveis de ambiente (prefixo ODIN_) e arquivo .env.

Chaves de API de provedores NÃO são lidas aqui ainda; entram junto com o
Model Manager (Task 002), sempre vindas do ambiente e nunca do repositório.
"""

from functools import lru_cache
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="ODIN_", env_file=".env", extra="ignore"
    )

    app_name: str = "ODIN FORCE"
    environment: Literal["development", "production", "test"] = "development"
    debug: bool = False
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR"] = "INFO"


@lru_cache
def get_settings() -> Settings:
    return Settings()
