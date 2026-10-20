"""45. Use continue to Skip Multiples of 3

Python practice program 45 of 100.
"""

for number in range(1, 21):
    if number % 3 == 0:
        continue
    print(number)
