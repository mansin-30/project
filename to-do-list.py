import json
import os

# File to store tasks
TASKS_FILE = "tasks.json"

# Load existing tasks from file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Function to add a new task
def add_task(title):
    tasks = load_tasks()
    tasks.append({"title": title, "completed": False})
    save_tasks(tasks)
    print(f"Task '{title}' added successfully!\n")

# Function to view tasks
def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.\n")
        return
    print("Your To-Do List:")
    for idx, task in enumerate(tasks, start=1):
        status = "✓ Completed" if task["completed"] else "✗ Pending"
        print(f"{idx}. {task['title']} - [{status}]")
    print()

# Function to mark a task as completed
def complete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        save_tasks(tasks)
        print(f"Task '{tasks[index]['title']}' marked as completed!\n")
    else:
        print("Invalid task number!\n")

# Function to delete a completed task
def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        if tasks[index]["completed"]:
            deleted_task = tasks.pop(index)
            save_tasks(tasks)
            print(f"Task '{deleted_task['title']}' deleted successfully!\n")
        else:
            print("Task is not completed yet. Complete it before deleting!\n")
    else:
        print("Invalid task number!\n")

# Main menu
def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Completed Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            title = input("Enter task title: ").strip()
            add_task(title)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks()
            try:
                task_num = int(input("Enter task number to mark as completed: ")) - 1
                complete_task(task_num)
            except ValueError:
                print("Invalid input! Enter a number.\n")
        elif choice == "4":
            view_tasks()
            try:
                task_num = int(input("Enter task number to delete (only completed tasks allowed): ")) - 1
                delete_task(task_num)
            except ValueError:
                print("Invalid input! Enter a number.\n")
        elif choice == "5":
            print("Exiting... Have a great day!")
            break
        else:
            print("Invalid choice! Please enter a number between 1-5.\n")

# Run the application
if __name__ == "__main__":
    main()
    