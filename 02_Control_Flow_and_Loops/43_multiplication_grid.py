"""43. Multiplication Grid Using Nested Loops

Python practice program 43 of 100.
"""

for row in range(1, 6):
    for col in range(1, 6):
        print(row * col, end="\t")
    print()
