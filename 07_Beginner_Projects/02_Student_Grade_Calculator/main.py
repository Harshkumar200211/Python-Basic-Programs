"""Project 2: Student Marks and Grade Calculator
Concepts: input, lists, loops, arithmetic and conditions.
"""

def read_marks(subject):
    while True:
        try:
            marks = float(input(f"Enter marks for {subject} (0-100): "))
            if 0 <= marks <= 100:
                return marks
            print("Marks must be between 0 and 100.")
        except ValueError:
            print("Please enter a number.")


def main():
    name = input("Enter student name: ").strip()
    if not name:
        name = "Student"

    subjects = ["Python", "Mathematics", "Computer Fundamentals"]
    marks = []

    for subject in subjects:
        marks.append(read_marks(subject))

    total = sum(marks)
    percentage = total / len(subjects)
    passed_all = all(mark >= 33 for mark in marks)

    if not passed_all:
        grade = "F (Fail)"
    elif percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "F (Fail)"

    print("\n=== STUDENT RESULT ===")
    print("Name:", name)
    for subject, mark in zip(subjects, marks):
        print(f"{subject}: {mark:g}")
    print(f"Total: {total:g} / {len(subjects) * 100}")
    print(f"Percentage: {percentage:.2f}%")
    print("Result:", "Pass" if passed_all and percentage >= 40 else "Fail")
    print("Grade:", grade)


if __name__ == "__main__":
    main()
