import json

# Task class definition
class Task:
    def __init__(self, id, title, completed=False):
        self.id = id
        self.title = title
        self.completed = completed

    def __repr__(self):
        status = '✓' if self.completed else '✗'
        return f"{self.id}. {self.title} - {status}"

# Function to add a task
def add_task(task_list, title):
    task_id = len(task_list) + 1
    task = Task(task_id, title)
    task_list.append(task)
    print(f"Task '{title}' added successfully!")

# Function to view all tasks
def view_tasks(task_list):
    if not task_list:
        print("No tasks available.")
    else:
        for task in task_list:
            print(task)

# Function to delete a task
def delete_task(task_list, task_id):
    task_list[:] = [task for task in task_list if task.id != task_id]
    print(f"Task {task_id} deleted successfully!")

# Function to mark a task as complete
def complete_task(task_list, task_id):
    for task in task_list:
        if task.id == task_id:
            task.completed = True
            print(f"Task {task_id} marked as completed!")

# Function to save tasks to a file
def save_tasks(task_list, filename='tasks.json'):
    with open(filename, 'w') as file:
        json.dump([task.__dict__ for task in task_list], file)
    print("Tasks saved to file.")

# Function to load tasks from a file
def load_tasks(filename='tasks.json'):
    try:
        with open(filename, 'r') as file:
            tasks_data = json.load(file)
            return [Task(**data) for data in tasks_data]
    except FileNotFoundError:
        return []

# Function for user login (optional for testing purposes)
def login():
    dummy_email = "testuser@example.com"
    dummy_password = "password123"

    email = input("Enter Email ID: ")
    password = input("Enter Password: ")

    if email == dummy_email and password == dummy_password:
        print("Login successful!")
        return True
    else:
        print("Invalid credentials, please try again.")
        return False

# Main CLI loop for task management
def main():
    task_list = load_tasks()

    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Complete")
        print("5. Save and Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter task title: ")
            add_task(task_list, title)
        elif choice == '2':
            view_tasks(task_list)
        elif choice == '3':
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_list, task_id)
        elif choice == '4':
            task_id = int(input("Enter task ID to mark as complete: "))
            complete_task(task_list, task_id)
        elif choice == '5':
            save_tasks(task_list)
            print("Exiting the application...")
            break
        else:
            print("Invalid option. Please choose again.")

# Start the application
if __name__ == "__main__":
    if login():  # Optional: if you want to include login functionality
        main()
    else:
        print("Exiting application.")
