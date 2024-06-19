import urwid
import os


class FileManagerWidget(urwid.WidgetWrap):
    signals = ['file_selected']

    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.file_list = urwid.SimpleListWalker([])
        super().__init__(urwid.ListBox(self.file_list))

        self.refresh_file_list()

    def refresh_file_list(self):
        self.file_list.clear()
        files = os.listdir(self.folder_path)
        for file in files:
            button = urwid.Button(file, on_press=self.handle_file_click)
            self.file_list.append(urwid.AttrMap(button, None, focus_map='reversed'))

    def handle_file_click(self, button, *_):
        filename = button.get_label()
        urwid.emit_signal(self, 'file_selected', self.folder_path, filename)


class FileManagerApp:
    def __init__(self):
        self.current_folder = os.getcwd()
        self.widget = FileManagerWidget(self.current_folder)
        urwid.connect_signal(self.widget, 'file_selected', self.handle_file_selected)

        self.main_loop = urwid.MainLoop(self.widget, palette=[('reversed', 'standout', '')])
        self.main_loop.run()

    def handle_file_selected(self, folder_path, filename):
        selected_path = os.path.join(folder_path, filename)
        if os.path.isdir(selected_path):
            self.current_folder = selected_path
            self.widget.folder_path = selected_path
            self.widget.refresh_file_list()
        else:
            self.main_loop.stop()


if __name__ == '__main__':
    FileManagerApp()
