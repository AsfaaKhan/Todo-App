# Implementation Plan: Todo Backend Service with PostgreSQL

## Overview
This plan outlines the implementation of a RESTful backend service for a Todo application using PostgreSQL as the primary data store. The service will be built with Python, FastAPI, SQLAlchemy ORM, and Pydantic for data validation.

## Tech Stack
- **Language**: Python 3.12+
- **Web Framework**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Validation**: Pydantic
- **ASGI Server**: UV (uvicorn)

## Architecture Overview
The application follows a modular architecture with clear separation of concerns:
- **API Layer**: FastAPI routes and request/response handling
- **Service Layer**: Business logic and data processing
- **Data Layer**: SQLAlchemy ORM models and database operations
- **Schema Layer**: Pydantic models for data validation

## Project Structure
```
todo-backend/
├── app/                          # Main application package
│   ├── __init__.py              # Package initialization
│   ├── main.py                  # FastAPI application instance and startup configuration
│   ├── config.py                # Configuration settings and environment variables
│   ├── database.py              # Database connection and session management
│   ├── models/                  # SQLAlchemy ORM models
│   │   ├── __init__.py
│   │   ├── base.py              # Base model and metadata
│   │   └── task.py              # Task model definition
│   ├── schemas/                 # Pydantic schemas for validation
│   │   ├── __init__.py
│   │   ├── task.py              # Task-related schemas (TaskCreate, TaskUpdate, TaskResponse)
│   │   └── error.py             # Error response schemas
│   ├── api/                     # API routes
│   │   ├── __init__.py
│   │   ├── deps.py              # Dependency injection functions
│   │   └── v1/                  # API version 1
│   │       ├── __init__.py
│   │       └── tasks.py         # Task-related routes (CRUD operations)
│   ├── services/                # Business logic layer
│   │   ├── __init__.py
│   │   └── task_service.py      # Task operations business logic
│   └── utils/                   # Utility functions
│       ├── __init__.py
│       └── exceptions.py        # Custom exception definitions
├── migrations/                  # Database migration files (Alembic)
│   └── versions/
├── tests/                       # Test files
│   ├── __init__.py
│   ├── conftest.py              # Test configuration
│   ├── test_tasks.py            # Task endpoint tests
│   └── test_config.py           # Configuration tests
├── requirements.txt             # Python dependencies
├── requirements-dev.txt         # Development dependencies
├── alembic.ini                 # Alembic configuration
├── .env.example                # Environment variables example
├── .gitignore                  # Git ignore patterns
└── README.md                   # Project documentation
```

## Database Schema Design

### Tasks Table
The PostgreSQL database will have a single table for tasks:

**Table: tasks**
- `id` (INTEGER, PRIMARY KEY, AUTO_INCREMENT) - Unique identifier for each task
- `title` (VARCHAR(200), NOT NULL) - Task title with maximum length validation
- `description` (TEXT, NULL) - Optional task description
- `completed` (BOOLEAN, DEFAULT FALSE) - Task completion status
- `created_at` (TIMESTAMP WITH TIME ZONE, DEFAULT NOW()) - Record creation timestamp
- `updated_at` (TIMESTAMP WITH TIME ZONE, DEFAULT NOW()) - Record update timestamp

**Indexes:**
- Primary key index on `id`
- Index on `completed` for efficient filtering of completed/incomplete tasks

## ORM Model Definitions

### Base Model
- Inherited from SQLAlchemy's declarative base
- Includes common functionality and metadata
- Uses declarative base for model definition

### Task Model
- Maps to the 'tasks' table
- Column definitions matching the database schema
- Validation constraints at the model level
- Automatic timestamp updates using SQLAlchemy events
- Relationship definitions (if needed for future expansion)

## Pydantic Schemas

### Task Schemas
- **TaskBase**: Common fields shared by all task schemas (title, description)
- **TaskCreate**: Inherits from TaskBase, includes validation for creation
- **TaskUpdate**: Inherits from TaskBase, all fields optional for partial updates
- **TaskResponse**: Inherits from TaskBase, includes id, completed status, and timestamps
- **TaskStatusUpdate**: Schema for updating only the completion status

