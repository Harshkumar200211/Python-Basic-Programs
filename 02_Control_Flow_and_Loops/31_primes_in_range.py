"""31. Print Prime Numbers up to N

Python practice program 31 of 100.
"""

n = int(input("Print primes up to: "))
for number in range(2, n + 1):
    is_prime = True
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            is_prime = False
            break
    if is_prime:
        print(number)
