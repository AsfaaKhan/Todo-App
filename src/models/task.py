from dataclasses import dataclass
from typing import Optional


@dataclass
class Task:
    """
    Represents a todo item with basic properties.

    Attributes:
        id (int): Auto-incrementing unique identifier for the task
        title (str): Title of the task (required, non-empty)
        description (str): Detailed description of the task (optional)
        completed (bool): Boolean indicating if the task is completed (default: False)
    """
    id: int
    title: str
    description: Optional[str] = ""
    completed: bool = False

    def __post_init__(self):
        """Validate the task after initialization."""
        if not self.title or not self.title.strip():
            raise ValueError("Task title cannot be empty or None")

    def validate_title(self, title: str) -> bool:
        """
        Validate that the title is not empty or None.

        Args:
            title: The title to validate

        Returns:
            bool: True if valid, raises ValueError if invalid
        """
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty or None")
        return True