### Error Schemas
- **ErrorDetail**: Schema for error responses with code, message, and optional details

## API Route Design

### Task Endpoints
- **POST /api/v1/tasks**: Create a new task
  - Request body: TaskCreate schema
  - Response: 201 Created with TaskResponse schema
  - Error responses: 422 for validation errors, 500 for server errors

- **GET /api/v1/tasks**: Retrieve all tasks
  - Query parameters: Optional filtering (completed status, pagination)
  - Response: 200 OK with array of TaskResponse schemas
  - Error responses: 500 for server errors

- **GET /api/v1/tasks/{id}**: Retrieve a specific task
  - Path parameter: task ID
  - Response: 200 OK with TaskResponse schema
  - Error responses: 404 for not found, 500 for server errors

- **PUT /api/v1/tasks/{id}**: Update a specific task
  - Path parameter: task ID
  - Request body: TaskUpdate schema
  - Response: 200 OK with updated TaskResponse schema
  - Error responses: 404 for not found, 422 for validation errors, 500 for server errors

- **DELETE /api/v1/tasks/{id}**: Delete a specific task
  - Path parameter: task ID
  - Response: 204 No Content
  - Error responses: 404 for not found, 500 for server errors

- **PATCH /api/v1/tasks/{id}/status**: Update task completion status
  - Path parameter: task ID
  - Request body: TaskStatusUpdate schema
  - Response: 200 OK with updated TaskResponse schema
  - Error responses: 404 for not found, 422 for validation errors, 500 for server errors

## Task Status Toggle Logic

The task status toggle functionality will be implemented through:
- A dedicated PATCH endpoint for status updates
- Input validation to ensure only boolean values are accepted
- Business logic to update the completion status in the database
- Automatic timestamp update for the updated_at field
- Return the updated task to confirm the status change

## Error Handling Strategy

The error handling strategy includes:
- Custom exception classes for different error types (TaskNotFound, ValidationError)
- Global exception handlers in FastAPI to catch and format errors
- Consistent error response format using Pydantic schemas
- Logging of errors with appropriate severity levels
- Validation errors handled automatically by Pydantic with detailed messages
- Database errors caught and converted to appropriate HTTP responses

## Database Connection Lifecycle

The database connection management follows these patterns:
- Async SQLAlchemy engine for PostgreSQL connection
- Dependency injection for database sessions in API endpoints
- Session creation per request with automatic cleanup
- Connection pooling configuration for performance
- Proper disposal of connections when application shuts down
- Health check endpoint to verify database connectivity

## Environment Variable Management

Environment variables will be managed through:
- A configuration class that loads variables from .env files
- Required variables: DATABASE_URL, DATABASE_HOST, DATABASE_PORT, DATABASE_NAME, DATABASE_USER, DATABASE_PASSWORD
- Optional variables: LOG_LEVEL, MAX_CONNECTIONS, MIN_CONNECTIONS
- Validation of required environment variables at startup
- Default values for non-critical configuration options

## Implementation Phases

### Phase 1: Project Setup and Configuration
- Set up project structure
- Configure dependencies (requirements.txt)
- Set up environment variable handling
- Configure database connection settings

### Phase 2: Database Layer
- Define SQLAlchemy models
- Set up database connection and session management
- Create Alembic migration configuration
- Implement database utility functions

### Phase 3: Schema Layer
- Define Pydantic schemas for requests and responses
- Implement validation logic
- Create error response schemas

### Phase 4: Service Layer
- Implement business logic in service classes
- Create data access methods
- Implement error handling logic

### Phase 5: API Layer
- Define API routes using FastAPI
- Implement endpoint handlers
- Connect endpoints to service layer
- Add request/response validation

### Phase 6: Testing and Documentation
- Write unit and integration tests
- Create API documentation
- Implement health check endpoints
- Add logging configuration

## Success Criteria
- All CRUD operations function correctly through API endpoints
- Database operations are efficient and maintain data integrity
- API responses follow consistent format with appropriate HTTP status codes
- Error handling provides meaningful feedback to clients
- Application can be deployed and run with proper environment configuration
- Tests provide adequate coverage for all major functionality