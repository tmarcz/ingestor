from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_PORT: int


settings: Settings = None
