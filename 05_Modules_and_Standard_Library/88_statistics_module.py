"""88. Calculate statistics with the statistics module."""

import statistics

marks = [72, 85, 90, 85, 68, 95, 85]

print("Marks:", marks)
print("Mean:", statistics.mean(marks))
print("Median:", statistics.median(marks))
print("Mode:", statistics.mode(marks))
print("Population standard deviation:", round(statistics.pstdev(marks), 2))
