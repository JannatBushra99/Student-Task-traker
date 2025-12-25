import json
from datetime import datetime
from typing import List, Optional

from task import Task  

class TaskManager:
    def __init__(self, filename: str = "tasks.json"):
        self.tasks: List[Task] = []   
        self.filename = filename      

    # Load tasks from JSON file

    def load_from_file(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f) 

            self.tasks = [Task.from_dict(item) for item in data]

        except FileNotFoundError:
            print(f"[INFO] {self.filename} not found.")
            self.tasks = []
        except json.JSONDecodeError:
            print(f"[ERROR] Cannot decode {self.filename}. Starting with an empty task list.")
            self.tasks = []
        except Exception as e:
            print(f"[ERROR] Unexpected error while loading tasks: {e}")
            self.tasks = []

    # Save tasks to JSON file
   
    def save_to_file(self):
        try:
            data = [task.to_dict() for task in self.tasks]
            with open(self.filename, "w") as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            print(f"[ERROR] Could not save tasks to {self.filename}: {e}")

    # Add a new task
    
    def add_task(self, title: str, description: str) -> Task:
        try:
             
            while True:
                task_id = int(input("Enter Task ID: "))
                if all(task.id != task_id for task in self.tasks):
                    break

            created_at = datetime.now()
            new_task = Task(task_id=task_id, title=title, description=description, created_at=created_at)
            self.tasks.append(new_task)
            print("[SUCCESS] Task added!")
            return new_task
        except Exception as e:
            print(f"[ERROR] Could not add task: {e}")
            raise

    # View all tasks
   
    def view_tasks(self):
        try:
            if not self.tasks:
                print("[INFO] No tasks found.")
                return

            for task in self.tasks:
                print("-----------------------------")
                print(f"ID: {task.id}")
                print(f"Title: {task.title}")
                print(f"Description: {task.description}")
                print(f"Created At: {task.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
                print("--------------------------------")
        except Exception as e:
            print(f"[ERROR] Could not view tasks: {e}")

    # Update an existing task
   
    def update_task(self, task_id: int, new_title: str, new_description: str) -> bool:
        try:
            for task in self.tasks:
                if task.id == task_id:
                    task.title = new_title
                    task.description = new_description
                    print("[SUCCESS] Task updated!")
                    return True
            print("[ERROR] Invalid ID: Task not found.")
            return False
        except Exception as e:
            print(f"[ERROR] Could not update task: {e}")
            return False

    # Delete a task by ID
   
    def delete_task(self, task_id: int) -> bool:
        try:
            for task in self.tasks:
                if task.id == task_id:
                    self.tasks.remove(task)
                    print("[SUCCESS] Task deleted!")
                    return True
            print("[ERROR] Invalid ID: Task not found.")
            return False
        except Exception as e:
            print(f"[ERROR] Could not delete task: {e}")
            return False
