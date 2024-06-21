# Description: Программа для управления задачами с использованием argparse
import argparse
import json

TASKS_FILE = 'tasks.json'

def load_tasks():
    try:
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

tasks = load_tasks()

def add_task(task):
    """Добавить новую задачу"""
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    print(f"Задача '{task}' добавлена.")

def remove_task(task):
    """Удалить задачу"""
    global tasks
    tasks = [t for t in tasks if t["task"] != task]
    save_tasks(tasks)
    print(f"Задача '{task}' удалена.")

def list_tasks():
    """Отобразить список задач"""
    if tasks:
        print("Список задач:")
        for idx, task in enumerate(tasks):
            status = "✔️" if task["completed"] else "❌"
            print(f"{idx + 1}. {status} {task['task']}")
    else:
        print("Список задач пуст.")

def complete_task(task):
    """Отметить задачу как выполненную"""
    for t in tasks:
        if t["task"] == task:
            t["completed"] = True
            save_tasks(tasks)
            print(f"Задача '{task}' отмечена как выполненная.")
            return
    print(f"Задача '{task}' не найдена.")

parser = argparse.ArgumentParser(description="Task Manager CLI")
subparsers = parser.add_subparsers(dest="command")

add_parser = subparsers.add_parser("add", help="Добавить новую задачу")
add_parser.add_argument("task", type=str, help="Описание задачи")

remove_parser = subparsers.add_parser("remove", help="Удалить задачу")
remove_parser.add_argument("task", type=str, help="Описание задачи")

list_parser = subparsers.add_parser("list", help="Отобразить список задач")

complete_parser = subparsers.add_parser("complete", help="Отметить задачу как выполненную")
complete_parser.add_argument("task", type=str, help="Описание задачи")

args = parser.parse_args()

if args.command == "add":
    add_task(args.task)
elif args.command == "remove":
    remove_task(args.task)
elif args.command == "list":
    list_tasks()
elif args.command == "complete":
    complete_task(args.task)
