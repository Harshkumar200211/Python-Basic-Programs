"""36. Check Perfect Number

Python practice program 36 of 100.
"""

n = int(input("Enter a positive integer: "))
total = 0
for divisor in range(1, n):
    if n % divisor == 0:
        total += divisor
if n > 1 and total == n:
    print("Perfect number")
else:
    print("Not a perfect number")
