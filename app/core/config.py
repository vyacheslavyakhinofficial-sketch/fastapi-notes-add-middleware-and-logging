from dotenv import load_dotenv
import os

# 1. Загружаем переменные
load_dotenv(dotenv_path=".env")

class Settings:
    def __init__(self):
        self.db_url = os.getenv("DATABASE_URL")
        self.cors_origins = os.getenv("CORS_ORIGINS")

settings = Settings()









































# # app/core/config.py
# from pathlib import Path
# from pydantic import Field, SecretStr
# from pydantic_settings import BaseSettings, SettingsConfigDict

# # Вычисляем корень проекта для абсолютного пути (важно для Windows + --reload)
# BASE_DIR = Path(__file__).resolve().parent.parent.parent

# class Settings(BaseSettings):
#     """
#     Все настройки приложения. 
#     Pydantic сам прочитает их из .env или переменных окружения.
#     """
    
#     # Настройки базы данных (в нижнем регистре!)
#     database_url: str | None = Field(default=None)
#     db_password: SecretStr | None = Field(default=None)

#     # Настройки CORS (автоматически станет списком из строки)
#     cors_origins: list[str] = Field(default=["http://localhost:3000"])

#     model_config = SettingsConfigDict(
#         env_file=BASE_DIR / ".env", 
#         env_file_encoding="utf-8",
#         case_sensitive=False,
#     )

#     @property
#     def sqlalchemy_url(self) -> str:
#         """Собирает URL для SQLAlchemy"""
#         if self.database_url:
#             return self.database_url
        
#         password = self.db_password.get_secret_value() if self.db_password else "admin"
#         return f"postgresql+psycopg://postgres:{password}@127.0.0.1:5432/postgres"


# # Создаём ОДИН глобальный экземпляр. 
# # Теперь это безопасно импортировать в любом месте.
# settings = Settings()










