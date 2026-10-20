"""74. Function with *args

Python practice program 74 of 100.
"""

def add_numbers(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(add_numbers(10, 20, 30))
print(add_numbers(1, 2, 3, 4, 5))
