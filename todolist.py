tasks = []

def showTasks():
    """Show all tasks."""
    if len(tasks) == 0:
        print("Your to-do list is empty!")
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def addTask():
    """Add a new task."""
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added to your list!")

def updateTask():
    """Update an existing task."""
    showTasks()
    if len(tasks) > 0:
        try:
            task_num = int(input("Enter the task number to update: ")) - 1
            if 0 <= task_num < len(tasks):
                new_task = input("Enter the new task description: ")
                tasks[task_num] = new_task
                print("Task updated successfully!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number.")

def deleteTask():
    """Delete an existing task."""
    showTasks()
    if len(tasks) > 0:
        try:
            task_num = int(input("Enter the task number to delete: ")) - 1
            if 0 <= task_num < len(tasks):
                removed_task = tasks.pop(task_num)
                print(f"Task '{removed_task}' removed from your list!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number.")

def showMenu():
    """Show menu options."""
    print("\n--- To-Do List Menu ---")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Update task")
    print("4. Delete task")
    print("5. Exit")

def main():
    """Main function to run the app."""
    while True:
        showMenu()
        choice = input("Choose an option (1-5): ")
        if choice == "1":
            showTasks()
        elif choice == "2":
            addTask()
        elif choice == "3":
            updateTask()
        elif choice == "4":
            deleteTask()
        elif choice == "5":
            print("Exiting the app...")
            break
        else:
            print("Invalid choice! Please choose a valid option.")

if __name__ == "__main__":
    main()
