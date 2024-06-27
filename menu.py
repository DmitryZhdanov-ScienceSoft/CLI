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
        title = Static("Выберите CLI-приложение для запуска:")
        self.button1 = Button("CLI App 1", name="cli_app_1")
        self.button2 = Button("CLI App 2", name="cli_app_2")
        self.button3 = Button("CLI App 3", name="cli_app_3")

        # Добавляем виджеты на экран
        await self.mount(title)
        await self.mount(self.button1)
        await self.mount(self.button2)
        await self.mount(self.button3)

        # Устанавливаем фокус на первую кнопку
        self.set_focus(self.button1)

    async def on_button_pressed(self, message: Button.Pressed):
        button_name = message.button.name
        await self.handle_button_pressed(button_name)

    async def handle_button_pressed(self, button_name):
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
