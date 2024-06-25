import click
import requests

API_URL = 'http://127.0.0.1:5000/todos'

@click.group()
def cli():
    """Простое CLI-приложение для взаимодействия с API."""
    pass

@cli.command()
def fetch_tasks():
    """Получить список задач из внешнего API."""
    response = requests.get(API_URL)
    if response.status_code == 200:
        tasks = response.json()
        for task in tasks:
            status = "✔️" if task['completed'] else "❌"
            click.echo(f"{task['id']}: {status} {task['title']}")
    else:
        click.echo(f"Ошибка при получении данных: {response.status_code}")

@cli.command()
@click.argument('title')
def create_task(title):
    """Создать новую задачу в API."""
    # Сначала получим текущие задачи, чтобы определить следующий ID
    response = requests.get(API_URL)
    print(response)
    if response.status_code == 200:
        tasks = response.json()
        new_id = max([task['id'] for task in tasks]) + 1 if tasks else 1
        new_task = {"id": new_id, "title": title, "completed": False}
        create_response = requests.post(API_URL, json=new_task)
        if create_response.status_code == 201:
            click.echo(f"Задача '{title}' создана.")
        else:
            click.echo(f"Ошибка при создании задачи: {create_response.status_code}")
    else:
        click.echo(f"Ошибка при получении данных: {response.status_code}")

if __name__ == "__main__":
    cli()
