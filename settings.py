from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    GOOGLE_TOKEN_ID: str = "zaglushka"
    sqlite_db_name: str = "SQLite/pomodoro.sqlite"
