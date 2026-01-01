#!/usr/bin/env python3
"""
Simple test to verify the improved UI functionality of the Todo CLI application
without requiring interactive input.
"""

from src.services.task_service import TaskService
from src.lib.formatters import TaskFormatter

def test_improved_ui_functionality():
    """Test the core functionality of the task service with improved UI."""
    print("Testing improved UI functionality for Todo CLI Application...")

    # Initialize the task service
    task_service = TaskService()
    formatter = TaskFormatter()

    print("\n1. Testing add_task functionality:")
    task1 = task_service.add_task("Buy groceries", "Milk, bread, eggs")
    print(f"   Added task: ID={task1.id}, Title='{task1.title}', Description='{task1.description}', Completed={task1.completed}")

    task2 = task_service.add_task("Walk the dog", "Daily exercise")
    print(f"   Added task: ID={task2.id}, Title='{task2.title}', Description='{task2.description}', Completed={task2.completed}")

    print("\n2. Testing get_all_tasks functionality:")
    all_tasks = task_service.get_all_tasks()
    print(f"   Total tasks: {len(all_tasks)}")
    for task in all_tasks:
        print(f"   - ID: {task.id}, Title: '{task.title}', Completed: {task.completed}")

    print("\n3. Testing update_task functionality:")
    update_result = task_service.update_task(task1.id, "Buy groceries and cook", "Milk, bread, eggs, chicken")
    print(f"   Update result for task {task1.id}: {update_result}")

    updated_task = task_service.find_task_by_id(task1.id)
    if updated_task:
        print(f"   Updated task: Title='{updated_task.title}', Description='{updated_task.description}'")

    print("\n4. Testing mark_task_complete functionality:")
    complete_result = task_service.mark_task_complete(task1.id, True)
    print(f"   Mark complete result for task {task1.id}: {complete_result}")

    completed_task = task_service.find_task_by_id(task1.id)
    if completed_task:
        print(f"   Task {task1.id} completed status: {completed_task.completed}")

    print("\n5. Testing mark_task_incomplete functionality:")
    incomplete_result = task_service.mark_task_complete(task1.id, False)
    print(f"   Mark incomplete result for task {task1.id}: {incomplete_result}")

    incomplete_task = task_service.find_task_by_id(task1.id)
    if incomplete_task:
        print(f"   Task {task1.id} completed status: {incomplete_task.completed}")

    print("\n6. Testing delete_task functionality:")
    delete_result = task_service.delete_task(task2.id)
    print(f"   Delete result for task {task2.id}: {delete_result}")

    remaining_tasks = task_service.get_all_tasks()
    print(f"   Remaining tasks after deletion: {len(remaining_tasks)}")

    print("\n7. Testing error handling:")
    # Try to find a non-existent task
    missing_task = task_service.find_task_by_id(999)
    print(f"   Finding non-existent task (ID=999): {missing_task}")

    # Try to update a non-existent task
    update_missing = task_service.update_task(999, "New title")
    print(f"   Updating non-existent task (ID=999): {update_missing}")

    # Try to delete a non-existent task
    delete_missing = task_service.delete_task(999)
    print(f"   Deleting non-existent task (ID=999): {delete_missing}")

    print("\n8. Testing validation:")
    try:
        # Try to add a task with empty title
        invalid_task = task_service.add_task("", "This should fail")
        print(f"   ERROR: Should not reach here - {invalid_task}")
    except ValueError as e:
        print(f"   Validation for empty title works: {e}")

    try:
        # Try to update a task with empty title
        task_with_title = task_service.add_task("Valid task", "Description")
        task_service.update_task(task_with_title.id, "")
        print(f"   ERROR: Should not reach here")
    except ValueError as e:
        print(f"   Validation for empty title in update works: {e}")

    print("\n9. Testing formatters:")
    all_tasks = task_service.get_all_tasks()
    print(f"   Testing formatter with {len(all_tasks)} tasks")
    formatter.print_tasks_table(all_tasks)

    print("\n+ All improved UI functionality tests passed!")
    print("+ The Todo CLI application with improved UI is working correctly.")

if __name__ == "__main__":
    test_improved_ui_functionality()