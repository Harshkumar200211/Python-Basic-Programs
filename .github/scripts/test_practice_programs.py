"""Run each numbered practice program with sample input and check its output.

These are smoke tests, not exhaustive proofs of correctness. File-writing
examples run in temporary working directories so generated files stay isolated.
Run from any directory:
    python .github/scripts/test_practice_programs.py
"""

from __future__ import annotations

import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PRACTICE_DIRS = [
    ROOT / "01_Basics",
    ROOT / "02_Control_Flow_and_Loops",
    ROOT / "03_Data_Structures_and_Problem_Solving",
    ROOT / "04_Functions_OOP_Files",
    ROOT / "05_Modules_and_Standard_Library",
    ROOT / "06_Advanced_Practice",
]

# Program number: (stdin text, required output fragment).
SAMPLES: dict[int, tuple[str, str]] = {
    1: ("", "Hello, World!"),
    2: ("", "Name: Harsh"),
    3: ("Harsh\n", "Hello, Harsh"),
    4: ("2\n3\n", "Sum = 5"),
    5: ("2\n3\n", "Addition: 5.0"),
    6: ("5\n4\n", "Area = 20.0"),
    7: ("2\n", "Area ="),
    8: ("0\n", "Fahrenheit = 32.0"),
    9: ("2\n3\n", "After: 3 2"),
    10: ("7\n3\n", "Quotient: 2"),
    11: ("2\n", "Even number"),
    12: ("-1\n", "Negative"),
    13: ("1\n2\n", "Largest = 2"),
    14: ("1\n2\n3\n", "Largest = 3"),
    15: ("2024\n", "Leap year"),
    16: ("a\n", "Vowel"),
    17: ("20\n", "Eligible to vote"),
    18: ("90\n", "Grade A"),
    19: ("55\n", "Divisible by both 5 and 11"),
    20: ("5\n+\n3\n", "Result: 8.0"),
    21: ("5\n", "5\n"),
    22: ("10\n", "10\n"),
    23: ("5\n", "Sum = 15"),
    24: ("5\n", "Factorial = 120"),
    25: ("5\n", "5 x 10 = 50"),
    26: ("123\n", "Digits = 3"),
    27: ("123\n", "Sum of digits = 6"),
    28: ("123\n", "Reversed = 321"),
    29: ("121\n", "Palindrome number"),
    30: ("7\n", "Prime number"),
    31: ("10\n", "7\n"),
    32: ("5\n", "0 1 1 2 3"),
    33: ("12\n8\n", "GCD = 4"),
    34: ("12\n8\n", "LCM = 24"),
    35: ("153\n", "Armstrong number"),
    36: ("6\n", "Perfect number"),
    37: ("10\n", "9\n"),
    38: ("6\n", "6 square = 36"),
    39: ("6\n", "Sum of squares = 56"),
    40: ("3\n", "***"),
    41: ("3\n", "***"),
    42: ("3\n", "1 2 3"),
    43: ("", "25"),
    44: ("", "First multiple of 7: 7"),
    45: ("", "20"),
    46: ("", "Sum = 150"),
    47: ("", "Largest = 89"),
    48: ("", "Smallest = 7"),
    49: ("", "Even count = 3"),
    50: ("", "Squares: [1, 4, 9, 16, 25]"),
    51: ("", "Second largest = 30"),
    52: ("", "Without duplicates: [1, 2, 3, 4]"),
    53: ("22\n", "Found at index: 2"),
    54: ("", "Sorted: [1, 2, 4, 5, 8]"),
    55: ("", "Reversed: [50, 40, 30, 20, 10]"),
    56: ("", "Rotated: [5, 1, 2, 3, 4]"),
    57: ("hello\n", "l : 2"),
    58: ("hello\n", "Vowels = 2"),
    59: ("Never odd or even\n", "Palindrome"),
    60: ("hello world\n", "world hello"),
    61: ("hello world\n", "Word count = 2"),
    62: ("", "Class average = 83.0"),
    63: ("", "'course': 'Python'"),
    64: ("", "[6, 8]"),
    65: ("", "[1, 4]"),
    66: ("", "Sum = 30"),
    67: ("2\n", "Even"),
    68: ("5\n", "Factorial = 120"),
    69: ("5\n", "0 1 1 2 3"),
    70: ("", "25"),
    71: ("", "[1, 4, 9, 16, 25]"),
    72: ("", "[2, 4, 6, 8]"),
    73: ("", "[1, 8, 27, 64, 125]"),
    74: ("", "60"),
    75: ("", "course : Python"),
    76: ("", "Result: Pass"),
    77: ("", "Roll number: 101"),
    78: ("", "Aman balance: 1500"),
    79: ("", "Perimeter: 30"),
    80: ("1\n0\n", "Cannot divide by zero"),
    81: ("22\n", "Next year you will be 23"),
    82: ("", "Practice a little every day."),
    83: ("", "Lines: 2"),
    84: ("", "['Riya', '92']"),
    85: ("", "Date:"),
    86: ("9\n2\n", "Square root: 3.0"),
    87: ("", "Dice roll:"),
    88: ("", "Mean:"),
    89: ("2027-01-01\n", "Days until event:"),
    90: ("2026\n10\n", "October 2026"),
    91: ("", "Current working directory:"),
    92: ("", "Python version:"),
    93: ("", "Student name: Riya"),
    94: ("Meeting 2026 with test@example.com\n", "Numbers found: ['2026']"),
    95: ("Python is fun Python\n", "python : 2"),
    96: ("".join(f"{number}\n" for number in range(1, 11)), "Correct! You guessed it."),
    97: ("GoodPass1!\n", "Meets the basic strength checks"),
    98: ("1\nHarsh\n9876543210\n2\n4\n", "Goodbye"),
    99: ("", "Total spent: Rs. 850"),
    100: ("", "Top student: Riya"),
    101: ("", "Values: 2 7"),
    102: ("", "FizzBuzz"),
    103: ("listen\nsilent\n", "Anagrams"),
    104: ("", "Most common value: 3"),
    105: ("", "Merged list: [1, 2, 3, 4, 7, 8, 10, 11]"),
    106: ("", "Main diagonal sum = 15"),
    107: ("25\n", "Found at index: 4"),
    108: ("", "Sorted list: [10, 13, 14, 29, 37]"),
    109: ("", "python : 3"),
    110: ("test@example.com\n", "Email format looks valid"),
}


