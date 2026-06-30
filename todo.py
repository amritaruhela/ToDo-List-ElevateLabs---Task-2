import os

TASK_FILE = "tasks.txt"


def load_tasks():
    """Load tasks from the text file."""
    if not os.path.exists(TASK_FILE):
        open(TASK_FILE, "w").close()

    with open(TASK_FILE, "r") as file:
        return [task.strip() for task in file.readlines()]


def save_tasks(tasks):
    """Save tasks to the text file."""
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def view_tasks(tasks):
    """Display all tasks."""
    print("\n" + "=" * 40)
    print("            YOUR TO-DO LIST")
    print("=" * 40)

    if not tasks:
        print("No tasks available.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

    print("=" * 40)


def add_task(tasks):
    """Add a new task."""
    task = input("Enter a new task: ").strip()

    if task == "":
        print("Task cannot be empty!")
        return

    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully.")


def remove_task(tasks):
    """Remove an existing task."""
    if not tasks:
        print("No tasks to remove.")
        return

    view_tasks(tasks)

    try:
        task_number = int(input("Enter task number to remove: "))

        if 1 <= task_number <= len(tasks):
            removed = tasks.pop(task_number - 1)
            save_tasks(tasks)
            print(f'Task "{removed}" removed successfully.')
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def display_menu():
    """Display the main menu."""
    print("\n" + "=" * 40)
    print("        TO-DO LIST MANAGER")
    print("=" * 40)
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")
    print("=" * 40)


def main():
    """Main program loop."""
    tasks = load_tasks()

    while True:
        display_menu()

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            view_tasks(tasks)

        elif choice == "2":
            add_task(tasks)

        elif choice == "3":
            remove_task(tasks)

        elif choice == "4":
            print("\nThank you for using the To-Do List Manager!")
            break

        else:
            print("Invalid option. Please choose between 1 and 4.")


if __name__ == "__main__":
    main()
