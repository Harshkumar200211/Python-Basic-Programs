"""41. Inverted Star Triangle

Python practice program 41 of 100.
"""

rows = int(input("Enter number of rows: "))
for row in range(rows, 0, -1):
    print("*" * row)
