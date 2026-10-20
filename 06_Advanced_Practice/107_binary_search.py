"""107. Binary Search in a Sorted List."""

numbers = [3, 7, 11, 18, 25, 31, 42]
target = int(input("Enter number to find: "))
low = 0
high = len(numbers) - 1
found = False

while low <= high:
    middle = (low + high) // 2
    if numbers[middle] == target:
        print("Found at index:", middle)
        found = True
        break
    elif numbers[middle] < target:
        low = middle + 1
    else:
        high = middle - 1

if not found:
    print("Number not found")
