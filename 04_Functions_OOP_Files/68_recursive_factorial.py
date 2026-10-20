"""68. Factorial Using Recursion

Python practice program 68 of 100.
"""

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

number = int(input("Enter a non-negative number: "))
if number < 0:
    print("Enter a non-negative number")
else:
    print("Factorial =", factorial(number))
