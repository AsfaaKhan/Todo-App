# Data Model: Todo CLI Application

## Task Entity

**Name**: Task
**Description**: Represents a todo item with basic properties
**Fields**:
- `id` (int): Auto-incrementing unique identifier for the task
- `title` (str): Title of the task (required, non-empty)
- `description` (str): Detailed description of the task (optional)
- `completed` (bool): Boolean indicating if the task is completed (default: False)

**Validation Rules**:
- `id`: Auto-generated, must be unique within the application session
- `title`: Required field, must not be empty or None
- `description`: Optional field, can be empty string
- `completed`: Boolean value, defaults to False when creating new tasks

**State Transitions**:
- `pending` → `completed`: When user marks task as complete
- `completed` → `pending`: When user marks task as incomplete

## Task List Entity

**Name**: TaskList
**Description**: Collection of Task entities managed in memory
**Fields**:
- `tasks` (list): List of Task objects
- `next_id` (int): Counter for generating next available ID (auto-increment)

**Operations**:
- Add task to list
- Remove task by ID
- Update task by ID
- Get all tasks
- Find task by ID
- Mark task as complete/incomplete by ID