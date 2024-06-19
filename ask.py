import requests
import os
import sys
from dotenv import load_dotenv

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
    response = requests.post(url, headers=headers, json=data)
    response_data = response.json()
    if 'error' in response_data:
        raise ValueError(f"Ошибка при запросе к OpenAI: {response_data['error']['message']}")
    return response_data['choices'][0]['message']['content']

if __name__ == '__main__':
    try:
        # Используем sys.stdin для получения ввода
        prompt = input("Введите текст для генерации: ")
    except UnicodeDecodeError:
        print("Ошибка декодирования Unicode. Убедитесь, что вводите текст на русском языке в UTF-8.")
        sys.exit(1)

    try:
        generated_text = query_gpt4o(prompt)
        print("Сгенерированный текст:")
        print(generated_text)
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"Произошла неизвестная ошибка: {e}")
