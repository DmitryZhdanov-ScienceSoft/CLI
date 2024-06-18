# Пример вывода простой гистограммы в консоли
def draw_histogram(data):
    max_value = max(data)
    scale_factor = 50 / max_value  # масштабирование значений для отображения

    for value in data:
        bar_length = int(value * scale_factor)
        bar = '#' * bar_length
        print(f'{value:5} | {bar}')

if __name__ == '__main__':
    data = [5, 10, 3, 8, 12]
    draw_histogram(data)
