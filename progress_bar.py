import time
from tqdm import tqdm

# Пример функции с задержкой, которая выводит прогресс
def example_function():
    total = 100
    with tqdm(total=total, desc='Processing', unit='s') as pbar:
        for i in range(total):
            time.sleep(0.1)  # Имитация задержки выполнения
            pbar.update(1)

if __name__ == '__main__':
    example_function()
