import curses

def main(stdscr):
    def save_file(filename="output.txt"):
        with open(filename, "w") as f:
            for line in text:
                f.write(line + "\n")
        return f"File saved as {filename}"

    curses.curs_set(1)  # Отображение курсора
    stdscr.clear()
    stdscr.refresh()
    rows, cols = stdscr.getmaxyx()

    text = [""]
    cursor_x = 0
    cursor_y = 0
    status_bar = "CTRL+S to save, CTRL+Q to quit, CTRL+Z to quit"

    while True:
        stdscr.clear()
        for i, line in enumerate(text):
            stdscr.addstr(i, 0, line)
        stdscr.addstr(rows - 1, 0, status_bar)
        stdscr.move(cursor_y, cursor_x)
        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_UP:
            cursor_y = max(0, cursor_y - 1)
            cursor_x = min(cursor_x, len(text[cursor_y]))
        elif key == curses.KEY_DOWN:
            cursor_y = min(len(text) - 1, cursor_y + 1)
            cursor_x = min(cursor_x, len(text[cursor_y]))
        elif key == curses.KEY_LEFT:
            cursor_x = max(0, cursor_x - 1)
        elif key == curses.KEY_RIGHT:
            cursor_x = min(len(text[cursor_y]), cursor_x + 1)
        elif key == curses.KEY_BACKSPACE or key == 127:
            if cursor_x > 0:
                text[cursor_y] = text[cursor_y][:cursor_x - 1] + text[cursor_y][cursor_x:]
                cursor_x -= 1
            elif cursor_y > 0:
                cursor_x = len(text[cursor_y - 1])
                text[cursor_y - 1] += text[cursor_y]
                text.pop(cursor_y)
                cursor_y -= 1
        elif key == 10:  # Enter
            text.insert(cursor_y + 1, text[cursor_y][cursor_x:])
            text[cursor_y] = text[cursor_y][:cursor_x]
            cursor_y += 1
            cursor_x = 0
        elif key == 27:  # Escape
            break
        elif key == 19:  # Ctrl+S (19 is the ASCII code for Ctrl+S)
            status_bar = save_file()
        elif key == 17:  # Ctrl+Q (17 is the ASCII code for Ctrl+Q)
            break
        elif key == 26:  # Ctrl+Z (26 is the ASCII code for Ctrl+Z)
            break
        elif 32 <= key <= 126:  # Печатаемые символы
            text[cursor_y] = text[cursor_y][:cursor_x] + chr(key) + text[cursor_y][cursor_x:]
            cursor_x += 1

        if cursor_y >= len(text):
            text.append("")

    stdscr.clear()
    stdscr.addstr(0, 0, "Saving text...")
    stdscr.refresh()
    save_file()
    stdscr.addstr(1, 0, "Text saved to output.txt. Press any key to exit.")
    stdscr.getch()

curses.wrapper(main)
