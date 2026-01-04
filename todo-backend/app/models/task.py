from sqlalchemy import Column, Integer, String, Boolean, Text
from sqlalchemy.sql import func
from sqlalchemy import DateTime
from .base import Base


class Task(Base):
    """
    SQLAlchemy model for the tasks table.
    Represents a todo item with title, description, and completion status.
    """
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    completed = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return f"<Task(id={self.id}, title='{self.title}', completed={self.completed})>"