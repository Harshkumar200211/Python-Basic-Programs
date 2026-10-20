"""Project 13: Student Manager Using a Custom Package
Run from this folder: python main.py
Concepts: packages, __init__.py, imports, classes and functions.
"""

from college import Student, calculate_result


def read_marks(subject):
    while True:
        try:
            mark = float(input(f"Enter marks for {subject} (0-100): "))
            if 0 <= mark <= 100:
                return mark
            print("Marks must be between 0 and 100.")
        except ValueError:
            print("Enter a valid number.")


def main():
    roll_number = input("Enter roll number: ").strip()
    name = input("Enter student name: ").strip()
    if not roll_number or not name:
        print("Roll number and name are required.")
        return

    marks = {
        "Python": read_marks("Python"),
        "Mathematics": read_marks("Mathematics"),
        "Computer Fundamentals": read_marks("Computer Fundamentals"),
    }
    student = Student(roll_number, name, marks)
    result = calculate_result(marks)

    print("\n=== STUDENT REPORT ===")
    student.show_details()
    print(f"Total: {result['total']:g} / {len(marks) * 100}")
    print(f"Percentage: {result['percentage']:.2f}%")
    print("Result:", result["result"])
    print("Grade:", result["grade"])


if __name__ == "__main__":
    main()
