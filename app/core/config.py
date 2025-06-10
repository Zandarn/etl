import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    api_version: str = os.getenv("API_VERSION")
    api_title: str = os.getenv("API_TITLE")
    api_description: str = os.getenv("API_DESCRIPTION")
    debug: bool = os.getenv("DEBUG")
    frankfurter_url: str = os.getenv("FRANKFURTER_URL")
    exchangerate_url: str = os.getenv("EXCHANGERATE_URL")
    database_url: str = os.getenv("DATABASE_URL")

    redis_url: str = os.getenv("REDIS_URL")
    redis_port: int = os.getenv("REDIS_PORT")
    redis_db: int = os.getenv("REDIS_DB")

    class Config:
        load_dotenv()


settings = Settings()
