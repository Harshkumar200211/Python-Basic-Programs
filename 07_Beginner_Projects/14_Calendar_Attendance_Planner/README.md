# Project: Calendar and Attendance Planner

## What this project does

Display a monthly calendar and save dated event or attendance notes.

## Python concepts used

calendar module, datetime.date, JSON, dictionaries, loops and validation.

## How it works, step by step

1. Choose a year and month to display the calendar.
2. Use calendar.monthrange() to show the number of days.
3. Enter an event using YYYY-MM-DD format and validate the date.
4. Save or update its note in planner_events.json.
5. View all saved events in date order.

## Files used

- `main.py` — Calendar display and event operations.
- `planner_events.json` — Created automatically when the first event is saved.

## How to run

1. Install Python 3.
2. Open this project folder in a terminal.
3. Run:

```bash
python main.py
```

On some systems, use `python3 main.py`.

## Learning note

This planner stores dated notes only. It does not connect to college data or automatically mark student attendance.

After the first run, change some inputs and explain how the code uses each listed concept.
