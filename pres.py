from pptx import Presentation
from pptx.util import Inches

# Создаем презентацию
prs = Presentation()

# Заголовочный слайд
slide_title = prs.slides.add_slide(prs.slide_layouts[0])
title = slide_title.shapes.title
subtitle = slide_title.placeholders[1]

title.text = "Исследование CLI-приложений на Python"
subtitle.text = "Создание и взаимодействие CLI-приложений"

# Слайд с основными библиотеками
slide = prs.slides.add_slide(prs.slide_layouts[1])
title, content = slide.shapes.title, slide.placeholders[1].text_frame
title.text = "Основные библиотеки для создания CLI-приложений"

content.text = "argparse, click, typer"
content.add_paragraph("argparse: Встроенная библиотека Python для обработки аргументов командной строки")
content.add_paragraph("click: Высокоуровневая библиотека для создания CLI-приложений")
content.add_paragraph("typer: Современная библиотека для создания CLI-приложений с использованием аннотаций типов")

# Слайд с примером использования argparse
slide = prs.slides.add_slide(prs.slide_layouts[1])
title, content = slide.shapes.title, slide.placeholders[1].text_frame
title.text = "Пример использования argparse"
content.text = """import argparse

def main():
    parser = argparse.ArgumentParser(description="Пример CLI-приложения.")
    parser.add_argument("name", type=str, help="Имя пользователя")
    parser.add_argument("--greet", action="store_true", help="Включить приветствие")
    args = parser.parse_args()
    if args.greet:
        print(f"Привет, {args.name}!")
    else:
        print(f"Привет, {args.name}.")

if __name__ == "__main__":
    main()"""

# Слайд с примером использования click
slide = prs.slides.add_slide(prs.slide_layouts[1])
title, content = slide.shapes.title, slide.placeholders[1].text_frame
title.text = "Пример использования click"
content.text = """import click

@click.command()
@click.argument('name')
@click.option('--greet', is_flag=True, help="Включить приветствие")
def main(name, greet):
    if greet:
        click.echo(f"Привет, {name}!")
    else:
        click.echo(f"Привет, {name}.")

if __name__ == "__main__":
    main()"""

# Слайд с примером использования typer
slide = prs.slides.add_slide(prs.slide_layouts[1])
title, content = slide.shapes.title, slide.placeholders[1].text_frame
title.text = "Пример использования typer"
content.text = """import typer

def main(name: str, greet: bool = False):
    if greet:
        typer.echo(f"Привет, {name}!")
    else:
        typer.echo(f"Привет, {name}.")

if __name__ == "__main__":
    typer.run(main)"""

# Слайд с взаимодействием через API
slide = prs.slides.add_slide(prs.slide_layouts[1])
title, content = slide.shapes.title, slide.placeholders[1].text_frame
title.text = "Взаимодействие через API"
content.text = """import click
import requests

API_URL = 'https://jsonplaceholder.typicode.com/todos'

@click.group()
def cli():
    pass

@cli.command()
def fetch_tasks():
    response = requests.get(API_URL)
    if response.status_code == 200:
        tasks = response.json()
        for task in tasks:
            status = "✔️" if task['completed'] else "❌"
            click.echo(f"{task['id']}: {status} {task['title']}")
    else:
        click.echo(f"Ошибка при получении данных: {response.status_code}")

if __name__ == "__main__":
    cli()"""

# Слайд с взаимодействием с базой данных
slide = prs.slides.add_slide(prs.slide_layouts[1])
title, content = slide.shapes.title, slide.placeholders[1].text_frame
title.text = "Взаимодействие с базой данных"
content.text = """import click
import sqlite3

DATABASE = 'tasks.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@click.group()
def cli():
    pass

@cli.command()
def init_db():
    conn = get_db_connection()
    conn.execute('''CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, title TEXT, completed BOOLEAN)''')
    conn.commit()
    conn.close()
    click.echo("База данных инициализирована")

@cli.command()
@click.argument('title')
def add_task(title):
    conn = get_db_connection()
    conn.execute('INSERT INTO tasks (title, completed) VALUES (?, ?)', (title, False))
    conn.commit()
    conn.close()
    click.echo(f"Задача '{title}' добавлена")

@cli.command()
def list_tasks():
    conn = get_db_connection()
    tasks = conn.execute('SELECT id, title, completed FROM tasks').fetchall()
    conn.close()
    for task in tasks:
        status = "✔️" if task['completed'] else "❌"
        click.echo(f"{task['id']}: {status} {task['title']}")

if __name__ == "__main__":
    cli()"""

# Слайд с взаимодействием через очереди сообщений
slide = prs.slides.add_slide(prs.slide_layouts[1])
title, content = slide.shapes.title, slide.placeholders[1].text_frame
title.text = "Взаимодействие через MQ (Message Queues)"
content.text = """import click
import pika

@click.group()
def cli():
    pass

@cli.command()
@click.argument('message')
def send_message(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='task_queue')
    channel.basic_publish(exchange='', routing_key='task_queue', body=message)
    connection.close()
    click.echo(f"Сообщение '{message}' отправлено в очередь")

@cli.command()
def receive_message():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='task_queue')

    def callback(ch, method, properties, body):
        click.echo(f"Получено сообщение: {body.decode()}")

    channel.basic_consume(queue='task_queue', on_message_callback=callback, auto_ack=True)
    click.echo("Ожидание сообщений. Нажмите CTRL+C для выхода.")
    channel.start_consuming()

if __name__ == "__main__":
    cli()"""

# Слайд с взаимодействием с облачными сервисами
slide = prs.slides.add_slide(prs.slide_layouts[1])
title, content = slide.shapes.title, slide.placeholders[1].text_frame
title.text = "Взаимодействие с облачными сервисами"
content.text = """import click
import boto3

s3 = boto3.client('s3')

@click.group()
def cli():
    pass

@cli.command()
@click.argument('bucket_name')
def list_objects(bucket_name):
    response = s3.list_objects_v2(Bucket=bucket_name)
    for obj in response.get('Contents', []):
        click.echo(obj['Key'])

@cli.command()
@click.argument('bucket_name')
@click.argument('file_name')
@click.argument('object_name')
def upload_file(bucket_name, file_name, object_name):
    s3.upload_file(file_name, bucket_name, object_name)
    click.echo(f"Файл '{file_name}' загружен как '{object_name}' в бакет '{bucket_name}'")

if __name__ == "__main__":
    cli()"""

# Сохранение презентации
prs.save("/mnt/data/CLI_Applications_Research.pptx")
