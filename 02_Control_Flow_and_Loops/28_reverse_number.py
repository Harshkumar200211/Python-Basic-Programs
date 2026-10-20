"""28. Reverse a Number

Python practice program 28 of 100.
"""

number = int(input("Enter an integer: "))
sign = -1 if number < 0 else 1
number = abs(number)
reverse = 0
while number > 0:
    reverse = reverse * 10 + number % 10
    number //= 10
print("Reversed =", sign * reverse)
