# Todo Backend Service

A RESTful backend service for a Todo application using PostgreSQL as the primary data store. Built with Python, FastAPI, SQLAlchemy ORM, and Pydantic for data validation.

## Tech Stack

- **Language**: Python 3.12+
- **Web Framework**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Validation**: Pydantic
- **ASGI Server**: Uvicorn

## Features

- Create, read, update, and delete todo tasks
- Mark tasks as complete/incomplete
- RESTful API design
- Data validation and error handling
- PostgreSQL persistence with async support

## API Endpoints

### Tasks

- `POST /api/v1/tasks` - Create a new task
  - Request body: `{ "title": "Task title", "description": "Task description" }`
  - Response: 201 Created with the created task object
  - Validation: Title is required (1-200 chars), description is optional (max 1000 chars)

- `GET /api/v1/tasks` - Retrieve all tasks
  - Query parameters: `skip` (default: 0), `limit` (default: 100)
  - Response: 200 OK with array of task objects

- `GET /api/v1/tasks/{id}` - Retrieve a specific task
  - Path parameter: task ID
  - Response: 200 OK with the task object or 404 if not found

- `PUT /api/v1/tasks/{id}` - Update a specific task
  - Path parameter: task ID
  - Request body: `{ "title"?: "New title", "description"?: "New description", "completed"?: true/false }`
  - Response: 200 OK with the updated task object or 404 if not found

- `DELETE /api/v1/tasks/{id}` - Delete a specific task
  - Path parameter: task ID
  - Response: 204 No Content or 404 if not found

- `PATCH /api/v1/tasks/{id}/status` - Update task completion status
  - Path parameter: task ID
  - Request body: `{ "completed": true/false }`
  - Response: 200 OK with the updated task object or 404 if not found

### Health Check

- `GET /` - Root endpoint to check if the service is running
- `GET /health` - Health check endpoint to verify service status

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Copy `.env.example` to `.env` and update the database configuration:
   ```bash
   cp .env.example .env
   ```
5. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

## Environment Variables

The application uses the following environment variables:

- `DATABASE_URL` - PostgreSQL connection string
- `DATABASE_HOST` - Database host
- `DATABASE_PORT` - Database port
- `DATABASE_NAME` - Database name
- `DATABASE_USER` - Database user
- `DATABASE_PASSWORD` - Database password
- `LOG_LEVEL` - Logging level (default: info)

## Database Migrations

This project uses Alembic for database migrations:

1. To create a new migration:
   ```bash
   alembic revision --autogenerate -m "Description of changes"
   ```
2. To apply migrations:
   ```bash
   alembic upgrade head
   ```

## Testing

Run the tests using pytest:
```bash
pytest
```