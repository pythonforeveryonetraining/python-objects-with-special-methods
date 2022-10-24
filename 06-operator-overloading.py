import math

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __mul__(self, value):
        return Vector2(self.x * value, self.y * value)

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

v1 = Vector2(4, 3)
print(v1.magnitude())
v1 = v1 * 2
print(v1.magnitude())
v2 = Vector2(4, 2) + Vector2(1, 2)
print(v2.magnitude())