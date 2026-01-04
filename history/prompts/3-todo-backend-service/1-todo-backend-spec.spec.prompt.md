---
id: 1
title: todo-backend-spec
stage: spec
date_iso: 2026-01-04
surface: agent
model: claude-sonnet-4-5-20250929
feature: todo-backend-service
branch: 3-todo-backend-service
user: Claude
command: /sp.specify
labels: ["specification", "todo-app", "backend", "postgresql", "rest-api"]
links:
  spec: "specs/3-todo-backend-service/spec.md"
  ticket: null
  adr: null
  pr: null
files_yaml:
  - "specs/3-todo-backend-service/spec.md"
  - "specs/3-todo-backend-service/checklists/requirements.md"
tests_yaml: []
prompt_text: |
  /sp.specify

  Build a backend service for a Todo Application where tasks are persisted in a PostgreSQL database.

  Objective:
  Provide a RESTful backend that supports full CRUD operations for Todo tasks and stores data in PostgreSQL.

  Core Features:
  - Create a task with title, description, and status
  - Fetch all tasks
  - Fetch a task by ID
  - Update task title, description, and status
  - Delete a task by ID
  - Mark task as complete or incomplete

  Tech Stack:
  - Python
  - UV (ASGI server)
  - FastAPI
  - PostgreSQL
  - SQLAlchemy ORM
  - Pydantic for data validation

  Database Requirements:
  - PostgreSQL as primary datastore
  - Auto-increment task ID
  - Store task title, description, status, timestamps

  Non-Goals:
  - No frontend implementation
  - No authentication or user management
  - No deployment setup

  Quality Requirements:
  - Clean REST API design
  - Proper error handling
  - Schema validation
  - Modular folder structure
  - Ready for frontend integration
response_text: |
  Created specification for Todo Backend Service with PostgreSQL. The specification includes:
  - User scenarios for CRUD operations and task management
  - Functional requirements covering all API endpoints and data validation
  - Key entities (Task) with database fields
  - Success criteria with measurable outcomes
  - Edge cases and error handling requirements

  The spec defines a RESTful API with endpoints for:
  - POST /tasks (create task)
  - GET /tasks (get all tasks)
  - GET /tasks/{id} (get specific task)
  - PUT /tasks/{id} (update task)
  - DELETE /tasks/{id} (delete task)
  - PATCH /tasks/{id} (update task status)

  The database will store tasks with auto-incrementing IDs, title, description, completion status, and timestamps.
outcome: "Specification successfully created for Todo Backend Service with PostgreSQL persistence, covering all CRUD operations and API contracts."
evaluation: "Specification meets all requirements with clear user scenarios, functional requirements, and measurable success criteria. No implementation details included."
---

# Prompt: todo-backend-spec

## Summary

Created specification for Todo Backend Service with PostgreSQL. The specification includes user scenarios, functional requirements, and success criteria for a RESTful backend service.

## Details

**Goal:** Build a backend service for a Todo Application where tasks are persisted in a PostgreSQL database.

**Objective:** Provide a RESTful backend that supports full CRUD operations for Todo tasks and stores data in PostgreSQL.

**Core Features:**
- Create a task with title, description, and status
- Fetch all tasks
- Fetch a task by ID
- Update task title, description, and status
- Delete a task by ID
- Mark task as complete or incomplete

**Tech Stack:**
- Python
- UV (ASGI server)
- FastAPI
- PostgreSQL
- SQLAlchemy ORM
- Pydantic for data validation

**Database Requirements:**
- PostgreSQL as primary datastore
- Auto-increment task ID
- Store task title, description, status, timestamps

**Non-Goals:**
- No frontend implementation
- No authentication or user management
- No deployment setup

**Quality Requirements:**
- Clean REST API design
- Proper error handling
- Schema validation
- Modular folder structure
- Ready for frontend integration

## Response

Created specification for Todo Backend Service with PostgreSQL. The specification includes:
- User scenarios for CRUD operations and task management
- Functional requirements covering all API endpoints and data validation
- Key entities (Task) with database fields
- Success criteria with measurable outcomes
- Edge cases and error handling requirements

The spec defines a RESTful API with endpoints for:
- POST /tasks (create task)
- GET /tasks (get all tasks)
- GET /tasks/{id} (get specific task)
- PUT /tasks/{id} (update task)
- DELETE /tasks/{id} (delete task)
- PATCH /tasks/{id} (update task status)

The database will store tasks with auto-incrementing IDs, title, description, completion status, and timestamps.