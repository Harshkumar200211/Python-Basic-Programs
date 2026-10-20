"""49. Count Even Numbers in a List

Python practice program 49 of 100.
"""

numbers = [2, 7, 8, 11, 14, 19]
count = 0
for number in numbers:
    if number % 2 == 0:
        count += 1
print("Even count =", count)
