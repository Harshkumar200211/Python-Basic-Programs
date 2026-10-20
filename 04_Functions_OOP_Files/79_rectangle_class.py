"""79. Rectangle Class with Area and Perimeter

Python practice program 79 of 100.
"""

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

rectangle = Rectangle(10, 5)
print("Area:", rectangle.area())
print("Perimeter:", rectangle.perimeter())
