"""63. Merge Two Dictionaries

Python practice program 63 of 100.
"""

first = {"name": "Aman", "age": 20}
second = {"course": "Python", "city": "Kanpur"}
combined = first.copy()
combined.update(second)
print(combined)
