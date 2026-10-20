"""39. Sum of Squares of Even Numbers

Python practice program 39 of 100.
"""

n = int(input("Enter N: "))
total = 0
for number in range(1, n + 1):
    if number % 2 == 0:
        square = number * number
        print(number, "square =", square)
        total += square
print("Sum of squares =", total)
