from pyglet.graphics import draw as gl_draw
from pyglet.gl import GL_LINES

from typing import Tuple

# COLOR CONSTANTS

RED = (255, 0, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
PINK = (255, 0, 200)
GREEN = (0, 255, 0)
BROWN = (80, 50, 0)
ORANGE = (255, 90, 0)
PURPLE = (140, 0, 255)
YELLOW = (255, 255, 0)
SEA_GREEN = (0, 255, 192)

BLACK = (0, 0, 0)
DARK_GRAY = (64, 64, 64)
GRAY = (128, 128, 128)
LIGHT_GRAY = (192, 192, 192)
WHITE = (255, 255, 255)

COLORS = {
    "RED": (255, 0, 0),
    "BLUE": (0, 0, 255),
    "CYAN": (0, 255, 255),
    "PINK": (255, 0, 200),
    "GRAY": (128, 128, 128),
    "BLACK": (0, 0, 0),
    "GREEN": (0, 255, 0),
    "BROWN": (80, 50, 0),
    "WHITE": (255, 255, 255),
    "ORANGE": (255, 90, 0),
    "PURPLE": (140, 0, 255),
    "YELLOW": (255, 255, 0),
    "DARK_GRAY": (64, 64, 64),
    "SEA_GREEN": (0, 255, 192),
    "LIGHT_GRAY": (192, 192, 192),
}
# end

# TPYES

Color = Tuple[int, int, int]

# end


class Line:
    """
    A line interface class with pyglet
    """

    def __init__(
        self,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
        id_: str,
        color: Color = RED,
        draw: bool = True,
    ):
        """
        Initialises the Line class

        params:
            x, y1: the x, y position of the first point
            x, y2: the x, y position of the second point
            id_: the logical id for the line (ex. `aim`)
            color: the color of the 
        """
        self.x1, self.y1 = self.pos1 = x1, y1
        self.x2, self.y2 = self.pos2 = x2, y2
        self.color = color

        if draw:
            self.draw()

    def draw(self):
        gl_draw(2, GL_LINES, ("v2i", (*self.pos1, *self.pos2)), ("c3B", self.color * 2))
