from asciimatics.widgets import Frame, ListBox, Layout, Label, Divider, Button, Text
from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.exceptions import StopApplication
import subprocess
import sys

class MenuFrame(Frame):
    def __init__(self, screen):
        super(MenuFrame, self).__init__(screen, screen.height, screen.width, has_border=True, can_scroll=False, title="Main Menu")
        layout = Layout([1], fill_frame=True)
        self.add_layout(layout)
        layout.add_widget(Divider())
        layout.add_widget(Label("Select an option:"))
        layout.add_widget(Divider())

        layout.add_widget(Button("1. Task Manager (argparse)", self.run_task_argp))
        layout.add_widget(Button("2. Task Manager (Typer)", self.run_typer_task))
        layout.add_widget(Button("3. Task Manager (Color)", self.run_task_color))
        layout.add_widget(Button("4. Task Manager (Format)", self.run_task_format))
        layout.add_widget(Button("5. Task Manager (Pending)", self.run_task_pending))
        layout.add_widget(Button("6. Basic Task Manager", self.run_task))
        layout.add_widget(Button("7. Text Editor", self.run_text_editor))
        layout.add_widget(Divider())
        layout.add_widget(Button("Quit", self.quit))

        self.fix()

    def run_task_argp(self):
        self._run_subprocess('task_argp.py')

    def run_typer_task(self):
        self._run_subprocess('typer_task.py')

    def run_task_color(self):
        self._run_subprocess('task_color.py')

    def run_task_format(self):
        self._run_subprocess('task_format.py')

    def run_task_pending(self):
        self._run_subprocess('task_pending.py')

    def run_task(self):
        self._run_subprocess('task.py')

    def run_text_editor(self):
        self._run_subprocess('editor.py')

    def _run_subprocess(self, script_name):
        subprocess.run([sys.executable, script_name])

    def quit(self):
        raise StopApplication("User pressed quit")

def demo(screen):
    scenes = [
        Scene([MenuFrame(screen)], -1, name="Main Menu")
    ]
    screen.play(scenes, stop_on_resize=True)

if __name__ == "__main__":
    Screen.wrapper(demo)
