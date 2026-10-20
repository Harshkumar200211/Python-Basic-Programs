"""72. Use filter() to Get Even Numbers

Python practice program 72 of 100.
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda n: n % 2 == 0, numbers))
print(even_numbers)
