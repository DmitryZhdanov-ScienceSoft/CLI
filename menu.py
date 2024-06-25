from textual.app import App
from textual.widgets import Static, Button
from textual.message import Message

class ButtonPressed(Message):
    def __init__(self, sender, button_name):
        super().__init__(sender)
        self.button_name = button_name

class CLIMenu(App):
    async def on_mount(self):
        # Создаем список CLI-приложений
        await self.view.dock(Static("Выберите CLI-приложение для запуска:"), edge="top")
        await self.view.dock(Button("CLI App 1", name="cli_app_1"), edge="top")
        await self.view.dock(Button("CLI App 2", name="cli_app_2"), edge="top")
        await self.view.dock(Button("CLI App 3", name="cli_app_3"), edge="top")

    async def on_button_pressed(self, message: Button.Pressed):
        button_name = message.button.name
        await self.message(ButtonPressed(self, button_name))

    async def handle_button_pressed(self, message: ButtonPressed):
        button_name = message.button_name
        if button_name == "cli_app_1":
            self.run_cli_app_1()
        elif button_name == "cli_app_2":
            self.run_cli_app_2()
        elif button_name == "cli_app_3":
            self.run_cli_app_3()

    def run_cli_app_1(self):
        # Код для запуска первого CLI-приложения
        print("Запуск CLI App 1")

    def run_cli_app_2(self):
        # Код для запуска второго CLI-приложения
        print("Запуск CLI App 2")

    def run_cli_app_3(self):
        # Код для запуска третьего CLI-приложения
        print("Запуск CLI App 3")

if __name__ == "__main__":
    CLIMenu.run()
