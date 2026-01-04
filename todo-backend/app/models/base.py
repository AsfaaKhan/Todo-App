from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeMeta
from sqlalchemy import Column, DateTime, func
import datetime


@as_declarative()
class Base:
    """
    Base class for all SQLAlchemy models.
    Provides common functionality for all models.
    """
    id: Column

    __name__: str

    # Auto-generated created_at and updated_at columns
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())