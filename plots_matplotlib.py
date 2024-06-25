import click
import matplotlib.pyplot as plt
import numpy as np

@click.group()
def cli():
    """Простое CLI-приложение для работы с графиками."""
    pass

@cli.command()
def show_histogram():
    """Показать гистограмму случайных данных."""
    data = np.random.randn(1000)
    plt.hist(data, bins=30, color='blue', alpha=0.7)
    plt.title('Гистограмма случайных данных')
    plt.xlabel('Значение')
    plt.ylabel('Частота')
    plt.grid(True)
    plt.show()

@cli.command()
def show_plot():
    """Показать линейный график."""
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    plt.plot(x, y, color='green', linestyle='-', linewidth=2, marker='o', markerfacecolor='red')
    plt.title('Линейный график')
    plt.xlabel('X')
    plt.ylabel('sin(X)')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    cli()
