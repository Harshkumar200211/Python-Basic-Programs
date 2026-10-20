"""64. Add Two 2 x 2 Matrices

Python practice program 64 of 100.
"""

a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]
result = [[0, 0], [0, 0]]
for row in range(2):
    for col in range(2):
        result[row][col] = a[row][col] + b[row][col]
for row in result:
    print(row)
