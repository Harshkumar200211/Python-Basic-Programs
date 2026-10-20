"""76. Create a Student Class

Python practice program 76 of 100.
"""

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show_result(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
        if self.marks >= 40:
            print("Result: Pass")
        else:
            print("Result: Fail")

student = Student("Rahul", 75)
student.show_result()
