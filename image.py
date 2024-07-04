import os
import glob

def find_latest_png():
    """Функция для поиска последнего созданного .png файла в текущей папке"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    current_dir += '/images/'
    png_files = glob.glob(os.path.join(current_dir, '*.png'))
    if not png_files:
        return None
    return max(png_files, key=os.path.getctime)

def display_image(filename):
    """Функция для отображения изображения в терминале с помощью chafa"""
    if filename:
        os.system(f"chafa {filename}")
    else:
        print("Изображение не найдено.")


# Находим последнюю созданную картинку .png
latest_image = find_latest_png()

# Отображаем найденную картинку
display_image(latest_image)
