"""Project 7: Daily Attendance Manager
Saves daily attendance in attendance_data.json beside this script.
Concepts: dates, dictionaries, lists, JSON and summary calculations.
"""

import json
from datetime import date
from pathlib import Path

DATA_FILE = Path(__file__).with_name("attendance_data.json")


def load_data():
    if not DATA_FILE.exists():
        return {}
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
        return data if isinstance(data, dict) else {}
    except (json.JSONDecodeError, OSError):
        print("Could not read attendance data. Starting with an empty record.")
        return {}


def save_data(data):
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def mark_today(data):
    today = date.today().isoformat()
    names_text = input("Enter student names separated by commas: ")
    names = list(dict.fromkeys(name.strip() for name in names_text.split(",") if name.strip()))
    if not names:
        print("No student names entered.")
        return

    day_record = data.setdefault(today, {})
    for name in names:
        while True:
            status = input(f"{name} - Present (P), Absent (A), Leave (L): ").strip().upper()
            if status in {"P", "A", "L"}:
                day_record[name] = {"P": "Present", "A": "Absent", "L": "Leave"}[status]
                break
            print("Enter P, A or L.")
    save_data(data)
    print(f"Attendance saved for {today}.")


def view_date(data):
    chosen_date = input("Enter date (YYYY-MM-DD): ").strip()
    record = data.get(chosen_date)
    if not record:
        print("No attendance records found for this date.")
        return
    print(f"\nAttendance for {chosen_date}")
    for name, status in sorted(record.items()):
        print(f"{name}: {status}")


def show_summary(data):
    summary = {}
    for day_record in data.values():
        for name, status in day_record.items():
            counts = summary.setdefault(name, {"Present": 0, "Absent": 0, "Leave": 0})
            if status in counts:
                counts[status] += 1

    if not summary:
        print("No attendance records yet.")
        return
    print("\n=== ATTENDANCE SUMMARY ===")
    for name, counts in sorted(summary.items()):
        working_days = counts["Present"] + counts["Absent"]
        percentage = counts["Present"] / working_days * 100 if working_days else 0
        print(f"{name}: Present {counts['Present']}, Absent {counts['Absent']}, "
              f"Leave {counts['Leave']}, Attendance {percentage:.1f}%")


def main():
    data = load_data()
    while True:
        print("\n=== DAILY ATTENDANCE MANAGER ===")
        print("1. Mark today's attendance")
        print("2. View attendance by date")
        print("3. View summary")
        print("4. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            mark_today(data)
        elif choice == "2":
            view_date(data)
        elif choice == "3":
            show_summary(data)
        elif choice == "4":
            print("Goodbye.")
            break
        else:
            print("Choose 1, 2, 3 or 4.")


if __name__ == "__main__":
    main()
