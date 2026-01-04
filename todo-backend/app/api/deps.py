from typing import AsyncGenerator
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from ..database import get_db


# Database dependency for API endpoints
async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Dependency to get database session for API endpoints.
    Ensures proper session cleanup after each request.
    """
    async for session in get_db():
        try:
            yield session
        finally:
            await session.close()