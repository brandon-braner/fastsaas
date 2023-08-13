import os
from os import environ as env
from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

env_file_path = Path(__file__).resolve().parent.parent / ".env"
env_file = str(env_file_path.resolve()) if env_file_path.resolve().exists() else None

if env_file:
    load_dotenv(dotenv_path=env_file)


class Settings(BaseSettings):
    app_name: str = "Single Pane"
    app_secret_key: str = env.get("APP_SECRET_KEY", "super-secret")
    dev_mode: str | bool = env.get("DEV_MODE")

    supabase_url: str = env.get("SUPABASE_URL")
    supabase_key: str = env.get("SUPABASE_KEY")
    supabase_jwt_secret: str = env.get("SUPABASE_JWT_SECRET")


def get_settings() -> Settings:
    return Settings()
