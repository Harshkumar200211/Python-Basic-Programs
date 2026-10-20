"""56. Rotate a List One Step to the Right

Python practice program 56 of 100.
"""

numbers = [1, 2, 3, 4, 5]
if numbers:
    last = numbers[-1]
    for index in range(len(numbers) - 1, 0, -1):
        numbers[index] = numbers[index - 1]
    numbers[0] = last
print("Rotated:", numbers)
