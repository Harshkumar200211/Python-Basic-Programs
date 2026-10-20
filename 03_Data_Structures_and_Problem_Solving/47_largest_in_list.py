"""47. Largest Element in a List

Python practice program 47 of 100.
"""

numbers = [12, 45, 7, 89, 23]
largest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number
print("Largest =", largest)
