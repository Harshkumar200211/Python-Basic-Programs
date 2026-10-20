"""Smoke-test the 15 console projects using sample input.

Run from the repository root:
    python .github/scripts/smoke_test_projects.py
"""

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROJECTS = ROOT / "07_Beginner_Projects"

CASES = [
    ("01_Menu_Driven_Calculator", "1\n3\n4\n5\n", "Result: 7.0"),
    ("02_Student_Grade_Calculator", "Harsh\n90\n80\n70\n", "Grade: A"),
    ("03_MCQ_Quiz_App", "b\nc\nb\nb\na\n", "Score: 5/5"),
    ("04_Number_Guessing_Game", "invalid\n" * 6, "No attempts left."),
    ("05_Unit_Converter", "1\n10\n7\n", "6.21 miles"),
    ("06_Student_Record_Manager", "1\nT101\nTest Student\n80\n2\n5\n", "Student saved."),
    ("07_Attendance_Manager", "1\nTest Student, Another Student\nP\nA\n4\n", "Attendance saved for"),
    ("08_Contact_Book", "1\nTest Contact\n9876543210\ntest@example.com\n5\n", "Contact saved."),
    ("09_Expense_Tracker", "1\nFood\nLunch\n125\n3\n4\n", "Total spent: Rs. 125.00"),
    ("10_Library_Management_System", "1\nTBOOK1\nPython Basics\nSample Author\n3\nTBOOK1\nTest Student\n4\nTBOOK1\n5\n", "Book returned."),
    ("11_Inventory_Billing_System", "2\nP101\n2\n0\n3\n", "Grand total:"),
    ("12_Custom_Modules_Calculator", "1\n10\n5\n7\n", "Result: 15"),
    ("13_Custom_Package_Student_Manager", "T101\nTest Student\n90\n80\n70\n", "Result: Pass"),
    ("14_Calendar_Attendance_Planner", "1\n2026\n10\n4\n", "Days in month: 31"),
    ("15_Text_File_Analyzer", "\n", "Words:"),
]


def run_case(folder_name: str, input_text: str, expected_text: str) -> None:
    project_folder = PROJECTS / folder_name
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    result = subprocess.run(
        [sys.executable, "main.py"],
        cwd=project_folder,
        input=input_text,
        text=True,
        capture_output=True,
        timeout=15,
        env=env,
        check=False,
    )
    combined_output = result.stdout + result.stderr
    if result.returncode != 0:
        raise AssertionError(
            f"{folder_name} exited with code {result.returncode}.\n"
            f"STDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
        )
    if expected_text not in combined_output:
        raise AssertionError(
            f"{folder_name} did not produce expected text {expected_text!r}.\n"
            f"Output:\n{combined_output}"
        )
    print(f"PASS: {folder_name}")


def main() -> None:
    for folder_name, input_text, expected_text in CASES:
        run_case(folder_name, input_text, expected_text)
    print(f"\nAll {len(CASES)} console projects passed their smoke tests.")


if __name__ == "__main__":
    main()
