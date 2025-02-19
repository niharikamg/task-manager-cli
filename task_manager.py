import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print(f"Task added: {task}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found!")
    else:
        for idx, task in enumerate(tasks, start=1):
            status = "[✔]" if task["done"] else "[ ]"
            print(f"{idx}. {status} {task['task']}")

if __name__ == "__main__":
    while True:
        print("\nTask Manager CLI")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter task description: ")
            add_task(task)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again!")
import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print(f"Task added: {task}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found!")
    else:
        for idx, task in enumerate(tasks, start=1):
            status = "[✔]" if task["done"] else "[ ]"
            print(f"{idx}. {status} {task['task']}")

if __name__ == "__main__":
    while True:
        print("\nTask Manager CLI")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter task description: ")
            add_task(task)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again!")
