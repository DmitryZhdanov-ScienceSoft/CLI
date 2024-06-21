from asciimatics.widgets import Frame, Layout, TextBox, Button, Widget, FileBrowser
from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.exceptions import StopApplication, ResizeScreenError
from asciimatics.event import KeyboardEvent, MouseEvent
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
        self.fix()

        # Создаем макет для кнопок
        button_layout = Layout([1, 1, 1])
        self.add_layout(button_layout)
        button_layout.add_widget(Button("Open", self._open), 0)
        button_layout.add_widget(Button("Save", self._save), 1)
        button_layout.add_widget(Button("Quit", self._quit), 2)
        self.fix()

        self.current_file = None

    def _open(self):
        # Показать диалоговое окно для выбора файла
        self._scene.add_effect(FileBrowserDialog(self._screen, self._load_file))

    def _load_file(self, filename):
        # Проверка, является ли выбранный путь файлом, и загрузка его содержимого
        if filename and os.path.isfile(filename):
            try:
                with open(filename, "r") as f:
                    self.text_box.value = f.read()
                self.current_file = filename
                self._scene.remove_effect(self._scene.effects[-1])
            except FileNotFoundError:
                self._show_message("File not found!")
            except Exception as e:
                self._show_message(f"An error occurred: {str(e)}")
        else:
            self._show_message("Selected path is not a file!")

    def _save(self):
        if self.current_file:
            with open(self.current_file, "w") as f:
                f.write(self.text_box.value)
            self._show_message("File saved successfully!")
        else:
            self._show_message("No file currently open!")

    def _quit(self):
        raise StopApplication("User pressed quit")

    def _show_message(self, message):
        self._scene.add_effect(PopUpDialog(self._screen, message, ["OK"]))


class FileBrowserDialog(Frame):
    def __init__(self, screen, callback):
        super(FileBrowserDialog, self).__init__(screen, screen.height * 2 // 3, screen.width * 2 // 3,
                                                has_border=True, can_scroll=True)
        self._callback = callback

        # Create a FileBrowser widget and add it to the Frame
        layout = Layout([100], fill_frame=True)
        self.add_layout(layout)
        self._file_browser = FileBrowser(Widget.FILL_FRAME, os.path.expanduser("~"))
        layout.add_widget(self._file_browser)
        self.fix()

    def process_event(self, event):
        if isinstance(event, KeyboardEvent):
            if event.key_code in [10, 13]:  # Enter key codes
                # If ENTER is pressed, call the callback with the selected file or change directory
                if self._file_browser.value:
                    if os.path.isfile(self._file_browser.value):
                        self._callback(self._file_browser.value)
                        self._close()
                    elif os.path.isdir(self._file_browser.value):
                        self._file_browser.path = self._file_browser.value
                        self._file_browser.value = None  # Clear selection
            elif event.key_code in [27]:  # Escape key code
                # If ESCAPE is pressed, close the file browser
                self._callback(None)
                self._close()
        elif isinstance(event, MouseEvent) and event.buttons != 0:
            # If mouse event is detected, check if a file is selected or change directory
            self._file_browser.process_event(event)
            if self._file_browser.value:
                if os.path.isfile(self._file_browser.value):
                    self._callback(self._file_browser.value)
                    self._close()
                elif os.path.isdir(self._file_browser.value):
                    self._file_browser.path = self._file_browser.value
                    self._file_browser.value = None  # Clear selection
        return super(FileBrowserDialog, self).process_event(event)

    def _close(self):
        self._scene.remove_effect(self)


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
