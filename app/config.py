from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "kiddox-notification-backend"
    app_version: str = "0.1.0"
    app_env: str = "development"
    cors_origins: list[str] = ["*"]

    supabase_url: str = ""
    supabase_anon_key: str = ""
    supabase_service_role_key: str = ""

    host: str = "0.0.0.0"
    port: int = 8005


settings = Settings()
