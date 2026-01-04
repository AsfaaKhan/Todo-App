from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from .base import BaseSchema


class TaskBase(BaseSchema):
    """
    Base schema for Task with common fields.
    """
    title: str = Field(..., min_length=1, max_length=200, description="Task title")
    description: Optional[str] = Field(None, max_length=1000, description="Task description")


class TaskCreate(TaskBase):
    """
    Schema for creating a new task.
    Inherits from TaskBase and adds any creation-specific validation.
    """
    title: str = Field(..., min_length=1, max_length=200, description="Task title (required)")


class TaskUpdate(TaskBase):
    """
    Schema for updating an existing task.
    All fields are optional to allow partial updates.
    """
    title: Optional[str] = Field(None, min_length=1, max_length=200, description="Task title")
    description: Optional[str] = Field(None, max_length=1000, description="Task description")
    completed: Optional[bool] = Field(None, description="Task completion status")


class TaskResponse(TaskBase):
    """
    Schema for returning task data to clients.
    Includes all fields from TaskBase plus id and timestamps.
    """
    id: int
    completed: bool = False
    created_at: datetime
    updated_at: Optional[datetime] = None


class TaskStatusUpdate(BaseSchema):
    """
    Schema for updating only the completion status of a task.
    """
    completed: bool = Field(..., description="New completion status for the task")