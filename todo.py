import json

# File to store tasks
TASKS_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Display tasks
def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks found!")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            status = "✅" if task["done"] else "❌"
            print(f"{i}. {task['task']} {status}")

# Add a new task
def add_task(tasks):
    task_name = input("\nEnter a new task: ")
    priority = input("Enter priority (High/Medium/Low): ")
    tasks.append({"task": task_name, "priority": priority, "done": False})
    save_tasks(tasks)
    print("Task added!")


# Mark a task as complete
def complete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("\nEnter task number to complete: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            save_tasks(tasks)
            print("Task marked as complete!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Delete a task
def delete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("\nEnter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"Deleted task: {removed['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main menu
def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do App")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