def discover_programs() -> dict[int, Path]:
    programs: dict[int, Path] = {}
    for folder in PRACTICE_DIRS:
        for path in folder.glob("*.py"):
            match = re.match(r"^(\d{2,3})_", path.name)
            if not match:
                continue
            number = int(match.group(1))
            if number in programs:
                raise AssertionError(f"Duplicate practice program number: {number}")
            programs[number] = path

    expected_numbers = set(range(1, 111))
    actual_numbers = set(programs)
    if actual_numbers != expected_numbers:
        missing = sorted(expected_numbers - actual_numbers)
        extra = sorted(actual_numbers - expected_numbers)
        raise AssertionError(f"Practice program index mismatch. Missing={missing}, extra={extra}")
    if set(SAMPLES) != expected_numbers:
        missing = sorted(expected_numbers - set(SAMPLES))
        extra = sorted(set(SAMPLES) - expected_numbers)
        raise AssertionError(f"Sample-test index mismatch. Missing={missing}, extra={extra}")
    return programs


def main() -> int:
    programs = discover_programs()
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    failures: list[str] = []

    for number in range(1, 111):
        path = programs[number]
        input_text, expected_fragment = SAMPLES[number]
        try:
            with tempfile.TemporaryDirectory(prefix=f"python-practice-{number:03d}-") as temp_dir:
                result = subprocess.run(
                    [sys.executable, str(path)],
                    cwd=temp_dir,
                    input=input_text,
                    text=True,
                    capture_output=True,
                    timeout=8,
                    env=env,
                    check=False,
                )
            output = result.stdout + result.stderr
            if result.returncode != 0:
                failures.append(
                    f"Program {number:03d} ({path.relative_to(ROOT)}): "
                    f"exit code {result.returncode}\n{output}"
                )
            elif expected_fragment not in result.stdout:
                failures.append(
                    f"Program {number:03d} ({path.relative_to(ROOT)}): "
                    f"expected {expected_fragment!r} in stdout\n{output}"
                )
            else:
                print(f"PASS: {number:03d} {path.relative_to(ROOT)}")
        except subprocess.TimeoutExpired as exc:
            failures.append(f"Program {number:03d} timed out: {path.relative_to(ROOT)}")
        except Exception as exc:  # Show an actionable report for unexpected test-runner errors.
            failures.append(f"Program {number:03d} test runner error: {exc}")

    print(f"\nTested {len(programs)} numbered practice programs.")
    if failures:
        print(f"FAILED: {len(failures)} program(s)")
        for failure in failures:
            print(f"\n{failure}")
        return 1
    print("All 110 practice programs passed their sample-input smoke tests.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
