tasks = []
completed_tasks = []

def show_tasks():
    """Show all tasks."""
    if len(tasks) == 0:
        print("Your to-do list is empty!")
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    """Add a new task."""
    task = input("Enter the task: ")
    tasks.append(task)  # Add task to the list
    print(f"Task '{task}' added to your list!")

def update_task():
    """Update an existing task."""
    show_tasks()
    if len(tasks) > 0:
        task_num = int(input("Enter the task number to update: ")) - 1
        if 0 <= task_num < len(tasks):
            new_task = input("Enter the new task description: ")
            tasks[task_num] = new_task
            print("Task updated successfully!")
        else:
            print("Invalid task number!")

def delete_task():
    """Delete an existing task."""
    show_tasks()
    if len(tasks) > 0:
        task_num = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            removed_task = tasks.pop(task_num)  # Fix: removed_task is assigned the deleted task
            print(f"Task '{removed_task}' removed from your list!")
        else:
            print("Invalid task number!")

def mark_task_completed():
    """Mark a task as completed."""
    show_tasks()
    if len(tasks) > 0:
        task_num = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= task_num < len(tasks):
            completed_task = tasks.pop(task_num)
            completed_tasks.append(completed_task)
            print(f"Task '{completed_task}' marked as completed!")
        else:
            print("Invalid task number!")

def show_completed_tasks():
    """Show completed tasks."""
    if len(completed_tasks) == 0:
        print("No tasks have been completed yet.")
    else:
        print("Completed tasks:")
        for i, task in enumerate(completed_tasks, 1):
            print(f"{i}. {task}")

def show_menu():
    """Show menu options."""
    print("\n--- To-Do List Menu ---")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Update task")
    print("4. Delete task")
    print("5. Mark task as completed")
    print("6. Show completed tasks")
    print("7. Exit")

def main():
    """Main function to run the app."""
    while True:
        show_menu()
        choice = input("Choose an option (1-7): ")
        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            mark_task_completed()
        elif choice == "6":
            show_completed_tasks()
        elif choice == "7":
            print("Exiting the to-do list app.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()