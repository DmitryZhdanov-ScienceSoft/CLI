import click
import requests
import os
import sys
import time
from dotenv import load_dotenv
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn

# Загрузка переменных окружения из файла .env
load_dotenv()

OPENAI_API_KEY = os.getenv('API_KEY')


def query_gpt4o(prompt):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {OPENAI_API_KEY}',
    }
    data = {
        'model': 'gpt-4',
        'messages': [{'role': 'user', 'content': prompt}],
        'max_tokens': 50,
    }

    # Примерное время ожидания ответа от сервера (можно настроить по своему усмотрению)
    estimated_time = 5  # seconds

    # Инициализация прогресс-бара с использованием Rich
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
    ) as progress:
        task = progress.add_task("Processing...", total=estimated_time)

        response = requests.post(url, headers=headers, json=data)
        for _ in range(estimated_time):
            time.sleep(1)
            progress.update(task, advance=1)

    response_data = response.json()
    if 'error' in response_data:
        raise ValueError(f"Ошибка при запросе к OpenAI: {response_data['error']['message']}")
    return response_data['choices'][0]['message']['content']


@click.group()
def cli():
    pass

@cli.command()
@click.argument('name')
@click.option('--greeting', default='Hello', help='Greeting to use')
def greet(name, greeting):
    click.echo(f"{greeting}, {name}!")

@cli.command()
@click.argument('a', type=int)
@click.argument('b', type=int)
def add(a, b):
    result = a + b
    click.echo(f"The sum of {a} and {b} is {result}")

@cli.command()
@click.argument('a', type=int)
@click.argument('b', type=int)
def multiply(a, b):
    result = a * b
    click.echo(f"The product of {a} and {b} is {result}")

@cli.command()
@click.argument('filename')
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            click.echo(contents)
    except FileNotFoundError:
        click.echo(f"Error: File '{filename}' not found or cannot be opened.")
    except Exception as e:
        click.echo(f"Error: An unexpected error occurred: {str(e)}")

@cli.command()
@click.option('--uppercase', '-u', is_flag=True, help='Convert text to uppercase.')
@click.argument('text')
def manipulate_text(text, uppercase):
    if uppercase:
        result = text.upper()
    else:
        result = text.lower()
    click.echo(result)

@cli.command()
@click.argument('prompt')
def query(prompt):
    try:
        generated_text = query_gpt4o(prompt)
        click.echo("Сгенерированный текст:")
        click.echo(generated_text)
    except ValueError as e:
        click.echo(e)
    except Exception as e:
        click.echo(f"Произошла неизвестная ошибка: {e}")

if __name__ == '__main__':
    cli()
