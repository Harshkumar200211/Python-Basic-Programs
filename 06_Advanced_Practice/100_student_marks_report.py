"""100. Mini Project: Student Marks Report

Calculate totals, averages and the top-performing student.
"""

students = [
    {"name": "Aman", "marks": [80, 75, 90]},
    {"name": "Riya", "marks": [92, 88, 95]},
    {"name": "Kabir", "marks": [65, 70, 72]}
]
topper = students[0]
print("STUDENT REPORT")
for student in students:
    total = sum(student["marks"])
    average = total / len(student["marks"])
    print(student["name"], "| Total:", total, "| Average:", round(average, 2))
    if total > sum(topper["marks"]):
        topper = student
print("Top student:", topper["name"])
print("Top total:", sum(topper["marks"]))
