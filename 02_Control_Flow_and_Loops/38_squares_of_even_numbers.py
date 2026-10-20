"""38. Squares of Even Numbers in a Range

Python practice program 38 of 100.
"""

n = int(input("Enter N: "))
for number in range(1, n + 1):
    if number % 2 == 0:
        print(number, "square =", number * number)
