# Quickstart: Todo CLI Application

## Prerequisites

- Python 3.12 or higher
- UV package manager

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   uv sync
   ```

   Or if starting fresh:
   ```bash
   uv init
   uv add rich questionary
   ```

## Running the Application

```bash
# Run the CLI application
python -m src.cli.main

# Or if entry point is configured
python main.py
```

## Basic Usage

1. Launch the application
2. Use the interactive menu to:
   - Add a new task
   - View all tasks
   - Update an existing task
   - Delete a task
   - Mark a task as complete/incomplete

## Project Structure

- `src/models/task.py`: Task data model
- `src/services/task_service.py`: Business logic for task operations
- `src/cli/main.py`: Main CLI interface with Questionary menus
- `src/lib/validators.py`: Input validation utilities

## Development

1. Make changes to the source files
2. Run the application to test changes
3. All data is stored in-memory only during the session