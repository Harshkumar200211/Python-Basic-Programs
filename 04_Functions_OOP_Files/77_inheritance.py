"""77. Inheritance with Person and Student

Python practice program 77 of 100.
"""

class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("Name:", self.name)

class Student(Person):
    def __init__(self, name, roll_number):
        super().__init__(name)
        self.roll_number = roll_number

    def show_details(self):
        self.show_name()
        print("Roll number:", self.roll_number)

Student("Riya", 101).show_details()
