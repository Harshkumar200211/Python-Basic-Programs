"""26. Count Digits in an Integer

Python practice program 26 of 100.
"""

number = abs(int(input("Enter an integer: ")))
if number == 0:
    count = 1
else:
    count = 0
    while number > 0:
        count += 1
        number //= 10
print("Digits =", count)
