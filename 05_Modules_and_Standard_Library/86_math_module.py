"""86. Practice the math module."""

import math

number = float(input("Enter a non-negative number: "))
if number >= 0:
    print("Square root:", math.sqrt(number))
else:
    print("Square root is not real for a negative number")

radius = float(input("Enter circle radius: "))
print("Circle area:", round(math.pi * radius ** 2, 2))
print("Ceiling of radius:", math.ceil(radius))
print("Floor of radius:", math.floor(radius))
