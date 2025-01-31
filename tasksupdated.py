# ChatGPT provided this code.
import json
import os

# A json file is used for storing list assignments
ASSIGNMENTS_FILE = "assignments.json"

# Load assignments from JSON file
def load_assignments():
    if os.path.exists(ASSIGNMENTS_FILE):
        with open(ASSIGNMENTS_FILE, "r") as file:
            return json.load(file)
    return []

# Save assignments to JSON file
def save_assignments(assignments):
    with open(ASSIGNMENTS_FILE, "w") as file:
        json.dump(assignments, file, indent=5)

# Add new assignment
def add_assignment(assignments, assignment_info:
    assignment = {
        "information": assignment_information,
        "completed": False
    }
    assignments.append(assignment)
    save_assignments(assignments)
    print(f"Assignment '{assignment_information}' has been input into the program.")

# List all tasks
def list_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    for idx, task in enumerate(tasks, 1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{idx}. {task['description']} - {status}")

# Mark a task as completed or toggle its status
def toggle_task_completed(tasks, task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = not tasks[task_index]["completed"]
        status = "Completed" if tasks[task_index]["completed"] else "Pending"
        save_tasks(tasks)
        print(f"Task {task_index + 1} is now {status}.")
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
        print("3. Toggle task completion (Complete/Incomplete)")
        print("4. Remove task")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            list_tasks(tasks)
        elif choice == '2':
            task_description = input("Enter the task description: ")
            add_task(tasks, task_description)
        elif choice == '3':
            task_number = int(input("Enter task number to toggle completion: ")) - 1
            toggle_task_completed(tasks, task_number)
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
