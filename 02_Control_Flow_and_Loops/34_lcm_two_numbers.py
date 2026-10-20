"""34. LCM of Two Numbers

Python practice program 34 of 100.
"""

a = abs(int(input("Enter first number: ")))
b = abs(int(input("Enter second number: ")))
if a == 0 or b == 0:
    print("LCM = 0")
else:
    x, y = a, b
    while y != 0:
        x, y = y, x % y
    print("LCM =", (a * b) // x)
