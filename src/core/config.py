"""
Centralized application configuration.

Loads settings from environment variables and provides
validated config access across the application.
"""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings.
    """

    app_name: str = "AI Helpdesk Triage System"
    app_version: str = "1.0.0"
    debug: bool = True

    database_url: str = "sqlite:///./helpdesk.db"

    gemini_api_key: str = ""

    log_level: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
    )


@lru_cache
def get_settings() -> Settings:
    """
    Return cached settings instance.

    Returns:
        Settings: application settings
    """
    return Settings()


settings = get_settings()