# Project: Student Record Manager

## What this project does

Add, view, search and delete student records using roll numbers.

## Python concepts used

Dictionaries, functions, loops, JSON, pathlib and exception handling.

## How it works, step by step

1. Load students.json if it exists; otherwise begin with an empty dictionary.
2. Add a unique roll number, name and marks.
3. List all records or search by roll number.
4. Delete a selected record.
5. Save each change to JSON so it is available after restart.

## Files used

- main.py — record operations. students.json

## How to run

1. Install Python 3.
2. Open this project folder in a terminal.
3. Run:

```bash
python main.py
```

On some systems, use `python3 main.py`.

## Learning note

The JSON data file is created beside main.py. Use sample student data in class exercises.

First run the project with sample data. Then trace how records change when you add, search, update or delete information.
