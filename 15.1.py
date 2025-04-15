import math
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        if isinstance(other,Rectangle):
            return self.get_square() == other.get_square()
        return False

    def __add__(self, other):
        total_area = self.get_square() + other.get_square()
        side = math.isqrt(total_area)
        while total_area % side != 0:
            side += 1
        new_width = side
        new_height = total_area // side
        return Rectangle(new_width, new_height)
    def __mul__(self, n):
        new_area = self.get_square() * n
        new_area = round(new_area)
        side = math.isqrt(new_area)
        while new_area % side != 0:
            side += 1
        new_width = side
        new_height = new_area // side
        return Rectangle(new_width, new_height)

    def __str__(self):
        return f' Rectangle : {self.width} * {self.height} = {self.get_square()}'


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'