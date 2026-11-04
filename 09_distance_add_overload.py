class Distance:
    def __init__(self, feet, inches):
        total_inches = feet * 12 + inches
        self.feet, self.inches = divmod(total_inches, 12)

    def __add__(self, other):
        total = (self.feet * 12 + self.inches) + (other.feet * 12 + other.inches)
        return Distance(0, total)

    def __str__(self):
        return f"{self.feet} feet {self.inches} inches"


d1 = Distance(5, 9)
d2 = Distance(3, 7)
d3 = d1 + d2

print("Distance 1:", d1)
print("Distance 2:", d2)
print("Sum       :", d3)
