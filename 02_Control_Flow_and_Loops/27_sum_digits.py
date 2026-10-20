"""27. Sum of Digits

Python practice program 27 of 100.
"""

number = abs(int(input("Enter an integer: ")))
total = 0
while number > 0:
    total += number % 10
    number //= 10
print("Sum of digits =", total)
