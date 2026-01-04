from typing import List, Optional
from .task import Task

class TaskList:
    """
    Collection of Task entities managed in memory.

    Attributes:
        tasks (list): List of Task objects
        next_id (int): Counter for generating next available ID (auto-increment)
    """

    def __init__(self):
        """Initialize an empty task list with ID counter starting at 1."""
        self.tasks: List[Task] = []
        self.next_id: int = 1

    def add_task(self, title: str, description: str = "") -> Task:
        """
        Add a new task to the list with auto-incrementing ID.

        Args:
            title: The title of the task
            description: The description of the task (optional)

        Returns:
            Task: The newly created task with assigned ID
        """
        task = Task(id=self.next_id, title=title, description=description, completed=False)
        self.tasks.append(task)
        self.next_id += 1
        return task

    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks in the list.

        Returns:
            List[Task]: All tasks in the list
        """
        return self.tasks.copy()

    def find_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Find a task by its ID.

        Args:
            task_id: The ID of the task to find

        Returns:
            Task: The task if found, None otherwise
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

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
        task = self.find_task_by_id(task_id)
        if not task:
            return False

        if title is not None:
            if title == "":
                raise ValueError("Task title cannot be empty")
            task.validate_title(title)
            task.title = title

        if description is not None:
            task.description = description

        return True

    def mark_task_complete(self, task_id: int, completed: bool = True) -> bool:
        """
        Mark a task as complete or incomplete.

        Args:
            task_id: The ID of the task to update
            completed: Whether the task is completed (default: True)

        Returns:
            bool: True if task was found and updated, False otherwise
        """
        task = self.find_task_by_id(task_id)
        if not task:
            return False

        task.completed = completed
        return True

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.

        Args:
            task_id: The ID of the task to delete

        Returns:
            bool: True if task was found and deleted, False otherwise
        """
        task = self.find_task_by_id(task_id)
        if not task:
            return False

        self.tasks.remove(task)
        return True