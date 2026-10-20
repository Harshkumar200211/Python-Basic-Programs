"""35. Check Armstrong Number

Python practice program 35 of 100.
"""

number = int(input("Enter a non-negative integer: "))
digits = str(number)
power = len(digits)
total = 0
for digit in digits:
    total += int(digit) ** power
if number == total:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
