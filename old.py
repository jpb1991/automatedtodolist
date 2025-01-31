// ChatGPT provided this code.
import json
import os

# File to store tasks
TASKS_FILE = "tasks.json"

# Load tasks from the JSON file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

# Save tasks to the JSON file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(tasks, task_description):
    task = {
        "description": task_description,
        "completed": False
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task_description}' added!")

# List all tasks
def list_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    for idx, task in enumerate(tasks, 1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{idx}. {task['description']} - {status}")

# Mark a task as completed
def mark_task_completed(tasks, task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        save_tasks(tasks)
        print(f"Task {task_index + 1} marked as completed.")
    else:
        print("Invalid task number.")

# Remove a task
def remove_task(tasks, task_index):
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        save_tasks(tasks)
        print(f"Task '{removed_task['description']}' removed.")
    else:
        print("Invalid task number.")

# Main menu to interact with the to-do list
def show_menu():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Menu:")
        print("1. List tasks")
        print("2. Add task")
        print("3. Mark task as completed")
        print("4. Remove task")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            list_tasks(tasks)
        elif choice == '2':
            task_description = input("Enter the task description: ")
            add_task(tasks, task_description)
        elif choice == '3':
            task_number = int(input("Enter task number to mark as completed: ")) - 1
            mark_task_completed(tasks, task_number)
        elif choice == '4':
            task_number = int(input("Enter task number to remove: ")) - 1
            remove_task(tasks, task_number)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    show_menu()