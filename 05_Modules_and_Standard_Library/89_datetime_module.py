"""89. Work with dates using datetime."""

from datetime import date, datetime

today = date.today()
print("Today's date:", today.strftime("%d-%m-%Y"))
print("Current time:", datetime.now().strftime("%H:%M:%S"))

birthday_text = input("Enter your next event date (YYYY-MM-DD): ")
try:
    event_date = date.fromisoformat(birthday_text)
    difference = (event_date - today).days
    print("Days until event:", difference)
except ValueError:
    print("Please use the YYYY-MM-DD date format")
