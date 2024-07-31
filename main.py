import datetime


class Task:
    def __init__(self, task_id, description):
        self.task_id = task_id
        self.description = description
        self.created_at = datetime.datetime.now()
        self.completed = False
        self.category = None

    def mark_as_completed(self):
        self.completed = True

    def set_category(self, category):
        self.category = category

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        category = f"Category: {self.category}" if self.category else "No Category"
        return f"[{self.task_id}] {self.description} - Created at: {self.created_at} - Status: {status} - {category}"


class ToDoListManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, description):
        task = Task(self.next_id, description)
        self.tasks.append(task)
        self.next_id += 1
        print(f"Task added: {task}")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            for task in self.tasks:
                print(task)

    def mark_task_as_completed(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.mark_as_completed()
                print(f"Task marked as completed: {task}")
                return
        print(f"Task with ID {task_id} not found.")

    def clear_tasks(self):
        self.tasks.clear()
        print("All tasks have been cleared.")

    def set_task_category(self, task_id, category):
        for task in self.tasks:
            if task.task_id == task_id:
                task.set_category(category)
                print(f"Category set for task {task_id}: {category}")
                return
        print(f"Task with ID {task_id} not found.")


def main():
    manager = ToDoListManager()

    while True:
        print("\n1. Add a new task")
        print("2. List all tasks")
        print("3. Mark a task as completed")
        print("4. Clear the entire to-do list")
        print("5. Set a category for a task")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter the task description: ")
            manager.add_task(description)
        elif choice == '2':
            manager.list_tasks()
        elif choice == '3':
            try:
                task_id = int(input("Enter the task ID to mark as completed: "))
                manager.mark_task_as_completed(task_id)
            except ValueError:
                print("Invalid input. Please enter a valid task ID.")
        elif choice == '4':
            manager.clear_tasks()
        elif choice == '5':
            try:
                task_id = int(input("Enter the task ID to set category: "))
                category = input("Enter the category: ")
                manager.set_task_category(task_id, category)
            except ValueError:
                print("Invalid input. Please enter a valid task ID.")
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

