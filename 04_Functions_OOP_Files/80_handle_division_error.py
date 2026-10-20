"""80. Handle Division by Zero

Python practice program 80 of 100.
"""

try:
    a = float(input("Enter numerator: "))
    b = float(input("Enter denominator: "))
    result = a / b
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Enter valid numbers")
else:
    print("Result:", result)
