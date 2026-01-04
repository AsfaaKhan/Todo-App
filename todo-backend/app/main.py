from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from .config import settings
from .database import engine, get_db_engine, get_engine
from .api.v1 import tasks
from .utils.exceptions import TaskNotFound
from .models.task import Base
import logging


# Set up logging
logging.basicConfig(level=settings.log_level.upper())
logger = logging.getLogger(__name__)


def setup_logging():
    """
    Configure logging for the application.
    """
    logging.basicConfig(
        level=settings.log_level.upper(),
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan event handler for startup and shutdown events.
    """
    # Startup
    setup_logging()
    logger.info("Starting up the application...")

    # Ensure we have the right database engine for the environment
    current_engine = await get_engine()

    # Create database tables
    async with current_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    logger.info("Database tables created successfully")

    yield  # This is where the application runs

    # Shutdown
    logger.info("Shutting down the application...")
    if current_engine:
        await current_engine.dispose()


# Create FastAPI app instance
app = FastAPI(
    title=settings.project_name,
    version=settings.version,
    openapi_url=f"{settings.api_v1_str}/openapi.json",
    lifespan=lifespan
)


# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Include API routes
app.include_router(tasks.router, prefix=settings.api_v1_str, tags=["tasks"])


@app.get("/")
def read_root():
    """
    Root endpoint to check if the service is running.
    """
    return {"message": "Todo Backend Service is running", "version": settings.version}


@app.get("/health")
def health_check():
    """
    Health check endpoint to verify service status.
    """
    return {"status": "healthy", "version": settings.version}


@app.exception_handler(TaskNotFound)
async def task_not_found_handler(request: Request, exc: TaskNotFound):
    """
    Exception handler for TaskNotFound.
    """
    return JSONResponse(
        status_code=404,
        content={
            "code": "TASK_NOT_FOUND",
            "message": str(exc),
            "details": f"No task found with ID {exc.task_id}"
        }
    )


@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    """
    General exception handler for unexpected errors.
    """
    return JSONResponse(
        status_code=500,
        content={
            "code": "INTERNAL_ERROR",
            "message": "An internal server error occurred",
            "details": str(exc) if settings.log_level == "debug" else None
        }
    )