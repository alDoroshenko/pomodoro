from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_HOST: str = 'localhost'
    DB_PORT: int = 5435
    DB_USER: str = 'postgres'
    DB_PASSWORD: str = 'postgres'
    DB_DRIVER: str = 'postgresql+psycopg2'
    DB_NAME: str = 'pomodoro'
    CACHE_HOST: str = 'localhost'
    CACHE_PORT: int = 6380
    CACHE_DB: int = 0
    JWT_SECRET_KEY: str = 'secret_key'
    JWT_ENCODE_ALG: str = 'HS256'

    @property
    def db_url(self):
        return f'{self.DB_DRIVER}://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
