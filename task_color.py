import click
import json
import os
import csv
from colorama import init, Fore, Style

init(autoreset=True)

TASKS_FILE = 'tasks.json'
FORMAT = 'json'

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r', encoding='utf-8') as file:
            if FORMAT == 'json':
                tasks = json.load(file)
            elif FORMAT == 'csv':
                reader = csv.DictReader(file)
                tasks = [row for row in reader]
            else:
                click.echo("Неподдерживаемый формат данных.")
                return []
            if all(isinstance(task, dict) and 'description' in task and 'completed' in task for task in tasks):
                return tasks
            else:
                click.echo("Ошибка формата данных. Файл будет перезаписан.")
                return []
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w', encoding='utf-8') as file:
        if FORMAT == 'json':
            json.dump(tasks, file, ensure_ascii=False, indent=4)
        elif FORMAT == 'csv':
            writer = csv.DictWriter(file, fieldnames=['description', 'completed'])
            writer.writeheader()
            writer.writerows(tasks)
        else:
            click.echo("Неподдерживаемый формат данных.")
            return

@click.group()
@click.option('--format', default='json', help="Формат файла задач: json, csv.")
def cli(format):
    """Простое приложение для управления списком дел."""
    global FORMAT
    FORMAT = format

@cli.command()
@click.argument('description')
def add(description):
    """Добавить задачу в список дел."""
    tasks = load_tasks()
    task = {
        "description": description,
        "completed": False
    }
    tasks.append(task)
    save_tasks(tasks)
    click.echo(f"Задача '{description}' добавлена.")

@cli.command()
@click.argument('task_id', type=int)
def remove(task_id):
    """Удалить задачу из списка дел по ID."""
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        removed_task = tasks.pop(task_id)
        save_tasks(tasks)
        click.echo(f"Задача '{removed_task['description']}' удалена.")
    else:
        click.echo(f"Задача с ID '{task_id}' не найдена.")

@cli.command()
def list():
    """Отобразить все задачи в списке дел."""
    tasks = load_tasks()
    if tasks:
        click.echo("Список задач:")
        for idx, task in enumerate(tasks):
            status = Fore.GREEN + "✔️" if task['completed'] else Fore.RED + "❌"
            click.echo(f"{idx}: {status} {task['description']}")
    else:
        click.echo("Список задач пуст.")

@cli.command()
@click.argument('task_id', type=int)
@click.argument('new_description')
def edit(task_id, new_description):
    """Редактировать описание задачи по ID."""
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        tasks[task_id]['description'] = new_description
        save_tasks(tasks)
        click.echo(f"Задача с ID '{task_id}' изменена на '{new_description}'.")
    else:
        click.echo(f"Задача с ID '{task_id}' не найдена.")

@cli.command()
@click.argument('task_id', type=int)
@click.option('--completed', is_flag=True, help="Пометить задачу как выполненную.")
@click.option('--uncompleted', is_flag=True, help="Пометить задачу как невыполненную.")
def mark(task_id, completed, uncompleted):
    """Пометить задачу как выполненную или невыполненную по ID."""
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        if completed:
            tasks[task_id]['completed'] = True
            click.echo(f"Задача с ID '{task_id}' помечена как выполненная.")
        elif uncompleted:
            tasks[task_id]['completed'] = False
            click.echo(f"Задача с ID '{task_id}' помечена как невыполненная.")
        save_tasks(tasks)
    else:
        click.echo(f"Задача с ID '{task_id}' не найдена.")

@cli.command()
@click.option('--completed', is_flag=True, help="Показать только выполненные задачи.")
@click.option('--uncompleted', is_flag=True, help="Показать только невыполненные задачи.")
def filter(completed, uncompleted):
    """Фильтрация задач по статусу."""
    tasks = load_tasks()
    filtered_tasks = []

    if completed:
        filtered_tasks = [task for task in tasks if task['completed']]
    elif uncompleted:
        filtered_tasks = [task for task in tasks if not task['completed']]

    if filtered_tasks:
        click.echo("Список задач:")
        for idx, task in enumerate(filtered_tasks):
            status = Fore.GREEN + "✔️" if task['completed'] else Fore.RED + "❌"
            click.echo(f"{idx}: {status} {task['description']}")
    else:
        click.echo("Нет задач, удовлетворяющих критериям фильтрации.")

@cli.command()
@click.argument('keyword')
def search(keyword):
    """Поиск задач по ключевому слову."""
    tasks = load_tasks()
    found_tasks = [(idx, task) for idx, task in enumerate(tasks) if keyword.lower() in task['description'].lower()]

    if found_tasks:
        click.echo("Найденные задачи:")
        for idx, task in found_tasks:
            status = Fore.GREEN + "✔️" if task['completed'] else Fore.RED + "❌"
            click.echo(f"{idx}: {status} {task['description']}")
    else:
        click.echo("Нет задач, содержащих данное ключевое слово.")

@cli.command()
def clear():
    """Удалить все задачи."""
    save_tasks([])
    click.echo("Все задачи удалены.")

@cli.command()
def clear_completed():
    """Удалить все выполненные задачи."""
    tasks = load_tasks()
    tasks = [task for task in tasks if not task['completed']]
    save_tasks(tasks)
    click.echo("Все выполненные задачи удалены.")

if __name__ == "__main__":
    cli()
