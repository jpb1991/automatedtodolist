# The following code with edits to the original code came from https://www.youtube.com/watch?v=1XDZ9Dy6qo4
# ChatGPT fixed this code.
tasks = []

def add_task():
    # add a task
    task = input("Enter task: ")
    tasks.append(task)
    print("The task has been added.")

def view_tasks():
    # view the tasks
    if len(tasks) == 0:  # Fixed the condition
        print("Tasks are not currently available.")
    else:
        print('The tasks are:')
        for i, task in enumerate(tasks):
            print(f'{i+1}. {task}')

def remove_task():
    # remove a task
    if len(tasks) == 0:  # Fixed the condition
        print("Tasks are not currently available to be removed.")
    else:
        print('The tasks are:')
        for i, task in enumerate(tasks):
            print(f'{i+1}. {task}')
        choice = int(input('Enter the task number to remove it:'))
        if 0 < choice <= len(tasks):
            del tasks[choice-1]
            print('The task has been removed.')
        else:
            print('Invalid task number. Please make another selection.')

def main():
    while True:
        print("1. Add a task.")
        print("2. View the tasks.")
        print("3. Remove a task.")
        print("4. Exit.")
        choice = int(input("Make a selection: "))  # Added colon for clarity
        if choice == 1:
            add_task()
        elif choice == 2:  # Fixed the condition
            view_tasks()
        elif choice == 3:
            remove_task()
        elif choice == 4:
            print("Goodbye.")
            break
        else:
            print('Please make another selection.')

if __name__ == "__main__":
    main()
