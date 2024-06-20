import time

from rich.console import Console
from rich.table import Table
from rich.progress import Progress

console = Console()

def display_table():
    table = Table(title="User Information")
    table.add_column("Name", style="cyan", no_wrap=True)
    table.add_column("Age", style="magenta")
    table.add_row("John Doe", "36")
    table.add_row("Jane Doe", "34")
    console.print(table)

def display_progress():
    with Progress() as progress:
        task1 = progress.add_task("Processing...", total=100)
        while not progress.finished:
            progress.update(task1, advance=1)
            time.sleep(0.1)

def main():
    console.print("Welcome to Rich CLI!", style="bold green")
    display_table()
    display_progress()

if __name__ == '__main__':
    main()
