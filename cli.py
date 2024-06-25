import typer
import subprocess
import sys

# Основное приложение Typer
app = typer.Typer()

# Импорт приложений Typer и добавление их в основное приложение
from typer_task import app as typer_task_app
app.add_typer(typer_task_app, name="typer_task")

# Определение функций для запуска скриптов с аргументами
@app.command(name="task_argp")
def task_argp(args: list[str] = typer.Argument(None)):
    """Run argparse-based task manager."""
    subprocess.run([sys.executable, 'task_argp.py'] + args)

@app.command(name="task_color")
def task_color(args: list[str] = typer.Argument(None)):
    """Run color-based task manager."""
    subprocess.run([sys.executable, 'task_color.py'] + args)

@app.command(name="task_format")
def task_format(args: list[str] = typer.Argument(None)):
    """Run format-based task manager."""
    subprocess.run([sys.executable, 'task_format.py'] + args)

@app.command(name="task_pending")
def task_pending(args: list[str] = typer.Argument(None)):
    """Run pending-based task manager."""
    subprocess.run([sys.executable, 'task_pending.py'] + args)

@app.command(name="task")
def task(args: list[str] = typer.Argument(None)):
    """Run basic task manager."""
    subprocess.run([sys.executable, 'task.py'] + args)

@app.command(name="text_editor")
def text_editor():
    """Run the text editor using urwid."""
    subprocess.run([sys.executable, 'editor.py'])

if __name__ == "__main__":
    app()
    