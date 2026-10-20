"""53. Linear Search in a List

Python practice program 53 of 100.
"""

numbers = [15, 8, 22, 5, 17]
target = int(input("Enter value to search: "))
found_index = -1
for index in range(len(numbers)):
    if numbers[index] == target:
        found_index = index
        break
if found_index != -1:
    print("Found at index:", found_index)
else:
    print("Value not found")
