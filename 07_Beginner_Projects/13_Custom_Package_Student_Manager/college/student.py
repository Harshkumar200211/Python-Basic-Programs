"""Student data model for the college package."""


class Student:
    def __init__(self, roll_number, name, marks):
        self.roll_number = roll_number
        self.name = name
        self.marks = marks

    def show_details(self):
        print("Roll number:", self.roll_number)
        print("Name:", self.name)
        for subject, mark in self.marks.items():
            print(f"{subject}: {mark:g}")
