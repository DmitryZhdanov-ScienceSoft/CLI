import urwid

def main():
    # Определяем палитру цветов
    palette = [
        ('banner', 'black', 'light gray'),
        ('streak', 'black', 'dark red'),
        ('background', 'black', 'light gray'),
    ]

    # Создаем текстовый виджет
    text = urwid.Text(('banner', u"Hello World"), align='center')
    streak = urwid.AttrMap(text, 'streak')

    # Создаем текст для фона
    background_text = urwid.Text(u'\u2592' * 80, align='left')
    background = urwid.AttrMap(urwid.Filler(background_text, valign='top'), 'background')

    # Используем Pile для упаковки виджетов
    pile = urwid.Pile([background, streak])
    top = urwid.Filler(pile, valign='top')

    # Создаем главное окно
    loop = urwid.MainLoop(top, palette)

    loop.run()

if __name__ == '__main__':
    main()
