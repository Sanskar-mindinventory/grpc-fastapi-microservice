import os

from pydantic_settings import BaseSettings
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

class Settings(BaseSettings):
    DEBUG: bool = True
    TESTING: bool = False

class JWTSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', extra='allow', env_file_encoding='utf-8')
    ACCESS_TOKEN_EXPIRE_TIME_MINUTES: int
    REFRESH_TOKEN_EXPIRE_TIME_HOURS: int
    JWT_ALGORITHM: str
    AUTH_JWT_HEADER_TYPE: str
    AUTH_SECRET_KEY: str
    AUTH_JWT_DECODE_ALGORITHMS: list
    authjwt_secret_key: str


class DatabaseSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', extra='allow', env_file_encoding='utf-8')
    DATABASE_USERNAME: str
    DATABASE_PASSWORD: str
    DATABASE_HOST: str
    DATABASE_NAME: str
    DATABASE_PORT: int


class DatabaseURLSettings(DatabaseSettings):
    SQLALCHEMY_DATABASE_URL: str = f"postgresql+psycopg2://{DatabaseSettings().DATABASE_USERNAME}:{DatabaseSettings().DATABASE_PASSWORD}@{DatabaseSettings().DATABASE_HOST}:{DatabaseSettings().DATABASE_PORT}/{DatabaseSettings().DATABASE_NAME}"