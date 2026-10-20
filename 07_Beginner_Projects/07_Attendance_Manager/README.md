# Project: Daily Attendance Manager

## What this project does

Record Present, Absent or Leave for a date and calculate a basic attendance summary.

## Python concepts used

date.today(), dictionaries, lists, JSON, loops and percentage calculations.

## How it works, step by step

1. Enter student names separated by commas.
2. Record P, A or L for each name.
3. Save date-wise records in attendance_data.json.
4. View attendance for a chosen date.
5. Summarize counts per student; the percentage uses Present / (Present + Absent), excluding Leave.

## Files used

- main.py — attendance menu and calculations. attendance_data.json

## How to run

1. Install Python 3.
2. Open this project folder in a terminal.
3. Run:

```bash
python main.py
```

On some systems, use `python3 main.py`.

## Learning note

This is a learning example, not an official attendance system. Official use would need authentication, backups and more validation.

First run the project with sample data. Then trace how records change when you add, search, update or delete information.
