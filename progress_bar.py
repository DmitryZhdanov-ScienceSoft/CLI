import time
from tqdm import tqdm
from rich.progress import Progress

# Пример функции с задержкой, которая выводит прогресс
def example_function():
    total = 100
    with tqdm(total=total, desc='Processing', unit='s') as pbar:
        for i in range(total):
            time.sleep(0.1)  # Имитация задержки выполнения
            pbar.update(1)


def display_progress():
    with Progress() as progress:
        task1 = progress.add_task("Processing...", total=100)
        while not progress.finished:
            progress.update(task1, advance=1)
            time.sleep(0.1)


if __name__ == '__main__':
    example_function()
    display_progress()
