"""101. Find Two Numbers with a Target Sum."""

numbers = [2, 7, 11, 15]
target = 9
found = False

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print("Values:", numbers[i], numbers[j])
            print("Indexes:", i, j)
            found = True
            break
    if found:
        break

if not found:
    print("No pair found")
