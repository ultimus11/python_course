from collections import OrderedDict
from functools import wraps

# Decorator for logging actions
def log_action(action):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"\n--- {action} ---")
            result = func(*args, **kwargs)
            print(f"--- {action} Complete ---\n")
            return result
        return wrapper
    return decorator

# Decorator to check if there are tasks
def require_tasks(func):
    @wraps(func)
    def wrapper(tasks, *args, **kwargs):
        if not tasks:
            print("\nNo tasks available. Please add tasks first.")
            return
        return func(tasks, *args, **kwargs)
    return wrapper

# Function to display the menu
def show_menu():
    print("To-Do App Menu:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

# View tasks
@log_action("Viewing Tasks")
@require_tasks
def view_tasks(tasks):
    for idx, (task, completed) in enumerate(tasks.items(), start=1):
        status = "✔" if completed else "✗"
        print(f"{idx}. [{status}] {task}")

# Add a task
@log_action("Adding Task")
def add_task(tasks):
    task = input("Enter the task to add: ").strip()
    if task:
        tasks[task] = False
        print(f"Task '{task}' added.")
    else:
        print("Task cannot be empty.")

# Mark a task as completed
@log_action("Marking Task as Completed")
@require_tasks
def mark_task_completed(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to mark as completed: "))
        task = list(tasks.keys())[task_num - 1]
        tasks[task] = True
        print(f"Task '{task}' marked as completed.")
    except (ValueError, IndexError):
        print("Invalid task number.")

# Delete a task
@log_action("Deleting Task")
@require_tasks
def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to delete: "))
        task = list(tasks.keys())[task_num - 1]
        del tasks[task]
        print(f"Task '{task}' deleted.")
    except (ValueError, IndexError):
        print("Invalid task number.")

# Main function
def main():
    tasks = OrderedDict()  # Using OrderedDict to preserve order of tasks
    while True:
        show_menu()
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                view_tasks(tasks)
            elif choice == 2:
                add_task(tasks)
            elif choice == 3:
                mark_task_completed(tasks)
            elif choice == 4:
                delete_task(tasks)
            elif choice == 5:
                print("Exiting the To-Do App. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
