import click
import requests
import time
import os

API_URL = "https://api.userapi.ai/midjourney/v2/imagine"
STATUS_URL = "https://api.userapi.ai/midjourney/v2/status"
API_KEY = "715faa38-3ceb-458e-b944-194babdf2d62"
ACCOUNT_HASH = "24f5ed2b-7abb-49d5-bf5c-ff259d60c42e"
WEBHOOK_URL = ""  # Укажите URL для webhook, если требуется


@click.group()
def cli():
    """CLI для взаимодействия с MidJourney API"""
    pass


@click.command()
@click.argument('prompt')
@click.option('--api-key', default=API_KEY, help='API ключ для доступа к MidJourney API')
@click.option('--account-hash', default=ACCOUNT_HASH, help='Account Hash, связанный с вашим Discord аккаунтом')
@click.option('--webhook-url', default=WEBHOOK_URL, help='URL для webhook уведомлений')
@click.option('--webhook-type', type=click.Choice(['progress', 'result']), default='result', help='Тип webhook')
def generate_image(prompt, api_key, account_hash, webhook_url, webhook_type):
    """Создание изображения по заданному запросу (prompt)"""
    headers = {
        'api-key': api_key,
        'Content-Type': 'application/json'
    }
    data = {
        "prompt": prompt,
        "webhook_url": webhook_url,
        "webhook_type": webhook_type,
        "account_hash": account_hash,
        "is_disable_prefilter": False
    }
    response = requests.post(API_URL, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        task_hash = result['hash']
        click.echo(f"Запрос на создание изображения отправлен. Хэш задачи: {task_hash}")
        click.echo("Ожидание завершения задачи...")
        time.sleep(5)  # Ожидание перед первым запросом на проверку состояния задачи
        check_image_url(task_hash, api_key)
    else:
        click.echo(f"Ошибка: {response.status_code} - {response.text}")


def check_image_url(task_hash, api_key):
    """Проверка статуса задачи и получение URL изображения по хэшу задачи"""
    headers = {
        'api-key': api_key
    }
    status_url = f"{STATUS_URL}?hash={task_hash}"
    while True:
        click.echo(f"Проверка статуса задачи: {status_url}")
        response = requests.get(status_url, headers=headers)
        click.echo(f"Ответ сервера: {response.status_code} - {response.text}")
        if response.status_code == 200:
            result = response.json()
            click.echo(f"Результат: {result}")
            if result and result['status'] == 'done' and 'result' in result and 'url' in result['result']:
                image_url = result['result']['url']
                filename = f"{task_hash}.{result['result']['filename'].split('.')[-1]}"
                click.echo(f"Изображение доступно по URL: {image_url}")
                save_image(image_url, filename)
                break
            else:
                click.echo("Задача еще не завершена, повторная проверка через 5 секунд...")
                time.sleep(5)
        else:
            click.echo(f"Ошибка: {response.status_code} - {response.text}")
            break


def save_image(url, filename):
    """Сохранение изображения по URL"""
    response = requests.get(url, stream=True)
    if response.headers['Content-Type'].startswith('image/'):
        if response.status_code == 200:
            with open(filename, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            click.echo(f"Изображение сохранено как {filename}")
        else:
            click.echo(f"Не удалось скачать изображение: {response.status_code} - {response.text}")
    else:
        click.echo("Полученные данные не являются изображением. Проверьте URL.")


cli.add_command(generate_image)

if __name__ == '__main__':
    cli()
