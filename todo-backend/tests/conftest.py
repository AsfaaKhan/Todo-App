import pytest
import pytest_asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from app.database import Base, engine
from app.main import app
from httpx import AsyncClient
import asyncio
import os


# Set the TESTING environment variable
os.environ["TESTING"] = "1"


@pytest.fixture(scope="session")
def event_loop():
    """
    Create an event loop for pytest-asyncio.
    """
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    try:
        yield loop
    finally:
        loop.close()


@pytest_asyncio.fixture(scope="session", autouse=True)
async def create_test_database():
    """
    Create the test database and tables.
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest_asyncio.fixture
async def async_client():
    """
    Create an async client for testing the API.
    """
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        yield client