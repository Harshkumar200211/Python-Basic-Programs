"""99. Mini Project: Expense Tracker

Summarize expenses by category using a list of dictionaries.
"""

expenses = [
    {"category": "Food", "amount": 250},
    {"category": "Travel", "amount": 120},
    {"category": "Food", "amount": 180},
    {"category": "Books", "amount": 300}
]
total = 0
by_category = {}
for expense in expenses:
    category = expense["category"]
    amount = expense["amount"]
    total += amount
    by_category[category] = by_category.get(category, 0) + amount
print("Total spent: Rs.", total)
for category, amount in by_category.items():
    print(category, "- Rs.", amount)
