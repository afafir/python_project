from pydantic import BaseSettings


class Settings(BaseSettings):
    TELEGRAM_ID: int
    TELEGRAM_HASH: str
    MESSAGES_API_URL: str
    BACK_API_TOKEN: str

    class Config(BaseSettings.Config):
        env_file = '.env'


settings = Settings()
