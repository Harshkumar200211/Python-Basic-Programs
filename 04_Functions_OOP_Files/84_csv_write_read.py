"""84. Write and Read a CSV File

Python practice program 84 of 100.
"""

import csv

students = [["Name", "Marks"], ["Aman", 85], ["Riya", 92], ["Kabir", 78]]
with open("students.csv", "w", newline="", encoding="utf-8") as file:
    csv.writer(file).writerows(students)

with open("students.csv", "r", newline="", encoding="utf-8") as file:
    for row in csv.reader(file):
        print(row)
