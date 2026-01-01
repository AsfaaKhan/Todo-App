import questionary
from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.prompt import Prompt
import sys
import os

# Add the src directory to the Python path to allow absolute imports
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from src.services.task_service import TaskService
from src.models.task import Task
from src.lib.formatters import TaskFormatter


class TodoCLI:
    """
    Main CLI application with interactive menu using Questionary.
    """

    def __init__(self):
        """Initialize the CLI application with a task service and formatter."""
        self.task_service = TaskService()
        self.formatter = TaskFormatter()
        self.console = Console()

    def run(self):
        """Start the main application loop."""
        self.console.clear()
        print(Panel("[bold blue]🎯 TODO CLI APPLICATION[/bold blue]", expand=False))
        print("[bold green]Welcome! Manage your tasks efficiently.[/bold green]\n")

        while True:
            try:
                # Display main menu options
                choice = questionary.select(
                    "📋 [bold yellow]What would you like to do?[/bold yellow]",
                    choices=[
                        {"name": "➕ Add Task", "value": "add"},
                        {"name": "📋 View All Tasks", "value": "view"},
                        {"name": "✏️ Update Task", "value": "update"},
                        {"name": "🗑️ Delete Task", "value": "delete"},
                        {"name": "✅ Mark Task Complete", "value": "complete"},
                        {"name": "⏳ Mark Task Incomplete", "value": "incomplete"},
                        {"name": "🚪 Exit", "value": "exit"}
                    ],
                    qmark=""
                ).ask()

                if choice == "add":
                    self.add_task()
                elif choice == "view":
                    self.view_all_tasks()
                elif choice == "update":
                    self.update_task()
                elif choice == "delete":
                    self.delete_task()
                elif choice == "complete":
                    self.mark_task_complete()
                elif choice == "incomplete":
                    self.mark_task_incomplete()
                elif choice == "exit":
                    print("\n[bold green]👋 Goodbye! Have a productive day![/bold green]")
                    break

                # Add a pause to see the result before showing the menu again
                print("\n[italic dim]Press Enter to continue...[/italic dim]", end="")
                input()
                self.console.clear()
                print(Panel("[bold blue]🎯 TODO CLI APPLICATION[/bold blue]", expand=False))
                print("[bold green]Welcome back! Continue managing your tasks.[/bold green]\n")

            except KeyboardInterrupt:
                print("\n\n[bold red]👋 Goodbye! Have a productive day![/bold red]")
                break

    def add_task(self):
        """Add a new task to the system."""
        print(Panel("[bold yellow]➕ ADDING A NEW TASK[/bold yellow]", expand=False))

        title = questionary.text("📝 Enter task title:").ask()
        if not title:
            print("[red]❌ Task title cannot be empty![/red]")
            return

        description = questionary.text("💬 Enter task description (optional):").ask() or ""

        try:
            task = self.task_service.add_task(title, description)
            print(f"[green]✅ Task added successfully! ID: {task.id}[/green]")
            print(f"[bold]Title:[/bold] {task.title}")
            if task.description:
                print(f"[bold]Description:[/bold] {task.description}")
        except ValueError as e:
            print(f"[red]❌ Error: {e}[/red]")

    def view_all_tasks(self):
        """Display all tasks in the system."""
        print(Panel("[bold yellow]📋 VIEWING ALL TASKS[/bold yellow]", expand=False))

        tasks = self.task_service.get_all_tasks()

        if not tasks:
            print("[yellow]⚠️ No tasks found![/yellow]")
            return

        print(f"[bold cyan]Total tasks: {len(tasks)}[/bold cyan]\n")
        self.formatter.print_tasks_table(tasks)

    def update_task(self):
        """Update an existing task."""
        print(Panel("[bold yellow]✏️ UPDATING A TASK[/bold yellow]", expand=False))

        tasks = self.task_service.get_all_tasks()

        if not tasks:
            print("[yellow]⚠️ No tasks available to update![/yellow]")
            return

        task_ids = [str(task.id) for task in tasks]
        selected_id = questionary.select(
            "🔢 Select task ID to update:",
            choices=task_ids
        ).ask()

        if selected_id:
            task_id = int(selected_id)
            task = self.task_service.find_task_by_id(task_id)

            if task:
                print(f"[bold blue]Updating task {task_id}:[/bold blue]")
                print(f"Current title: [italic]{task.title}[/italic]")
                if task.description:
                    print(f"Current description: [italic]{task.description}[/italic]")

                # Keep existing values as defaults
                new_title = questionary.text("📝 Enter new title:", default=task.title).ask()
                new_description = questionary.text("💬 Enter new description:", default=task.description).ask()

                if self.task_service.update_task(task_id, new_title, new_description):
                    print(f"[green]✅ Task {task_id} updated successfully![/green]")
                else:
                    print(f"[red]❌ Failed to update task {task_id}[/red]")
            else:
                print(f"[red]❌ Task with ID {task_id} not found![/red]")

    def delete_task(self):
        """Delete a task by ID."""
        print(Panel("[bold yellow]🗑️ DELETING A TASK[/bold yellow]", expand=False))

        tasks = self.task_service.get_all_tasks()

        if not tasks:
            print("[yellow]⚠️ No tasks available to delete![/yellow]")
            return

        task_ids = [str(task.id) for task in tasks]
        selected_id = questionary.select(
            "🔢 Select task ID to delete:",
            choices=task_ids
        ).ask()

        if selected_id:
            task_id = int(selected_id)
            task = self.task_service.find_task_by_id(task_id)

            if task:
                print(f"[bold red]You are about to delete:[/bold red]")
                print(f"  ID: {task.id}")
                print(f"  Title: {task.title}")
                if task.description:
                    print(f"  Description: {task.description}")
                print(f"  Status: {'✅ Completed' if task.completed else '⏳ Pending'}")

                # Confirmation prompt
                confirm = questionary.confirm(f"⚠️ Are you sure you want to delete task {task_id}?").ask()

                if confirm and self.task_service.delete_task(task_id):
                    print(f"[green]✅ Task {task_id} deleted successfully![/green]")
                elif not confirm:
                    print("[yellow]❌ Deletion cancelled.[/yellow]")
                else:
                    print(f"[red]❌ Failed to delete task {task_id}[/red]")
            else:
                print(f"[red]❌ Task with ID {task_id} not found![/red]")

    def mark_task_complete(self):
        """Mark a task as complete."""
        print(Panel("[bold yellow]✅ MARKING TASK AS COMPLETE[/bold yellow]", expand=False))

        tasks = self.task_service.get_all_tasks()

        if not tasks:
            print("[yellow]⚠️ No tasks available![/yellow]")
            return

        pending_tasks = [task for task in tasks if not task.completed]

        if not pending_tasks:
            print("[yellow]⚠️ No pending tasks to mark as complete![/yellow]")
            return

        task_ids = [str(task.id) for task in pending_tasks]
        selected_id = questionary.select(
            "🔢 Select task ID to mark as complete:",
            choices=task_ids
        ).ask()

        if selected_id:
            task_id = int(selected_id)
            task = self.task_service.find_task_by_id(task_id)

            if task:
                print(f"[bold blue]Marking task as complete:[/bold blue]")
                print(f"  ID: {task.id}")
                print(f"  Title: {task.title}")

                if self.task_service.mark_task_complete(task_id, True):
                    print(f"[green]✅ Task {task_id} marked as complete![/green]")
                else:
                    print(f"[red]❌ Failed to mark task {task_id} as complete[/red]")
            else:
                print(f"[red]❌ Task with ID {task_id} not found![/red]")

    def mark_task_incomplete(self):
        """Mark a task as incomplete."""
        print(Panel("[bold yellow]⏳ MARKING TASK AS INCOMPLETE[/bold yellow]", expand=False))

        tasks = self.task_service.get_all_tasks()

        if not tasks:
            print("[yellow]⚠️ No tasks available![/yellow]")
            return

        completed_tasks = [task for task in tasks if task.completed]

        if not completed_tasks:
            print("[yellow]⚠️ No completed tasks to mark as incomplete![/yellow]")
            return

        task_ids = [str(task.id) for task in completed_tasks]
        selected_id = questionary.select(
            "🔢 Select task ID to mark as incomplete:",
            choices=task_ids
        ).ask()

        if selected_id:
            task_id = int(selected_id)
            task = self.task_service.find_task_by_id(task_id)

            if task:
                print(f"[bold blue]Marking task as incomplete:[/bold blue]")
                print(f"  ID: {task.id}")
                print(f"  Title: {task.title}")

                if self.task_service.mark_task_complete(task_id, False):
                    print(f"[green]✅ Task {task_id} marked as incomplete![/green]")
                else:
                    print(f"[red]❌ Failed to mark task {task_id} as incomplete[/red]")
            else:
                print(f"[red]❌ Task with ID {task_id} not found![/red]")


def main():
    """Entry point for the application."""
    app = TodoCLI()
    app.run()


if __name__ == "__main__":
    main()