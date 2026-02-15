"""
Module 09: Final Project - Task Manager CLI

A complete command-line application to manage tasks.
Data is saved to 'tasks.json'.
"""

import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from the JSON file."""
    if not os.path.exists(TASKS_FILE):
        return []
    try:
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        return []

def save_tasks(tasks):
    """Save the current list of tasks to the JSON file."""
    try:
        with open(TASKS_FILE, 'w') as file:
            json.dump(tasks, file, indent=4)
    except IOError as e:
        print(f"Error saving tasks: {e}")

def add_task(tasks):
    """Add a new task."""
    title = input("Enter task title: ").strip()
    if title:
        tasks.append({"title": title, "completed": False})
        print(f"Task '{title}' added.")
    else:
        print("Task title cannot be empty.")

def list_tasks(tasks):
    """List all tasks with their status."""
    print("\n--- Your Tasks ---")
    if not tasks:
        print("No tasks found.")
    for index, task in enumerate(tasks):
        status = "✅" if task["completed"] else "❌"
        print(f"{index + 1}. [{status}] {task['title']}")
    print("------------------\n")

def complete_task(tasks):
    """Mark a task as completed."""
    list_tasks(tasks)
    try:
        task_num = int(input("Enter task number to complete: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    """Delete a task."""
    list_tasks(tasks)
    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"Task '{removed['title']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """Main application loop."""
    tasks = load_tasks()
    
    while True:
        print("\n=== TASK MANAGER CLI ===")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            list_tasks(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please try again.")
        
        # Auto-save after every modification (optional safer approach)
        save_tasks(tasks)

if __name__ == "__main__":
    main()
