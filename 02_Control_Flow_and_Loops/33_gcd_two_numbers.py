"""33. GCD of Two Numbers

Python practice program 33 of 100.
"""

a = abs(int(input("Enter first number: ")))
b = abs(int(input("Enter second number: ")))
while b != 0:
    a, b = b, a % b
print("GCD =", a)
