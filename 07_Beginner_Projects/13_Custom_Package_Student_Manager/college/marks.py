"""Functions for student result calculation."""


def calculate_result(marks):
    if not marks:
        raise ValueError("At least one subject mark is required.")
    if any(mark < 0 or mark > 100 for mark in marks.values()):
        raise ValueError("Each mark must be between 0 and 100.")

    total = sum(marks.values())
    percentage = total / len(marks)
    passed_all = all(mark >= 33 for mark in marks.values())

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

    return {
        "total": total,
        "percentage": percentage,
        "result": "Pass" if passed_all and percentage >= 40 else "Fail",
        "grade": grade,
    }
