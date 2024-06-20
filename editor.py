from asciimatics.widgets import Frame, Layout, Divider, TextBox, Button, Widget, PopUpDialog, FileBrowser
from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.exceptions import StopApplication, NextScene, ResizeScreenError
from asciimatics.event import KeyboardEvent
import os
import sys


class TextEditor(Frame):
    def __init__(self, screen):
        super(TextEditor, self).__init__(screen, screen.height, screen.width, has_border=True, name="My Text Editor")

        # Создаем основной макет с текстовым полем
        layout = Layout([100], fill_frame=True)
        self.add_layout(layout)
        self.text_box = TextBox(screen.height - 6, as_string=True, line_wrap=True)
        layout.add_widget(self.text_box)
        layout.add_widget(Divider())

        # Создаем макет для кнопок
        button_layout = Layout([1, 1, 1, 1, 1])
        self.add_layout(button_layout)
        button_layout.add_widget(Button("Open", self._open), 0)
        button_layout.add_widget(Button("Save", self._save), 1)
        button_layout.add_widget(Button("Find", self._find), 2)
        button_layout.add_widget(Button("Replace", self._replace), 3)
        button_layout.add_widget(Button("Quit", self._quit), 4)
        self.fix()

    def _open(self):
        # Показать диалоговое окно для выбора файла
        self._scene.add_effect(FileBrowserDialog(self._screen, self._load_file))

    def _load_file(self, filename):
        # Открыть выбранный файл и загрузить его содержимое
        if filename:
            try:
                with open(filename, "r") as f:
                    self.text_box.value = f.read()
            except FileNotFoundError:
                self._show_message("File not found!", "Error")
            except Exception as e:
                self._show_message(f"An error occurred: {str(e)}", "Error")

    def _save(self):
        with open("output.txt", "w") as f:
            f.write(self.text_box.value)
        raise NextScene("Main")

    def _find(self):
        # Показываем окно поиска
        self._show_message("Find functionality not implemented yet!", "Info")

    def _replace(self):
        # Показываем окно замены
        self._show_message("Replace functionality not implemented yet!", "Info")

    def _quit(self):
        raise StopApplication("User pressed quit")

    def _show_message(self, message, title):
        self._scene.add_effect(
            PopUpDialog(self._screen, message, [("OK", None)], title=title)
        )


class FileBrowserDialog(Frame):
    def __init__(self, screen, callback):
        super(FileBrowserDialog, self).__init__(screen, screen.height * 2 // 3, screen.width * 2 // 3,
                                                has_border=True, can_scroll=True, title="Select a file")
        self._callback = callback

        # Create a FileBrowser widget and add it to the Frame
        layout = Layout([100], fill_frame=True)
        self.add_layout(layout)
        self._file_browser = FileBrowser(Widget.FILL_FRAME, os.path.expanduser("~"))
        layout.add_widget(self._file_browser)
        self.fix()

    def process_event(self, event):
        if isinstance(event, KeyboardEvent) and event.key_code == Screen.KEY_ENTER:
            # If ENTER is pressed, call the callback with the selected file
            self._callback(self._file_browser.value)
            raise NextScene("Main")
        return super(FileBrowserDialog, self).process_event(event)

    def _on_close(self):
        self._callback(None)
        raise NextScene("Main")


def demo(screen, scene):
    scenes = [
        Scene([TextEditor(screen)], -1, name="Main")
    ]

    screen.play(scenes, stop_on_resize=True, start_scene=scene)


if __name__ == "__main__":
    last_scene = None
    while True:
        try:
            Screen.wrapper(demo, catch_interrupt=True, arguments=[last_scene])
            sys.exit(0)
        except ResizeScreenError as e:
            last_scene = e.scene
