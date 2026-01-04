from pydantic_settings import BaseSettings
from typing import Optional
import os


class Settings(BaseSettings):
    # Database configuration
    database_url: str = ""
    database_host: str = "localhost"
    database_port: int = 5432
    database_name: str = "todo_app"
    database_user: str = "todo_user"
    database_password: str = "todo_password"

    # Application configuration
    log_level: str = "info"
    max_connections: int = 20
    min_connections: int = 5

    # API configuration
    api_v1_str: str = "/api/v1"
    project_name: str = "Todo Backend Service"
    version: str = "1.0.0"

    # Test configuration
    test_database_url: str = "sqlite+aiosqlite:///:memory:"

    class Config:
        env_file = ".env"


# Create a single instance of settings
settings = Settings()


def get_database_url():
    """
    Return the appropriate database URL based on whether we're in test mode.
    """
    # Check for test environment first
    if os.getenv("TESTING"):
        return settings.test_database_url

    # Use environment variable for database URL if available
    db_url = os.getenv("DATABASE_URL")
    if db_url:
        return db_url

    # Use the database_url from settings if environment variable is not set
    if settings.database_url:
        return settings.database_url

    # Construct database URL from individual components as fallback
    return f"postgresql+asyncpg://{settings.database_user}:{settings.database_password}@{settings.database_host}:{settings.database_port}/{settings.database_name}"