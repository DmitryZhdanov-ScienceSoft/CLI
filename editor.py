import urwid
import os

class TextEditor:
    def __init__(self):
        self.content = urwid.SimpleFocusListWalker([
            urwid.Edit("Type here: "),
        ])
        self.listbox = urwid.ListBox(self.content)
        self.file_name = None
        self.main_loop = urwid.MainLoop(
            urwid.Frame(self.listbox, footer=self.footer()),
            unhandled_input=self.handle_input,
            palette=[('footer', 'black', 'light gray'), ('key', 'light cyan', 'black', 'bold')],
        )

    def footer(self):
        footer_text = [
            ('title', "Text Editor"), "    ",
            ('key', "F2"), ": Save    ",
            ('key', "F3"), ": Open    ",
            ('key', "F4"), ": Quit",
        ]
        return urwid.AttrMap(urwid.Text(footer_text), 'footer')

    def handle_input(self, key):
        if key == 'f4':
            raise urwid.ExitMainLoop()
        elif key == 'f2':
            self.show_save_dialog()
        elif key == 'f3':
            self.show_open_dialog()

    def show_save_dialog(self):
        save_edit = urwid.Edit("Save as: ", edit_text=self.file_name or "")
        save_dialog = urwid.Pile([save_edit, urwid.Button("OK", on_press=self.save_file, user_data=save_edit)])
        overlay = urwid.Overlay(urwid.LineBox(save_dialog), self.main_loop.widget,
                                'center', ('relative', 50), 'middle', ('relative', 25))
        self.main_loop.widget = overlay

    def save_file(self, button, save_edit):
        self.file_name = save_edit.edit_text
        if self.file_name:
            with open(self.file_name, "w") as f:
                for edit in self.content:
                    f.write(edit.edit_text + "\n")
            self.show_message("File saved!")

    def show_open_dialog(self):
        open_edit = urwid.Edit("Open file: ")
        open_dialog = urwid.Pile([open_edit, urwid.Button("OK", on_press=self.open_file, user_data=open_edit)])
        overlay = urwid.Overlay(urwid.LineBox(open_dialog), self.main_loop.widget,
                                'center', ('relative', 50), 'middle', ('relative', 25))
        self.main_loop.widget = overlay

    def open_file(self, button, open_edit):
        self.file_name = open_edit.edit_text
        if self.file_name and os.path.isfile(self.file_name):
            with open(self.file_name, "r") as f:
                lines = f.readlines()
            self.content.clear()
            for line in lines:
                self.content.append(urwid.Edit(edit_text=line.strip()))
            self.show_message("File opened!")
        else:
            self.show_message("File not found!")

    def show_message(self, message):
        message_dialog = urwid.Pile([urwid.Text(message), urwid.Button("OK", on_press=self.clear_overlay)])
        overlay = urwid.Overlay(urwid.LineBox(message_dialog), self.main_loop.widget,
                                'center', ('relative', 50), 'middle', ('relative', 25))
        self.main_loop.widget = overlay

    def clear_overlay(self, button):
        self.main_loop.widget = urwid.Frame(self.listbox, footer=self.footer())

    def run(self):
        self.main_loop.run()

if __name__ == "__main__":
    TextEditor().run()
