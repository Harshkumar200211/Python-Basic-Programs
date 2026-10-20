"""09. Swap Two Numbers

Python practice program 09 of 100.
"""

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Before:", a, b)
temp = a
a = b
b = temp
print("After:", a, b)
