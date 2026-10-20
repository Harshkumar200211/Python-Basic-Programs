"""30. Check Prime Number

Python practice program 30 of 100.
"""

n = int(input("Enter a number: "))
is_prime = n >= 2
for divisor in range(2, int(n ** 0.5) + 1):
    if n % divisor == 0:
        is_prime = False
        break
if is_prime:
    print("Prime number")
else:
    print("Not a prime number")
