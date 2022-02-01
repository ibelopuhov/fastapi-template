from pydantic import BaseSettings

class Settings(BaseSettings):
    database_hostname: str = "localhost"
    database_password: str = "p05tgre5"
    database_username: str = "postgres"
    database_port: int = 5432
    database_name: str = "fastapi"
    app_settings_file = "app_config.json"

    class Config:
        env_file = ".env"

settings: Settings = Settings()


