from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from ..models.task import Task
from ..schemas.task import TaskCreate, TaskUpdate, TaskResponse, TaskStatusUpdate
from ..utils.exceptions import TaskNotFound


class TaskService:
    """
    Service class for handling business logic related to Task operations.
    Provides methods for CRUD operations on tasks.
    """

    @staticmethod
    async def create_task(db: AsyncSession, task_data: TaskCreate) -> TaskResponse:
        """
        Create a new task in the database.

        Args:
            db: Database session
            task_data: Task creation data

        Returns:
            TaskResponse: Created task data
        """
        # Validation is handled by Pydantic schema, but we can add additional business logic here if needed
        if len(task_data.title.strip()) == 0:
            raise ValueError("Task title cannot be empty or whitespace only")

        # Create a new Task instance
        db_task = Task(
            title=task_data.title,
            description=task_data.description,
            completed=False  # New tasks are not completed by default
        )

        # Add the task to the session and commit
        db.add(db_task)
        await db.commit()
        await db.refresh(db_task)

        # Convert to response schema and return
        return TaskResponse.model_validate(db_task)

    @staticmethod
    async def get_all_tasks(db: AsyncSession, skip: int = 0, limit: int = 100) -> List[TaskResponse]:
        """
        Retrieve all tasks from the database.

        Args:
            db: Database session
            skip: Number of records to skip (for pagination)
            limit: Maximum number of records to return

        Returns:
            List[TaskResponse]: List of all tasks
        """
        # Query all tasks with optional pagination
        result = await db.execute(
            select(Task)
            .offset(skip)
            .limit(limit)
        )
        tasks = result.scalars().all()

        # Convert to response schemas
        return [TaskResponse.model_validate(task) for task in tasks]

    @staticmethod
    async def get_task_by_id(db: AsyncSession, task_id: int) -> Optional[TaskResponse]:
        """
        Retrieve a specific task by its ID.

        Args:
            db: Database session
            task_id: ID of the task to retrieve

        Returns:
            TaskResponse: The requested task, or None if not found
        """
        # Query task by ID
        result = await db.execute(
            select(Task).where(Task.id == task_id)
        )
        task = result.scalar_one_or_none()

        if task is None:
            return None

        # Convert to response schema and return
        return TaskResponse.model_validate(task)

    @staticmethod
    async def update_task(db: AsyncSession, task_id: int, task_data: TaskUpdate) -> Optional[TaskResponse]:
        """
        Update an existing task.

        Args:
            db: Database session
            task_id: ID of the task to update
            task_data: Task update data

        Returns:
            TaskResponse: Updated task data, or None if task not found
        """
        # Check if task exists
        result = await db.execute(
            select(Task).where(Task.id == task_id)
        )
        task = result.scalar_one_or_none()

        if task is None:
            return None

        # Additional validation for updates
        if task_data.title is not None and len(task_data.title.strip()) == 0:
            raise ValueError("Task title cannot be empty or whitespace only")

        # Prepare update data
        update_data = {}
        if task_data.title is not None:
            update_data["title"] = task_data.title
        if task_data.description is not None:
            update_data["description"] = task_data.description
        if task_data.completed is not None:
            update_data["completed"] = task_data.completed

        # Update the task
        await db.execute(
            update(Task)
            .where(Task.id == task_id)
            .values(**update_data)
        )
        await db.commit()

        # Refresh and return the updated task
        await db.refresh(task)
        return TaskResponse.model_validate(task)

    @staticmethod
    async def delete_task(db: AsyncSession, task_id: int) -> bool:
        """
        Delete a task by its ID.

        Args:
            db: Database session
            task_id: ID of the task to delete

        Returns:
            bool: True if task was deleted, False if not found
        """
        # Delete the task
        result = await db.execute(
            delete(Task)
            .where(Task.id == task_id)
        )

        # Commit the transaction
        await db.commit()

        # Return True if a row was deleted, False otherwise
        return result.rowcount > 0

    @staticmethod
    async def update_task_status(db: AsyncSession, task_id: int, status_data: TaskStatusUpdate) -> Optional[TaskResponse]:
        """
        Update the completion status of a task.

        Args:
            db: Database session
            task_id: ID of the task to update
            status_data: Task status update data

        Returns:
            TaskResponse: Updated task data, or None if task not found
        """
        # Check if task exists
        result = await db.execute(
            select(Task).where(Task.id == task_id)
        )
        task = result.scalar_one_or_none()

        if task is None:
            return None

        # Update the completion status
        await db.execute(
            update(Task)
            .where(Task.id == task_id)
            .values(completed=status_data.completed)
        )
        await db.commit()

        # Refresh and return the updated task
        await db.refresh(task)
        return TaskResponse.model_validate(task)