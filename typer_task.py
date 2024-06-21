# Description: Простой менеджер задач с использованием библиотеки Typer
import typer
import json
from typing import List

app = typer.Typer()
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

@app.command()
def add(task: str):
    """Добавить новую задачу"""
    tasks = load_tasks()
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    typer.echo(f"Задача '{task}' добавлена.")

@app.command()
def remove(task: str):
    """Удалить задачу"""
    tasks = load_tasks()
    tasks = [t for t in tasks if t["task"] != task]
    save_tasks(tasks)
    typer.echo(f"Задача '{task}' удалена.")

@app.command()
def list():
    """Отобразить список задач"""
    tasks = load_tasks()
    if tasks:
        typer.echo("Список задач:")
        for idx, task in enumerate(tasks):
            status = "✔️" if task["completed"] else "❌"
            typer.echo(f"{idx + 1}. {status} {task['task']}")
    else:
        typer.echo("Список задач пуст.")

@app.command()
def complete(task: str):
    """Отметить задачу как выполненную"""
    tasks = load_tasks()
    for t in tasks:
        if t["task"] == task:
            t["completed"] = True
            save_tasks(tasks)
            typer.echo(f"Задача '{task}' отмечена как выполненная.")
            return
    typer.echo(f"Задача '{task}' не найдена.")

if __name__ == "__main__":
    app()
