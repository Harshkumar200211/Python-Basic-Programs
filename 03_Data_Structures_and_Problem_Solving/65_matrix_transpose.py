"""65. Transpose a Matrix

Python practice program 65 of 100.
"""

matrix = [[1, 2, 3], [4, 5, 6]]
rows = len(matrix)
cols = len(matrix[0])
transpose = []
for col in range(cols):
    new_row = []
    for row in range(rows):
        new_row.append(matrix[row][col])
    transpose.append(new_row)
for row in transpose:
    print(row)
