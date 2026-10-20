"""13. Largest of Two Numbers

Python practice program 13 of 100.
"""

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("Largest =", a)
elif b > a:
    print("Largest =", b)
else:
    print("Both are equal")
