"""20. Simple Calculator

Python practice program 20 of 100.
"""

a = float(input("Enter first number: "))
operator = input("Operator (+, -, *, /): ")
b = float(input("Enter second number: "))
if operator == "+":
    print("Result:", a + b)
elif operator == "-":
    print("Result:", a - b)
elif operator == "*":
    print("Result:", a * b)
elif operator == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Unknown operator")
