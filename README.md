# Todo CLI Application

A command-line Todo application with in-memory storage, interactive menu using Questionary, and formatted output using Rich.

## Features

- Add, view, update, delete, and mark tasks as complete/incomplete
- Interactive menu using Questionary
- Formatted output using Rich tables, panels, and colors
- Status indicators: ✅ for completed, ⏳ for pending
- In-memory storage only (no persistent storage)
- Enhanced UI with emojis and styled panels

## Prerequisites

- Python 3.12 or higher
- UV package manager

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   uv sync
   ```

## Running the Application

```bash
# Run the CLI application
python -m src.main
```

## Usage

1. Launch the application
2. Use the interactive menu to:
   - Add a new task (with title and optional description)
   - View all tasks (displayed in a Rich-formatted table)
   - Update an existing task (by ID)
   - Delete a task (with confirmation)
   - Mark a task as complete/incomplete

## Project Structure

- `src/main.py`: Main CLI interface with enhanced UI and Questionary menus
- `src/models/task.py`: Task data model with id, title, description, completed status
- `src/models/task_list.py`: In-memory task storage with auto-incrementing ID generation
- `src/services/task_service.py`: Business logic for task operations
- `src/lib/formatters.py`: Rich-based formatting utilities with improved styling

## Development

1. Make changes to the source files
2. Run the application to test changes
3. All data is stored in-memory only during the session