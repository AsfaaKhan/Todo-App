from typing import List, Optional
from ..models.task_list import TaskList
from ..models.task import Task


class TaskService:
    """
    Business logic for task operations (add, update, delete, mark complete).
    """

    def __init__(self):
        """Initialize the task service with an in-memory task list."""
        self.task_list = TaskList()

    def add_task(self, title: str, description: str = "") -> Task:
        """
        Add a new task to the system.

        Args:
            title: The title of the task (required)
            description: The description of the task (optional)

        Returns:
            Task: The newly created task with assigned ID
        """
        return self.task_list.add_task(title, description)

    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks in the system.

        Returns:
            List[Task]: All tasks in the system
        """
        return self.task_list.get_all_tasks()

    def update_task(self, task_id: int, title: str = None, description: str = None) -> bool:
        """
        Update an existing task's title and/or description.

        Args:
            task_id: The ID of the task to update
            title: The new title (optional)
            description: The new description (optional)

        Returns:
            bool: True if task was found and updated, False otherwise
        """
        return self.task_list.update_task(task_id, title, description)

    def mark_task_complete(self, task_id: int, completed: bool = True) -> bool:
        """
        Mark a task as complete or incomplete.

        Args:
            task_id: The ID of the task to update
            completed: Whether the task is completed (default: True)

        Returns:
            bool: True if task was found and updated, False otherwise
        """
        return self.task_list.mark_task_complete(task_id, completed)

    def find_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Find a task by its ID.

        Args:
            task_id: The ID of the task to find

        Returns:
            Task: The task if found, None otherwise
        """
        return self.task_list.find_task_by_id(task_id)

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.

        Args:
            task_id: The ID of the task to delete

        Returns:
            bool: True if task was found and deleted, False otherwise
        """
        return self.task_list.delete_task(task_id)