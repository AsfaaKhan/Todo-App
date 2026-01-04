class TaskNotFound(Exception):
    """
    Exception raised when a task is not found in the database.
    """
    def __init__(self, task_id: int):
        self.task_id = task_id
        super().__init__(f"Task with ID {task_id} not found")


class ValidationError(Exception):
    """
    Exception raised when validation fails for input data.
    """
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class DatabaseError(Exception):
    """
    Exception raised when there's an error with database operations.
    """
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)