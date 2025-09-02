from typing import List

class TaskManager:
    """Class to manage a list of tasks."""

    def __init__(self):
        """Initialize the TaskManager with an empty task list."""
        self.tasks: List[str] = []

    def add_task(self, task: str) -> None:
        """Add a task to the list."""
        if not task:
            raise ValueError("Task cannot be empty")
        self.tasks.append(task)
        print(f"Task added: {task}")
