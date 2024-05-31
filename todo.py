import os
import json

class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

    def to_dict(self):
        return {"description": self.description, "completed": self.completed}

    @classmethod
    def from_dict(cls, task_dict):
        return cls(task_dict['description'], task_dict['completed'])

class ToDoList:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        self.save_tasks()

    def view_tasks(self):
        for index, task in enumerate(self.tasks, start=1):
            status = "Done" if task.completed else "Not Done"
            print(f"{index}. {task.description} [{status}]")

    def update_task(self, index, description=None, completed=None):
        if 0 <= index < len(self.tasks):
            if description is not None:
                self.tasks[index].description = description
            if completed is not None:
                self.tasks[index].completed = completed
            self.save_tasks()
        else:
            print("Invalid task index")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks()
        else:
            print("Invalid task index")

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                tasks = json.load(file)
                return [Task.from_dict(task) for task in tasks]
        return []

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            index = int(input("Enter task number to update: ")) - 1
            description = input("Enter new description (leave blank to keep current): ")
            completed_str = input("Is the task completed? (yes/no/leave blank to keep current): ")
            completed = None
            if completed_str.lower() == 'yes':
                completed = True
            elif completed_str.lower() == 'no':
                completed = False
            todo_list.update_task(index, description if description else None, completed)
        elif choice == '4':
            index = int(input("Enter task number to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
