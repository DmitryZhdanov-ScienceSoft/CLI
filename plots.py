import click
import numpy as np
from rich.console import Console
from rich.table import Table

console = Console()

@click.group()
def cli():
    """Простое CLI-приложение для работы с графиками."""
    pass

@cli.command()
def show_histogram():
    """Показать гистограмму случайных данных."""
    data = np.random.randn(1000)
    counts, bin_edges = np.histogram(data, bins=10)
    table = Table(title="Гистограмма случайных данных")

    table.add_column("Бин", justify="right", style="cyan", no_wrap=True)
    table.add_column("Частота", justify="right", style="magenta")

    for count, edge in zip(counts, bin_edges[:-1]):
        table.add_row(f"{edge:.2f}", str(count))

    console.print(table)

@cli.command()
def show_plot():
    """Показать линейный график."""
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    console.rule("Линейный график")
    for xi, yi in zip(x, y):
        console.print(f"{xi:.2f}: {'█' * int((yi + 1) * 10)}", style="green")

if __name__ == "__main__":
    cli()
