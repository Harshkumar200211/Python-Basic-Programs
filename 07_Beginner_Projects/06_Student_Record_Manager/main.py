"""Project 6: Student Record Manager
Stores student records in a JSON file beside this script.
Concepts: dictionaries, functions, JSON, loops and validation.
"""

import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("students.json")


def load_students():
    if not DATA_FILE.exists():
        return {}
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
        return data if isinstance(data, dict) else {}
    except (json.JSONDecodeError, OSError):
        print("Could not read students.json. Starting with an empty record.")
        return {}


def save_students(students):
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(students, file, indent=4, ensure_ascii=False)


def read_marks():
    while True:
        try:
            marks = float(input("Enter marks out of 100: "))
            if 0 <= marks <= 100:
                return marks
            print("Marks must be between 0 and 100.")
        except ValueError:
            print("Please enter a number.")


def main():
    students = load_students()
    while True:
        print("\n=== STUDENT RECORD MANAGER ===")
        print("1. Add student")
        print("2. View all students")
        print("3. Search by roll number")
        print("4. Delete student")
        print("5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            roll = input("Roll number: ").strip()
            name = input("Student name: ").strip()
            if not roll or not name:
                print("Roll number and name cannot be empty.")
                continue
            if roll in students:
                print("This roll number already exists.")
                continue
            students[roll] = {"name": name, "marks": read_marks()}
            save_students(students)
            print("Student saved.")
        elif choice == "2":
            if not students:
                print("No student records yet.")
            else:
                for roll, student in sorted(students.items()):
                    print(f"{roll} | {student['name']} | Marks: {student['marks']}")
        elif choice == "3":
            roll = input("Enter roll number: ").strip()
            student = students.get(roll)
            if student:
                print("Roll:", roll, "| Name:", student["name"], "| Marks:", student["marks"])
            else:
                print("Student not found.")
        elif choice == "4":
            roll = input("Roll number to delete: ").strip()
            if roll in students:
                del students[roll]
                save_students(students)
                print("Record deleted.")
            else:
                print("Student not found.")
        elif choice == "5":
            print("Records saved. Goodbye.")
            break
        else:
            print("Choose an option from 1 to 5.")


if __name__ == "__main__":
    main()
