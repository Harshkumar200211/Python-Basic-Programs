"""106. Sum the Main Diagonal of a Matrix."""

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
total = 0

for i in range(len(matrix)):
    total += matrix[i][i]

print("Main diagonal sum =", total)
