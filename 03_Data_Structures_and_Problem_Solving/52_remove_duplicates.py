"""52. Remove Duplicates from a List

Python practice program 52 of 100.
"""

numbers = [1, 2, 2, 3, 1, 4, 3]
unique = []
for number in numbers:
    if number not in unique:
        unique.append(number)
print("Without duplicates:", unique)
