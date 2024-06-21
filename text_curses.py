import curses

def main(stdscr):
    curses.curs_set(0)  # Отключаем отображение курсора
    stdscr.nodelay(1)  # Делаем ввод не блокирующим
    stdscr.timeout(100)  # Устанавливаем таймаут для ввода

    sh, sw = stdscr.getmaxyx()  # Получаем размеры экрана
    w = curses.newwin(sh, sw, 0, 0)  # Создаем новое окно

    text = "Hello, TUI!"
    w.addstr(0, 0, text)  # Добавляем текст в окно
    w.refresh()

    while True:
        key = w.getch()  # Получаем ввод с клавиатуры
        if key == curses.KEY_EXIT or key == ord('q'):
            break

curses.wrapper(main)
