"""108. Sort a List Using Selection Sort."""

numbers = [29, 10, 14, 37, 13]

for i in range(len(numbers)):
    smallest = i
    for j in range(i + 1, len(numbers)):
        if numbers[j] < numbers[smallest]:
            smallest = j
    numbers[i], numbers[smallest] = numbers[smallest], numbers[i]

print("Sorted list:", numbers)
