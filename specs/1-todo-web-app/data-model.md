# Data Model: Todo Web Application

## Task Entity

**Definition**: A single todo item representing a task that can be completed

**Attributes**:
- `id`: string
  - Unique identifier for the task
  - Generated using crypto.randomUUID()
  - Required field
- `title`: string
  - The main text of the task
  - Required field
  - Maximum length: 200 characters
- `description`: string
  - Optional detailed information about the task
  - Maximum length: 1000 characters
  - Default: empty string
- `completed`: boolean
  - Indicates whether the task is completed
  - Default: false
- `createdAt`: Date
  - Timestamp when the task was created
  - Default: new Date()

## TaskList State

**Definition**: The application state for managing multiple tasks

**Attributes**:
- `tasks`: Task[]
  - Array containing all tasks
  - Default: empty array
- `filter`: 'all' | 'active' | 'completed'
  - Determines which tasks to display
  - Default: 'all'
- `editingTaskId`: string | null
  - ID of the task currently being edited
  - Default: null

## Validation Rules

**Task Creation**:
- Title must be provided and not empty
- Title must not exceed 200 characters
- Description (if provided) must not exceed 1000 characters

**Task Updates**:
- ID cannot be changed
- Title must remain non-empty after update
- Title must not exceed 200 characters after update
- Description must not exceed 1000 characters after update

## State Transitions

**Task Completion**:
- When marking as complete: `completed` changes from `false` to `true`
- When marking as incomplete: `completed` changes from `true` to `false`

**Task Editing**:
- `editingTaskId` is set to task ID when entering edit mode
- `editingTaskId` is set to `null` when editing is completed or cancelled

## Relationships

**Task to TaskList**:
- Each Task belongs to exactly one TaskList
- TaskList contains multiple Tasks
- Tasks are independent of each other