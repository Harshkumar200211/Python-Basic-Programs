"""81. Safe Integer Input with try-except

Python practice program 81 of 100.
"""

try:
    age = int(input("Enter your age: "))
    print("Next year you will be", age + 1)
except ValueError:
    print("Enter a whole number")
