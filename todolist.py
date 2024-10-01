# To-Do List  App

tasks = []

def show_tasks():
    """Show all tasks."""
    if len(tasks) == 0:
        print("Your to-do list is empty!")
    else:
        print("Your tasks:")
        #loop to show all tasks in the list

def add_task():
    """Add a new task."""
    task = input("Enter the task: ")
    #add task to the list
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
            #delete task at index "task_num"
            print(f"Task '{removed_task}' removed from your list!")
        else:
            print("Invalid task number!")

def show_menu():
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
        show_menu()
        choice = input("Choose an option (1-5): ")
        #if-else ladder to take choices from user including for show_tasks, add_tasks, update_task, delete_task, exit and one if wrong input is given

if __name__ == "__main__":
    main()
