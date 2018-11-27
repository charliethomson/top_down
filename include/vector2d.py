class Vector2D:
    def __init__(self, x: int = 0, y: int = 0):
        self.x, self.y = x, y

    def __repr__(self) -> str:
        return f"{self.x}, {self.y}"

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __div__(self, other):
        if isinstance(other, (int, float)):
            return Vector2D(self.x / other, self.y / other)
        if isinstance(other, Vector2D):
            return Vector2D(self.x / other.x, self.y / other.y)

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __lt__(self, other):
        return (self.x < other.x) and (self.y < other.y)

    def __gt__(self, other):
        return self.x > other.x) and (self.y > other.y)

    def __le__(self, other):
        return self < other or self == other

    def __ge__(self, other):
        return self > other or self == other

    def __ne__(self, other):
        return not self == other

    def floor(self):
        return Vector2D(self.x // 1, self.y // 1)
