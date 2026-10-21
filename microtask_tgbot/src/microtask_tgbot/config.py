from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    bot_token: str

    db_host: str
    db_port: int
    db_user: str
    db_pass: str
    db_name: str

    @property
    def database_url(self) -> str:
        return f"{self.db_url}"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )

settings = Settings()
