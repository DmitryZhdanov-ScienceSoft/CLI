import os
import sys
import subprocess
from textual.app import App
from textual.widgets import Static, Button
from textual.message import Message


class ButtonPressed(Message):
    def __init__(self, sender, button_name):
        super().__init__(sender)
        self.button_name = button_name


class CLIMenu(App):
    async def on_mount(self):
        title = Static("Выберите CLI-приложение для запуска:")
        self.button1 = Button("menu.py", name="menu_py")
        self.button2 = Button("CLI App 2", name="cli_app_2")
        self.button3 = Button("CLI App 3", name="cli_app_3")

        await self.mount(title)
        await self.mount(self.button1)
        await self.mount(self.button2)
        await self.mount(self.button3)

        self.set_focus(self.button1)

    async def on_button_pressed(self, message: Button.Pressed):
        button_name = message.button.name
        await self.handle_button_pressed(button_name)

    async def handle_button_pressed(self, button_name):
        if button_name == "menu_py":
            self.run_menu_py()
        elif button_name == "cli_app_2":
            self.run_cli_app_2()
        elif button_name == "cli_app_3":
            self.run_cli_app_3()

    def run_menu_py(self):
        self.exit()  # Закрываем текущее приложение
        script_dir = os.path.dirname(os.path.abspath(__file__))
        menu_path = os.path.join(script_dir, 'menu.py')

        # Используем os.execv для полной передачи управления menu.py
        os.execv(sys.executable, ['python', menu_path])

    def run_cli_app_2(self):
        print("Запуск CLI App 2")

    def run_cli_app_3(self):
        print("Запуск CLI App 3")

    async def on_key(self, event):
        if event.key == "down":
            self.focus_next_widget()
        elif event.key == "up":
            self.focus_previous_widget()
        elif event.key == "enter":
            focused_widget = self.focused
            if isinstance(focused_widget, Button):
                await self.handle_button_pressed(focused_widget.name)

    def focus_next_widget(self):
        focused = self.focused
        if focused == self.button1:
            self.set_focus(self.button2)
        elif focused == self.button2:
            self.set_focus(self.button3)
        elif focused == self.button3:
            self.set_focus(self.button1)

    def focus_previous_widget(self):
        focused = self.focused
        if focused == self.button1:
            self.set_focus(self.button3)
        elif focused == self.button2:
            self.set_focus(self.button1)
        elif focused == self.button3:
            self.set_focus(self.button2)


if __name__ == "__main__":
    app = CLIMenu()
    app.run()
