"""54. Sort a List Using Bubble Sort

Python practice program 54 of 100.
"""

numbers = [5, 1, 4, 2, 8]
for i in range(len(numbers)):
    for j in range(len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
print("Sorted:", numbers)
