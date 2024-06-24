import click
import termplotlib as tpl
import numpy as np

@click.group()
def cli():
    """Простое CLI-приложение для работы с графиками."""
    pass

@cli.command()
def show_histogram():
    """Показать гистограмму случайных данных."""
    data = np.random.randn(1000)
    counts, bin_edges = np.histogram(data, bins=30)
    fig = tpl.figure()
    fig.hist(counts, bin_edges, force_ascii=False)
    fig.show()

@cli.command()
def show_plot():
    """Показать линейный график."""
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    fig = tpl.figure()
    fig.plot(x, y, width=60, height=20)
    fig.show()

if __name__ == "__main__":
    cli()
