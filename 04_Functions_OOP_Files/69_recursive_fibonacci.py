"""69. Fibonacci Using Recursion

Python practice program 69 of 100.
"""

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

terms = int(input("How many terms (0 to 10)? "))
if 0 <= terms <= 10:
    for i in range(terms):
        print(fibonacci(i), end=" ")
    print()
else:
    print("Enter a value from 0 to 10")
