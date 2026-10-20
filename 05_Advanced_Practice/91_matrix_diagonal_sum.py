"""91. Sum of Main Diagonal in a Matrix

Python practice program 91 of 100.
"""

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
total = 0
for i in range(len(matrix)):
    total += matrix[i][i]
print("Main diagonal sum =", total)
