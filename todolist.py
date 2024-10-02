class ToDoList:
    """
    A class to represent a to-do list.
    This class handles all operations such as adding, updating, deleting, and showing tasks.
    """
    def __init__(self):
        """
        Initialize the ToDoList class with an empty list of tasks.
        This is the constructor method which is called when an object is created.
        """
        self.tasks = []

    def show_tasks(self):
        """
        Display all tasks in the to-do list.
        If there are no tasks, it shows an appropriate message.
        """
        if len(self.tasks) == 0:
            print("Your to-do list is empty!")
        else:
            print("Your tasks:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    def add_task(self):
        """
        Add a new task to the to-do list.
        The task is input by the user and then appended to the list.
        """
        task = input("Enter the task: ")
        self.tasks.append(task)
        print(f"Task '{task}' added to your list!")

    def update_task(self):
        """
        Update an existing task in the to-do list.
        The user selects which task to update by its index, and then enters a new description.
        """
        self.show_tasks()       # Show current tasks so the user can choose
        if len(self.tasks) > 0:
            task_num = int(input("Enter the task number to update: ")) - 1      # Get task number to update
            if 0 <= task_num < len(self.tasks):
                new_task = input("Enter the new task description: ")
                self.tasks[task_num] = new_task
                print("Task updated successfully!")
            else:
                print("Invalid task number!")

    def delete_task(self):
        """
        Delete a task from the to-do list.
        The user selects which task to delete by its index.
        """
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
                print("...Exiting the app...")
                break
            else:
                print("Invalid choice! Please try again.")

if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.main()
