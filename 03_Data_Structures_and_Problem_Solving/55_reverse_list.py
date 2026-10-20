"""55. Reverse a List Without reverse()

Python practice program 55 of 100.
"""

numbers = [10, 20, 30, 40, 50]
reversed_numbers = []
for index in range(len(numbers) - 1, -1, -1):
    reversed_numbers.append(numbers[index])
print("Reversed:", reversed_numbers)
