"""89. Find the Most Common List Value

Python practice program 89 of 100.
"""

numbers = [2, 3, 2, 5, 3, 2, 4, 3, 3]
frequency = {}
for number in numbers:
    frequency[number] = frequency.get(number, 0) + 1
most_common = max(frequency, key=frequency.get)
print("Most common:", most_common)
print("Frequency:", frequency[most_common])
