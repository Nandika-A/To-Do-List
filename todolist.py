class ToDoList:
    def __init__(self):
        """Initialize an empty task list."""
        self.tasks = []

    def show_tasks(self):
        """Show all tasks."""
        if len(self.tasks) == 0:
            print("Your to-do list is empty!")
        else:
            print("Your tasks:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    def add_task(self):
        """Add a new task."""
        task = input("Enter the task: ")
        self.tasks.append(task)
        print(f"Task '{task}' added to your list!")

    def update_task(self):
        """Update an existing task."""
        self.show_tasks()
        if len(self.tasks) > 0:
            task_num = int(input("Enter the task number to update: ")) - 1
            if 0 <= task_num < len(self.tasks):
                new_task = input("Enter the new task description: ")
                self.tasks[task_num] = new_task
                print("Task updated successfully!")
            else:
                print("Invalid task number!")

    def delete_task(self):
        """Delete an existing task."""
        self.show_tasks()
        if len(self.tasks) > 0:
            task_num = int(input("Enter the task number to delete: ")) - 1
            if 0 <= task_num < len(self.tasks):
                removed_task = self.tasks.pop(task_num)
                print(f"Task '{removed_task}' removed from your list!")
            else:
                print("Invalid task number!")

    def show_menu(self):
        """Show menu options."""
        print("\n--- To-Do List Menu ---")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Update task")
        print("4. Delete task")
        print("5. Exit")

    def main(self):
        """Main function to run the app."""
        while True:
            self.show_menu()
            choice = int(input("Choose an option (1-5): "))
            if choice == 1:
                self.show_tasks()
            elif choice == 2:
                self.add_task()
            elif choice == 3:
                self.update_task()
            elif choice == 4:
                self.delete_task()
            elif choice == 5:
                print("Exiting the app...")
                break
            else:
                print("Invalid choice! Please try again.")

if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.main()
