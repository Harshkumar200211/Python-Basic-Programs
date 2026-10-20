"""90. Display a calendar with the calendar module."""

import calendar

year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))

if 1 <= month <= 12:
    print(calendar.month(year, month))
else:
    print("Month must be between 1 and 12")
