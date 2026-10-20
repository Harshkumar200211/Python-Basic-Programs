"""32. Fibonacci Series

Python practice program 32 of 100.
"""

terms = int(input("How many terms? "))
a, b = 0, 1
for _ in range(max(0, terms)):
    print(a, end=" ")
    a, b = b, a + b
print()
