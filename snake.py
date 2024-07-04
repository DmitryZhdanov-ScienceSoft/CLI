import random
import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN

# Инициализация
curses.initscr()
win = curses.newwin(20, 60, 0, 0)
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)

# Начальное положение змейки и еды
snake = [(4, 10), (4, 9), (4, 8)]
food = (10, 20)


# Функция для создания новой еды
def create_food():
    while True:
        food = (random.randint(1, 18), random.randint(1, 58))
        if food not in snake:
            return food


# Создаем начальную еду
food = create_food()

# Игровая логика
score = 0
ESC = 27
key = KEY_RIGHT

while key != ESC:
    win.clear()
    win.border(0)
    win.addstr(0, 2, 'Score : ' + str(score) + ' ')
    win.addstr(0, 27, ' SNAKE ')

    # Отрисовка еды
    try:
        win.addch(food[0], food[1], '#')
    except curses.error:
        pass  # Игнорируем ошибку, если координаты выходят за границы

    # Отрисовка змейки
    for i, c in enumerate(snake):
        try:
            win.addch(c[0], c[1], '*' if i == 0 else 'o')
        except curses.error:
            pass  # Игнорируем ошибку, если координаты выходят за границы

    # Отладочная информация
    win.addstr(19, 2, f'Food: {food}')

    win.timeout(150 - (len(snake) // 5 + len(snake) // 10) % 120)

    prevKey = key
    event = win.getch()
    key = key if event == -1 else event

    if key == ord(' '):
        key = -1
        while key != ord(' '):
            key = win.getch()
        key = prevKey
        continue

    if key not in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, ESC]:
        key = prevKey

    # Вычисляем следующую координату головы
    y = snake[0][0]
    x = snake[0][1]
    if key == KEY_DOWN:
        y += 1
    if key == KEY_UP:
        y -= 1
    if key == KEY_LEFT:
        x -= 1
    if key == KEY_RIGHT:
        x += 1

    snake.insert(0, (y, x))

    # Проверка на столкновение с границами
    if y == 0 or y == 19 or x == 0 or x == 59:
        break

    # Если змейка съела себя
    if snake[0] in snake[1:]:
        break

    if snake[0] == food:
        # Змейка съела еду
        score += 1
        food = create_food()
    else:
        # Двигаем змейку
        last = snake.pop()

curses.endwin()
print(f"Final score = {score}")