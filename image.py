import os

def display_image(filename):
    """Функция для отображения изображения в терминале с помощью chafa"""
    os.system(f"chafa {filename}")

# Пример использования
input_image = input("Your image name? ")
display_image(input_image)
