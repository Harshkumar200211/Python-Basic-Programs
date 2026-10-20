"""23. Sum of First N Natural Numbers

Python practice program 23 of 100.
"""

n = int(input("Enter N: "))
total = 0
for number in range(1, n + 1):
    total += number
print("Sum =", total)
