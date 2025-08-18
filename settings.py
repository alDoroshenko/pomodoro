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
    GOOGLE_CLIENT_ID: str = '524171505871-hu4t67u488thfgq8ruaj07s4ashimorp.apps.googleusercontent.com'
    GOOGLE_REDIRECT_URI: str = 'http://localhost:8000/api/auth/google'
    GOOGLE_CLIENT_SECRET: str = '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'
    GOOGLE_TOKEN_URL: str = 'https://accounts.google.com/o/oauth2/token'

    @property
    def db_url(self):
        return f'{self.DB_DRIVER}://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'

    @property
    def google_redirect_url(self) -> str:
        return f"https://accounts.google.com/o/oauth2/auth?response_type=code&client_id={self.GOOGLE_CLIENT_ID}&redirect_uri={self.GOOGLE_REDIRECT_URI}&scope=openid%20profile%20email&access_type=offline"
