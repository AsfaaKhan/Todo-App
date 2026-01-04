import pytest
from httpx import AsyncClient
from app.schemas.task import TaskCreate


@pytest.mark.asyncio
async def test_create_task(async_client: AsyncClient):
    """
    Test creating a new task.
    """
    task_data = {
        "title": "Test Task",
        "description": "This is a test task"
    }

    response = await async_client.post("/api/v1/tasks", json=task_data)

    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Task"
    assert data["description"] == "This is a test task"
    assert data["completed"] is False
    assert "id" in data
    assert "created_at" in data


@pytest.mark.asyncio
async def test_create_task_without_description(async_client: AsyncClient):
    """
    Test creating a task without a description (description is optional).
    """
    task_data = {
        "title": "Task without description"
    }

    response = await async_client.post("/api/v1/tasks", json=task_data)

    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Task without description"
    assert data["description"] is None
    assert data["completed"] is False
    assert "id" in data


@pytest.mark.asyncio
async def test_create_task_with_empty_title_should_fail(async_client: AsyncClient):
    """
    Test creating a task with an empty title (should fail validation).
    """
    task_data = {
        "title": "",
        "description": "This task has an empty title"
    }

    response = await async_client.post("/api/v1/tasks", json=task_data)

    assert response.status_code == 422  # Validation error


@pytest.mark.asyncio
async def test_get_all_tasks_initially_empty(async_client: AsyncClient):
    """
    Test getting all tasks when there are no tasks.
    """
    response = await async_client.get("/api/v1/tasks")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 0


@pytest.mark.asyncio
async def test_get_specific_task(async_client: AsyncClient):
    """
    Test creating a task and then retrieving it by ID.
    """
    # Create a task first
    task_data = {
        "title": "Task to retrieve",
        "description": "This task will be retrieved"
    }
    create_response = await async_client.post("/api/v1/tasks", json=task_data)
    assert create_response.status_code == 201
    created_task = create_response.json()

    # Retrieve the task by ID
    task_id = created_task["id"]
    get_response = await async_client.get(f"/api/v1/tasks/{task_id}")

    assert get_response.status_code == 200
    retrieved_task = get_response.json()
    assert retrieved_task["id"] == task_id
    assert retrieved_task["title"] == "Task to retrieve"
    assert retrieved_task["description"] == "This task will be retrieved"


@pytest.mark.asyncio
async def test_get_nonexistent_task(async_client: AsyncClient):
    """
    Test retrieving a task that doesn't exist.
    """
    response = await async_client.get("/api/v1/tasks/99999")

    assert response.status_code == 404


@pytest.mark.asyncio
async def test_update_task(async_client: AsyncClient):
    """
    Test updating an existing task.
    """
    # Create a task first
    task_data = {
        "title": "Original Task",
        "description": "Original description"
    }
    create_response = await async_client.post("/api/v1/tasks", json=task_data)
    assert create_response.status_code == 201
    created_task = create_response.json()

    # Update the task
    task_id = created_task["id"]
    update_data = {
        "title": "Updated Task",
        "description": "Updated description",
        "completed": True
    }
    update_response = await async_client.put(f"/api/v1/tasks/{task_id}", json=update_data)

    assert update_response.status_code == 200
    updated_task = update_response.json()
    assert updated_task["id"] == task_id
    assert updated_task["title"] == "Updated Task"
    assert updated_task["description"] == "Updated description"
    assert updated_task["completed"] is True


@pytest.mark.asyncio
async def test_delete_task(async_client: AsyncClient):
    """
    Test deleting an existing task.
    """
    # Create a task first
    task_data = {
        "title": "Task to delete",
        "description": "This task will be deleted"
    }
    create_response = await async_client.post("/api/v1/tasks", json=task_data)
    assert create_response.status_code == 201
    created_task = create_response.json()

    # Delete the task
    task_id = created_task["id"]
    delete_response = await async_client.delete(f"/api/v1/tasks/{task_id}")

    assert delete_response.status_code == 204

    # Verify the task is gone
    get_response = await async_client.get(f"/api/v1/tasks/{task_id}")
    assert get_response.status_code == 404


@pytest.mark.asyncio
async def test_update_task_status(async_client: AsyncClient):
    """
    Test updating a task's completion status.
    """
    # Create a task first
    task_data = {
        "title": "Task to update status",
        "description": "This task status will be updated"
    }
    create_response = await async_client.post("/api/v1/tasks", json=task_data)
    assert create_response.status_code == 201
    created_task = create_response.json()

    # Update the task status
    task_id = created_task["id"]
    status_data = {
        "completed": True
    }
    patch_response = await async_client.patch(f"/api/v1/tasks/{task_id}/status", json=status_data)

    assert patch_response.status_code == 200
    patched_task = patch_response.json()
    assert patched_task["id"] == task_id
    assert patched_task["completed"] is True