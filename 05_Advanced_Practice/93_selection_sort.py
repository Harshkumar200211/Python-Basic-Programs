"""93. Sort a List Using Selection Sort

Python practice program 93 of 100.
"""

numbers = [29, 10, 14, 37, 13]
for i in range(len(numbers)):
    smallest = i
    for j in range(i + 1, len(numbers)):
        if numbers[j] < numbers[smallest]:
            smallest = j
    numbers[i], numbers[smallest] = numbers[smallest], numbers[i]
print("Sorted list:", numbers)
