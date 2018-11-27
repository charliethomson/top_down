from include.vector2d import Vector2D
from include.rect import *
from math import sin, cos, radians


class Bullet:
    def __init__(self, pos: Vector2D, vel: Vector2D, angle: float, id_: str):
        """
        params:
            pos: Vector2D; the initial position of the bullet
            vel: Vector2D; the initial velocity of the bullet
            angle: float; the angle the bullet is shot at 
            id_: str; the logical id of the bullet
        """

        self.pos = pos
        self.angle = angle
        self.vel = Vector2D(5 * sin((self.angle)), 5 * cos((self.angle))) + (vel // 2)
        self.id_ = id_

    def __repr__(self):
        return f"\n{self.id_}:\
             \n\tpos: {self.pos};\
             \n\tvel: {self.vel};\
             \n\tangle: {self.angle};"

    def update(self):
        self.pos += self.vel

    def draw(self):
        pos = Vector2D(int(self.pos.x), int(self.pos.y))
        Rect(pos.x, pos.y, 8, 8, color=BLACK, id_="bullet")
