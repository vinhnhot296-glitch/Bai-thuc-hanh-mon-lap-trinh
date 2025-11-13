import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

# Ví dụ sử dụng
c = Circle(7)
print("Diện tích:", c.area())
print("Chu vi:", c.circumference())
