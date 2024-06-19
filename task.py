import click
import json
import os

TASKS_FILE = 'tasks.json'


def load_tasks():
    print("Загрузка задач...")
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r', encoding='utf-8') as file:
            tasks = json.load(file)
            # Проверка формата данных
            if all(isinstance(task, dict) and 'description' in task and 'completed' in task for task in tasks):
                print("Задачи загружены:", tasks)
                return tasks
            else:
                print("Ошибка формата данных в файле tasks.json. Файл будет перезаписан.")
                return []
    print("Файл задач не найден. Возвращаем пустой список.")
    return []


def save_tasks(tasks):
    print("Сохранение задач...")
    with open(TASKS_FILE, 'w', encoding='utf-8') as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)
    print("Задачи сохранены:", tasks)


@click.group()
def cli():
    """Простое приложение для управления списком дел."""
    print("Инициализация CLI...")


@cli.command()
@click.argument('description')
def add(description):
    """Добавить задачу в список дел."""
    print("Добавление задачи:", description)
    tasks = load_tasks()
    task = {
        "description": description,
        "completed": False
    }
    tasks.append(task)
    save_tasks(tasks)
    click.echo(f"Задача '{description}' добавлена.")


@cli.command()
@click.argument('description')
def remove(description):
    """Удалить задачу из списка дел."""
    print("Удаление задачи:", description)
    tasks = load_tasks()
    for task in tasks:
        if task['description'] == description:
            tasks.remove(task)
            save_tasks(tasks)
            click.echo(f"Задача '{description}' удалена.")
            return
    click.echo(f"Задача '{description}' не найдена.")


@cli.command()
def list():
    """Отобразить все задачи в списке дел."""
    print("Отображение списка задач...")
    tasks = load_tasks()
    if tasks:
        click.echo("Список задач:")
        for task in tasks:
            status = "✔️" if task['completed'] else "❌"
            click.echo(f"{status} {task['description']}")
    else:
        click.echo("Список задач пуст.")


@cli.command()
@click.argument('description')
@click.argument('new_description')
def edit(description, new_description):
    """Редактировать описание задачи."""
    print("Редактирование задачи:", description, "на", new_description)
    tasks = load_tasks()
    for task in tasks:
        if task['description'] == description:
            task['description'] = new_description
            save_tasks(tasks)
            click.echo(f"Задача '{description}' изменена на '{new_description}'.")
            return
    click.echo(f"Задача '{description}' не найдена.")


@cli.command()
@click.argument('description')
@click.option('--completed', is_flag=True, help="Пометить задачу как выполненную.")
@click.option('--uncompleted', is_flag=True, help="Пометить задачу как невыполненную.")
def mark(description, completed, uncompleted):
    """Пометить задачу как выполненную или невыполненную."""
    print("Изменение статуса задачи:", description)
    tasks = load_tasks()
    for task in tasks:
        if task['description'] == description:
            if completed:
                task['completed'] = True
                click.echo(f"Задача '{description}' помечена как выполненная.")
            elif uncompleted:
                task['completed'] = False
                click.echo(f"Задача '{description}' помечена как невыполненная.")
            save_tasks(tasks)
            return
    click.echo(f"Задача '{description}' не найдена.")


@cli.command()
@click.option('--completed', is_flag=True, help="Показать только выполненные задачи.")
@click.option('--uncompleted', is_flag=True, help="Показать только невыполненные задачи.")
def filter(completed, uncompleted):
    """Фильтрация задач по статусу."""
    print("Фильтрация задач...")
    tasks = load_tasks()
    filtered_tasks = []

    if completed:
        filtered_tasks = [task for task in tasks if task['completed']]
    elif uncompleted:
        filtered_tasks = [task for task in tasks if not task['completed']]

    if filtered_tasks:
        click.echo("Список задач:")
        for task in filtered_tasks:
            status = "✔️" if task['completed'] else "❌"
            click.echo(f"{status} {task['description']}")
    else:
        click.echo("Нет задач, удовлетворяющих критериям фильтрации.")


if __name__ == "__main__":
    cli()
