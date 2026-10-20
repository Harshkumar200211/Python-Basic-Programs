"""62. Student Marks and Average Using Dictionary

Python practice program 62 of 100.
"""

marks = {"Aman": 82, "Riya": 91, "Kabir": 76}
for name, score in marks.items():
    print(name, ":", score)
average = sum(marks.values()) / len(marks)
print("Class average =", round(average, 2))
