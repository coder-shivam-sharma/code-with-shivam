import csv
import datetime

# Task class to represent each task
class Task:
    def __init__(self, name, due_date, priority):
        self.name = name
        self.due_date = due_date
        self.priority = priority
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __repr__(self):
        status = "Completed" if self.completed else "Pending"
        return f"{self.name} (Due: {self.due_date}, Priority: {self.priority}, Status: {status})"

# ToDoList class to manage the tasks
class ToDoList:
    def __init__(self, filename="todo_list.csv"):
        self.tasks = []
        self.filename = filename
        self.load_tasks()

    # Add a task to the list
    def add_task(self, name, due_date, priority):
        task = Task(name, due_date, priority)
        self.tasks.append(task)
        self.save_tasks()

    # Mark a task as completed
    def complete_task(self, task_number):
        if 0 <= task_number < len(self.tasks):
            self.tasks[task_number].mark_completed()
            print(f"Task '{self.tasks[task_number].name}' marked as completed!")
            self.save_tasks()

    # View tasks (sorted by priority or due date)
    def view_tasks(self, sort_by="priority"):
        if sort_by == "priority":
            sorted_tasks = sorted(self.tasks, key=lambda task: task.priority)
        elif sort_by == "due_date":
            sorted_tasks = sorted(self.tasks, key=lambda task: task.due_date)

        for i, task in enumerate(sorted_tasks):
            print(f"{i + 1}. {task}")

    # Save tasks to file (CSV format)
    def save_tasks(self):
        with open(self.filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Due Date", "Priority", "Completed"])
            for task in self.tasks:
                writer.writerow([task.name, task.due_date, task.priority, task.completed])

    # Load tasks from the CSV file
    def load_tasks(self):
        try:
            with open(self.filename, newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    task = Task(
                        name=row["Name"],
                        due_date=row["Due Date"],
                        priority=int(row["Priority"]),
                    )
                    task.completed = row["Completed"] == "True"
                    self.tasks.append(task)
        except FileNotFoundError:
            print(f"No saved tasks found. Starting a new To-Do List!")

# Main program to run the To-Do List app
def main():
    todo_list = ToDoList()
    
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add a Task")
        print("2. View Tasks")
        print("3. Complete a Task")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            name = input("Enter task name: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            priority = input("Enter priority (1-High, 2-Medium, 3-Low): ")
            todo_list.add_task(name, due_date, priority)
            print(f"Task '{name}' added successfully!")
        
        elif choice == "2":
            print("1. Sort by Priority")
            print("2. Sort by Due Date")
            sort_choice = input("Sort by (1-2): ")
            sort_by = "priority" if sort_choice == "1" else "due_date"
            todo_list.view_tasks(sort_by=sort_by)
        
        elif choice == "3":
            task_number = int(input("Enter task number to mark as complete: ")) - 1
            todo_list.complete_task(task_number)
        
        elif choice == "4":
            print("Exiting the To-Do List app. Goodbye!")
            break

        else:
            print("Invalid choice! Please choose a valid option.")

if __name__ == "__main__":
    main()
