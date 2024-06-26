from random import randint
from asciimatics.screen import Screen
from asciimatics.event import KeyboardEvent
from collections import deque

class SnakeGame:
    def __init__(self, screen):
        self.screen = screen
        self.snake = deque([(5, 5)])
        self.food = self._place_food()
        self.direction = (1, 0)
        self.game_over = False

    def _place_food(self):
        while True:
            food = (randint(1, self.screen.width - 2), randint(1, self.screen.height - 2))
            if food not in self.snake:
                return food

    def process_input(self):
        event = self.screen.get_event()
        if isinstance(event, KeyboardEvent):
            if event.key_code in [ord('w'), ord('W')]:
                if self.direction != (0, 1):  # Prevent snake from reversing
                    self.direction = (0, -1)
            elif event.key_code in [ord('s'), ord('S')]:
                if self.direction != (0, -1):  # Prevent snake from reversing
                    self.direction = (0, 1)
            elif event.key_code in [ord('a'), ord('A')]:
                if self.direction != (1, 0):  # Prevent snake from reversing
                    self.direction = (-1, 0)
            elif event.key_code in [ord('d'), ord('D')]:
                if self.direction != (-1, 0):  # Prevent snake from reversing
                    self.direction = (1, 0)
            elif event.key_code in [ord('q'), ord('Q')]:
                self.game_over = True

    def update(self):
        if self.game_over:
            return
        head = (self.snake[0][0] + self.direction[0], self.snake[0][1] + self.direction[1])
        if head[0] < 0 or head[0] >= self.screen.width or head[1] < 0 or head[1] >= self.screen.height or head in self.snake:
            self.game_over = True
        else:
            self.snake.appendleft(head)
            if head == self.food:
                self.food = self._place_food()
            else:
                self.snake.pop()

    def draw(self):
        self.screen.clear_buffer(7, 0, 0)
        for x, y in self.snake:
            self.screen.print_at('O', x, y, 3)
        self.screen.print_at('X', self.food[0], self.food[1], 2)
        if self.game_over:
            self.screen.print_at('GAME OVER', self.screen.width // 2 - 5, self.screen.height // 2, 1)
        self.screen.refresh()

def play_game(screen):
    game = SnakeGame(screen)
    while not game.game_over:
        game.process_input()
        game.update()
        game.draw()
        screen.wait_for_input(0.1)

Screen.wrapper(play_game)
