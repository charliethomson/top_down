from pyglet.window.key import W, S, A, D

from .player import Player

from include.rect import *
from include.bullet import Bullet
from include.vector2d import Vector2D


class Game:
    """
    This is the main game class. It handles all the game logic, drawing, controls, etc.
    """

    def __init__(self, window, keys, DEBUG=False):
        """
        initialises the Game class

        params: 
            window: the main <pyglet.window.Window> object for the game
            keys: the <pyglet.key.KeyStateHandler> object that handles currently pressed keys 
        kwargs:
            DEBUG: if true, enables debug mode
        """
        self.window = window
        self.frame_count = 0

        self.DEBUG = DEBUG

        self.keys = keys

    def _get_all_elements(self) -> tuple:
        return (
            self.background,
            self.player,
            *self.menus,
            *self.enemies,
            *self.walls,
            *self.bullets,
        )

    def get_element_by_id(self, id_):
        for element in self.elements:
            if element.id_ == id_:
                return element

    def handle_controls(self):
        """
        handles all the controls for the player
        """
        x = 8 if self.keys[D] else -8 if self.keys[A] else 0
        y = 8 if self.keys[W] else -8 if self.keys[S] else 0

        self.player.move(Vector2D(x, y))

    def setup(self):
        """
        sets up the window w/ caption, icon, size, background
        """
        self.window.set_caption("TOPDOWNSHOOTER v1.0")
        # self.window.set_icon(icon goes here lmao)
        self.window.set_size(1000, 1000)
        # self.window.set_location(100, 1000)
        self.window.clear()
        self.background = Rect(
            0,
            0,
            self.window.width,
            self.window.height,
            mode=CORNERS,
            draw=False,
            id_="background",
        )
        self.player = Player(self.window, "player", DEBUG=self.DEBUG)

        self.enemies = []

        self.walls = []

        self.mouse_position = Vector2D()

        self.menus = []

        self.bullets = []

        self.elements = self._get_all_elements()

    def on_mouse_motion(self, x, y, dx, dy):
        """
        updates the mouse position variable
        params:
            x: the new x position of the cursor
            y: the new y position of the cursor
            dx: the difference between the last x position and the new x position
            dy: the difference between the last y position and the new y position
        """
        self.mouse_position = Vector2D(x, y)
        self.player.on_mouse_motion(self.mouse_position)

    def on_mouse_press(self, x, y, button, mod):
        """

        called when the mouse is pressed
        handles the `shooting` of the game 

        params:
            x: the current x position of the cursor
            y: the current y position of the cursor
            button: the mouse button being pressed
            mod: any modifiers on the keyboard currently active (NUM_LOCK, SCROLL_LOCK, CAPS_LOCK, etc)
        """
        pos, vel, angle = self.player._get_bullet_data()
        self.bullets.append(Bullet(pos, vel, angle, f"bullet frame {self.frame_count}"))

    def mainloop(self, delta):
        """
        The main game loop

        params:
            delta: the time from the last time the function was called
                   a required param for the pyglet.clock.schedule_interval() function
        """
        # print(self.keys)
        self.elements = self._get_all_elements()
        self.frame_count += 1
        self.window.clear()
        [element.draw() for element in self.elements]
        self.player.update()
        print(f"\n\n\n\t{self.bullets}\n\n\n")
        for bullet in self.bullets:
            bullet.update()
            if not (
                0 < bullet.pos.x < self.window.width
                and 0 < bullet.pos.y < self.window.height
            ):
                self.bullets.remove(bullet)
        self.handle_controls()
