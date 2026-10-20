"""Project 14: Calendar and Attendance Planner
Saves reminders in planner_events.json beside this script.
Concepts: calendar, datetime, JSON, dictionaries and validation.
"""

import calendar
import json
from datetime import date
from pathlib import Path

DATA_FILE = Path(__file__).with_name("planner_events.json")


def load_events():
    if not DATA_FILE.exists():
        return {}
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
        return data if isinstance(data, dict) else {}
    except (json.JSONDecodeError, OSError):
        print("Could not read planner data. Starting with an empty planner.")
        return {}


def save_events(events):
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(events, file, indent=4, ensure_ascii=False)


def read_year_month():
    try:
        year = int(input("Enter year (e.g. 2026): "))
        month = int(input("Enter month (1-12): "))
        if year < 1 or not 1 <= month <= 12:
            raise ValueError
        return year, month
    except ValueError:
        print("Please enter a valid year and a month from 1 to 12.")
        return None


def show_calendar(events):
    selection = read_year_month()
    if selection is None:
        return
    year, month = selection
    print(calendar.month(year, month))
    print("Days in month:", calendar.monthrange(year, month)[1])
    prefix = f"{year:04d}-{month:02d}-"
    month_events = [(event_date, note) for event_date, note in events.items()
                    if event_date.startswith(prefix)]
    if month_events:
        print("Planned events:")
        for event_date, note in sorted(month_events):
            print(f"{event_date}: {note}")
    else:
        print("No events planned for this month.")


def add_event(events):
    event_date = input("Enter event date (YYYY-MM-DD): ").strip()
    try:
        date.fromisoformat(event_date)
    except ValueError:
        print("Invalid date. Use YYYY-MM-DD.")
        return
    note = input("Enter event or attendance note: ").strip()
    if not note:
        print("Event note cannot be empty.")
        return
    events[event_date] = note
    save_events(events)
    print("Event saved.")


def main():
    events = load_events()
    while True:
        print("\n=== CALENDAR AND ATTENDANCE PLANNER ===")
        print("1. Show a monthly calendar")
        print("2. Add or update an event")
        print("3. View all planned events")
        print("4. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            show_calendar(events)
        elif choice == "2":
            add_event(events)
        elif choice == "3":
            if not events:
                print("No events planned.")
            for event_date, note in sorted(events.items()):
                print(f"{event_date}: {note}")
        elif choice == "4":
            print("Planner closed.")
            break
        else:
            print("Choose 1, 2, 3 or 4.")


if __name__ == "__main__":
    main()
