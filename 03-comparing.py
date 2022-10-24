import math

class Vector2:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def magnitude(self):
        return math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)

    def __lt__(self, other):
        return self.magnitude() < other.magnitude()

    def __le__(self, other):
        return self.magnitude() <= other.magnitude()

v1 = Vector2(0, 0, 4, 3)  # magnitude 5
v2 = Vector2(0, 0, 4, 3)  # magnitude 5

print(v1 < v2)
print(v1 > v2)
print(v1 <= v2)
print(v1 >= v2)