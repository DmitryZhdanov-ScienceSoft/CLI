import click
import requests

API_URL = 'https://jsonplaceholder.typicode.com/todos'

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

if __name__ == "__main__":
    cli()
