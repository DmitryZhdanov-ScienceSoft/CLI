from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.renderers import FigletText
from asciimatics.effects import BannerText
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication

def demo(screen):
    effects = [
        BannerText(
            screen,
            FigletText("Hello, World!", font='big'),
            screen.height // 2 - 3,
            Screen.COLOUR_RED
        )
    ]
    screen.play([Scene(effects, -1)], stop_on_resize=True)

Screen.wrapper(demo)
