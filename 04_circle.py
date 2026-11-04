import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius


radius = float(input("Enter radius: "))

c = Circle(radius)
print(f"Area          : {c.area():.2f}")
print(f"Circumference : {c.circumference():.2f}")
