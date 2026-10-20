"""48. Smallest Element in a List

Python practice program 48 of 100.
"""

numbers = [12, 45, 7, 89, 23]
smallest = numbers[0]
for number in numbers:
    if number < smallest:
        smallest = number
print("Smallest =", smallest)
