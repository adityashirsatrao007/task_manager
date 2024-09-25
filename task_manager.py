import json
import os

class TaskManager:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, title, description):
        task = {"id": len(self.tasks) + 1, "title": title, "description": description}
        self.tasks.append(task)
        self.save_tasks()
        print(f'Task "{title}" added.')

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        for task in self.tasks:
            print(f'ID: {task["id"]}, Title: {task["title"]}, Description: {task["description"]}')

    def update_task(self, task_id, title, description):
        for task in self.tasks:
            if task['id'] == task_id:
                task['title'] = title
                task['description'] = description
                self.save_tasks()
                print(f'Task "{task_id}" updated.')
                return
        print(f'Task with ID {task_id} not found.')

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task['id'] != task_id]
        self.save_tasks()
        print(f'Task "{task_id}" deleted.')

def main():
    manager = TaskManager()
    while True:
        command = input("Enter a command (add/list/update/delete/exit): ").strip().lower()
        if command == 'add':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            manager.add_task(title, description)
        elif command == 'list':
            manager.list_tasks()
        elif command == 'update':
            task_id = int(input("Enter task ID to update: "))
            title = input("Enter new task title: ")
            description = input("Enter new task description: ")
            manager.update_task(task_id, title, description)
        elif command == 'delete':
            task_id = int(input("Enter task ID to delete: "))
            manager.delete_task(task_id)
        elif command == 'exit':
            print("Exiting the Task Manager.")
            break
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()
