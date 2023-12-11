from pydantic import BaseSettings


class Settings(BaseSettings):
    VK_TOKEN: str
    BACK_API_URL: str
    BACK_API_TOKEN: str

    class Config:
        env_file = '.env'


settings = Settings()
