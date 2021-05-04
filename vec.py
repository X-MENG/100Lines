import math

class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, rhs):
        x = self.x + rhs.x
        y = self.y + rhs.y
        return Vec2(x, y)

    def __sub__(self, rhs):
        x = self.x - rhs.x
        y = self.y - rhs.y
        return Vec2(x, y)

    def __mul__(self, n):
        x = self.x * n
        y = self.y * n
        return Vec2(x, y)

    def __div__(self, n):
        x = self.x / n
        y = self.y / n
        return Vec2(x, y)
    # 稍后再添加
    def __assign__(self, v):
        self.pos = Vec2(v.pos.x, v.pos.y)

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def dot(self, v):
        return self.x * v.x + self.y * v.y

    def proj(self, v):
        v.normalize()
        return self.dot(v)

    def normalize(self):
        s = self.length()
        if s != 0:
            self.x = self.x / s
            self.y = self.y / s

    def output(self):
        print(self.x, self.y)

