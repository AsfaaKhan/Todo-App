from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from ...schemas.task import TaskCreate, TaskUpdate, TaskResponse, TaskStatusUpdate
from ...services.task_service import TaskService
from ..deps import get_db_session


# Create the API router
router = APIRouter()


@router.post(
    "/tasks",
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new task",
    description="Creates a new task with the provided details."
)
async def create_task(
    task: TaskCreate,
    db: AsyncSession = Depends(get_db_session)
) -> TaskResponse:
    """
    Create a new task.

    Args:
        task: Task creation data
        db: Database session

    Returns:
        TaskResponse: Created task data
    """
    try:
        return await TaskService.create_task(db, task)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating task: {str(e)}"
        )


@router.get(
    "/tasks",
    response_model=List[TaskResponse],
    summary="Get all tasks",
    description="Retrieves all tasks with optional pagination."
)
async def get_tasks(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db_session)
) -> List[TaskResponse]:
    """
    Retrieve all tasks.

    Args:
        skip: Number of records to skip (for pagination)
        limit: Maximum number of records to return
        db: Database session

    Returns:
        List[TaskResponse]: List of all tasks
    """
    try:
        return await TaskService.get_all_tasks(db, skip=skip, limit=limit)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving tasks: {str(e)}"
        )


@router.get(
    "/tasks/{task_id}",
    response_model=TaskResponse,
    summary="Get a specific task",
    description="Retrieves a specific task by its ID."
)
async def get_task(
    task_id: int,
    db: AsyncSession = Depends(get_db_session)
) -> TaskResponse:
    """
    Retrieve a specific task by its ID.

    Args:
        task_id: ID of the task to retrieve
        db: Database session

    Returns:
        TaskResponse: The requested task

    Raises:
        HTTPException: If the task is not found
    """
    task = await TaskService.get_task_by_id(db, task_id)
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with ID {task_id} not found"
        )
    return task


@router.put(
    "/tasks/{task_id}",
    response_model=TaskResponse,
    summary="Update a task",
    description="Updates an existing task with the provided details."
)
async def update_task(
    task_id: int,
    task: TaskUpdate,
    db: AsyncSession = Depends(get_db_session)
) -> TaskResponse:
    """
    Update an existing task.

    Args:
        task_id: ID of the task to update
        task: Task update data
        db: Database session

    Returns:
        TaskResponse: Updated task data

    Raises:
        HTTPException: If the task is not found
    """
    updated_task = await TaskService.update_task(db, task_id, task)
    if updated_task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with ID {task_id} not found"
        )
    return updated_task


@router.delete(
    "/tasks/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a task",
    description="Deletes a specific task by its ID."
)
async def delete_task(
    task_id: int,
    db: AsyncSession = Depends(get_db_session)
) -> None:
    """
    Delete a task by its ID.

    Args:
        task_id: ID of the task to delete
        db: Database session

    Raises:
        HTTPException: If the task is not found
    """
    success = await TaskService.delete_task(db, task_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with ID {task_id} not found"
        )


@router.patch(
    "/tasks/{task_id}/status",
    response_model=TaskResponse,
    summary="Update task completion status",
    description="Updates the completion status of a specific task."
)
async def update_task_status(
    task_id: int,
    status_update: TaskStatusUpdate,
    db: AsyncSession = Depends(get_db_session)
) -> TaskResponse:
    """
    Update the completion status of a task.

    Args:
        task_id: ID of the task to update
        status_update: Task status update data
        db: Database session

    Returns:
        TaskResponse: Updated task data

    Raises:
        HTTPException: If the task is not found
    """
    updated_task = await TaskService.update_task_status(db, task_id, status_update)
    if updated_task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with ID {task_id} not found"
        )
    return updated_task