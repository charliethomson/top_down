from include.vector2d import Vector2D
from include.rect import *
from include.line import *
from math import atan2, degrees


class Player:
    def __init__(self, window, id_, DEBUG=False):
        self.window = window
        self.health = 0
        self.pos = Vector2D(self.window.width // 2, self.window.height // 2)
        self.vel = Vector2D()
        self.w, self.h = 25, 25

        self.DEBUG = DEBUG

        self.id_ = id_

        self.mouse_pos = Vector2D()

        self.angle = 0

        # # what the theoretical first person player can see
        # self.frustum = None

    def __repr__(self):
        return f"Player:\
                \n\thealth: {self.health};\
                \n\tpos: {(self.pos)};\
                \n\taim angle (d): {degrees(self.angle)};\
                \n\taim angle (r): {self.angle}"

    def _fix_pos(self):
        self.pos = Vector2D(int(self.pos.x), int(self.pos.y))

    def _keep_in_bounds(self):
        if self.pos.x <= self.w // 2:
            self.pos.x = self.w // 2
        if self.pos.x >= self.window.width - self.w // 2:
            self.pos.x = self.window.width - self.w // 2

        if self.pos.y <= self.h // 2:
            self.pos.y = self.h // 2
        if self.pos.y >= self.window.height - self.h // 2:
            self.pos.y = self.window.height - self.h // 2

    def _get_bullet_data(self) -> tuple:
        return (self.pos, self.vel, self.angle)

    def on_mouse_motion(self, pos: Vector2D):
        assert isinstance(pos, Vector2D)
        self.mouse_pos = pos

        opp = self.mouse_pos.y - self.pos.y
        adj = self.mouse_pos.x - self.pos.x

        if opp and adj:
            self.angle = atan2(opp, adj)
        else:
            self.angle = atan2(opp, 1)

        # print(f"tan({opp}) / {adj} = {self.angle}")

    def move(self, amount: Vector2D):
        assert isinstance(amount, Vector2D), "Move amount must be type Vector2D"
        self.vel = amount

    def update(self):
        if self.DEBUG:
            print(self)
            # print(f"player data:\n\tpos: {self.pos}\n\tangle: {self.angle}")
        self._keep_in_bounds()
        self.pos += self.vel
        self.vel = Vector2D()

    def draw(self):
        self._fix_pos()

        if self.DEBUG:
            Rect(
                self.pos.x,
                self.pos.y,
                self.w,
                self.h,
                mode=CENTER,
                color=ORANGE,
                id_="player hitbox",
            )
            Line(
                self.pos.x,
                self.pos.y,
                self.mouse_pos.x,
                self.mouse_pos.y,
                id_="player aim",
            )
