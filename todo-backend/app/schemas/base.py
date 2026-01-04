from pydantic import BaseModel


class BaseSchema(BaseModel):
    """
    Base schema for all Pydantic models.
    Provides common configuration for all schemas.
    """
    class Config:
        from_attributes = True  # This allows SQLAlchemy models to be converted to Pydantic models