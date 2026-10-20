"""90. Merge Two Sorted Lists

Python practice program 90 of 100.
"""

first = [1, 4, 7, 10]
second = [2, 3, 8, 11]
merged = []
i = j = 0
while i < len(first) and j < len(second):
    if first[i] <= second[j]:
        merged.append(first[i])
        i += 1
    else:
        merged.append(second[j])
        j += 1
merged.extend(first[i:])
merged.extend(second[j:])
print("Merged list:", merged)
