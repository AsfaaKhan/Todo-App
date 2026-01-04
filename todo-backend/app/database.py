from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.pool import NullPool
from typing import AsyncGenerator
from .config import get_database_url, settings
import os


def create_engine():
    """
    Create the async database engine with appropriate settings based on the database type.
    """
    db_url = get_database_url()
    is_sqlite = db_url.startswith("sqlite")

    # Configure engine options based on database type
    engine_kwargs = {
        "echo": False,  # Set to True for SQL query logging
    }

    if is_sqlite:
        # SQLite-specific options
        engine_kwargs.update({
            "poolclass": NullPool,  # Use NullPool for SQLite
        })
    else:
        # PostgreSQL-specific options
        engine_kwargs.update({
            "pool_size": settings.max_connections,
            "max_overflow": settings.min_connections,
            "pool_pre_ping": True,  # Verify connections before use
            "pool_recycle": 300,  # Recycle connections after 5 minutes
        })

    return create_async_engine(
        db_url,
        **engine_kwargs
    )


# Global variable to hold the engine instance
_engine_instance = None


async def get_engine():
    """
    Get the database engine, creating it if it doesn't exist or if the URL has changed.
    This ensures the engine is created with the current environment settings.
    """
    global _engine_instance
    current_db_url = get_database_url()

    # If we don't have an engine instance or the URL has changed, create a new one
    if _engine_instance is None or str(_engine_instance.url) != current_db_url:
        if _engine_instance is not None:
            await _engine_instance.dispose()  # Dispose of the old engine if it exists
        _engine_instance = create_engine()

    return _engine_instance


# Don't create the engine at import time - it will be created when needed
engine = None


def get_db_engine():
    """
    Get the database engine, potentially recreating it if the environment has changed.
    This allows for switching between test and production databases.
    """
    # This function should return a sync engine for non-async contexts
    # For async contexts, use get_engine() directly
    global _engine_instance
    current_db_url = get_database_url()

    # If we don't have an engine instance or the URL has changed, create a new one
    if _engine_instance is None or str(_engine_instance.url) != current_db_url:
        # For sync access, we'll return the current instance or create one
        if _engine_instance is None:
            _engine_instance = create_engine()

    return _engine_instance

# Base class for SQLAlchemy models
Base = declarative_base()


# Create async session maker function
def get_db_session_local():
    """
    Get a database session maker using the current engine.
    This ensures the session maker is using the correct engine based on the environment.
    """
    current_engine = get_db_engine()
    return sessionmaker(
        current_engine,
        class_=AsyncSession,
        expire_on_commit=False
    )


# Dependency to get database session
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    # Get the session maker with the current engine
    session_local = get_db_session_local()
    async with session_local() as session:
        try:
            yield session
        finally:
            await session.close()