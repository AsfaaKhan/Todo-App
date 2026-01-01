# API Contracts: Todo CLI Application

## Task Operations Contract

### Add Task
- **Input**: title (string, required), description (string, optional)
- **Output**: Task object with assigned ID
- **Validation**: Title must not be empty
- **Error cases**: Invalid input, empty title

### View All Tasks
- **Input**: None
- **Output**: List of Task objects
- **Format**: Rich-formatted table with ID, title, description, status

### Update Task
- **Input**: task_id (int), title (string, optional), description (string, optional)
- **Output**: Updated Task object
- **Validation**: Task must exist
- **Error cases**: Task not found

### Delete Task
- **Input**: task_id (int)
- **Output**: Success confirmation
- **Validation**: Task must exist
- **Error cases**: Task not found

### Mark Task Complete/Incomplete
- **Input**: task_id (int), completed (boolean)
- **Output**: Updated Task object
- **Validation**: Task must exist
- **Error cases**: Task not found