DEBUG = True

from pyglet.window import Window
from pyglet.window.key import KeyStateHandler
from pyglet.clock import schedule_interval
from pyglet.app import run as run_game

from src.game import Game

keys = KeyStateHandler()
window = Window()
window.push_handlers(keys)
game = Game(window, keys, DEBUG=DEBUG)
game.setup()


@window.event
def on_mouse_motion(x, y, dx, dy):
    game.on_mouse_motion(x, y, dx, dy)


@window.event
def on_mouse_press(x, y, button, mod):
    game.on_mouse_press(x, y, button, mod)


@window.event
def on_mouse_drag(x, y, dx, dy, button, mod):
    game.on_mouse_motion(x, y, dx, dy)
    game.on_mouse_press(x, y, button, mod)


schedule_interval(game.mainloop, 1 / 60.0)
if __name__ == "__main__":
    run_game()
