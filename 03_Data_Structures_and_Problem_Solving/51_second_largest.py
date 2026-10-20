"""51. Find the Second Largest Distinct Value

Python practice program 51 of 100.
"""

numbers = [10, 40, 20, 40, 30]
unique_numbers = sorted(set(numbers), reverse=True)
if len(unique_numbers) >= 2:
    print("Second largest =", unique_numbers[1])
else:
    print("Second distinct value does not exist")
