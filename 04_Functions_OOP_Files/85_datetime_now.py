"""85. Display Current Date and Time

Python practice program 85 of 100.
"""

from datetime import datetime

now = datetime.now()
print("Date:", now.strftime("%d-%m-%Y"))
print("Time:", now.strftime("%H:%M:%S"))
