# Project: Student Manager Using a Custom Package

## What this project does

Organize student details and result calculations into a reusable package named college.

## Python concepts used

Packages, __init__.py, imports, classes, methods, dictionaries and reusable functions.

## How it works, step by step

1. Create the college folder as a Python package.
2. Define the Student class in college/student.py.
3. Define total, percentage, pass/fail and grade logic in college/marks.py.
4. Export the class and function from college/__init__.py.
5. Import them in main.py and print the report.

## Files used

- `main.py` — Accepts input and displays the result.
- `college/__init__.py` — Exports Student and calculate_result.
- `college/student.py` — Defines the Student class.
- `college/marks.py` — Contains result calculation logic.

## How to run

1. Install Python 3.
2. Open this project folder in a terminal.
3. Run:

```bash
python main.py
```

On some systems, use `python3 main.py`.

## Learning note

Run python main.py from this project folder. Do not move main.py outside the project folder unless you also adjust the package path.

After the first run, change some inputs and explain how the code uses each listed concept.
