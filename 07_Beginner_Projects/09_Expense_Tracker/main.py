"""Project 9: Personal Expense Tracker
Stores expenses in expenses.json beside this script.
Concepts: lists, dictionaries, dates, JSON and aggregation.
"""

import json
from datetime import date
from pathlib import Path

DATA_FILE = Path(__file__).with_name("expenses.json")


def load_expenses():
    if not DATA_FILE.exists():
        return []
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        print("Could not read expenses.json. Starting with an empty list.")
        return []


def save_expenses(expenses):
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4, ensure_ascii=False)


def add_expense(expenses):
    category = input("Category (Food, Travel, Books, etc.): ").strip()
    if not category:
        print("Category cannot be empty.")
        return
    description = input("Short description: ").strip()
    while True:
        try:
            amount = float(input("Amount in Rs.: "))
            if amount > 0:
                break
            print("Amount must be greater than zero.")
        except ValueError:
            print("Enter a valid amount.")

    expenses.append({
        "date": date.today().isoformat(),
        "category": category,
        "description": description,
        "amount": round(amount, 2),
    })
    save_expenses(expenses)
    print("Expense saved.")


def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return
    print("\nNo. | Date | Category | Description | Amount")
    for number, item in enumerate(expenses, start=1):
        print(f"{number}. {item['date']} | {item['category']} | "
              f"{item['description']} | Rs. {item['amount']:.2f}")


def show_summary(expenses):
    if not expenses:
        print("No expenses to summarize.")
        return
    totals = {}
    for item in expenses:
        totals[item["category"]] = totals.get(item["category"], 0) + item["amount"]
    grand_total = sum(item["amount"] for item in expenses)
    print(f"Total spent: Rs. {grand_total:.2f}")
    print("Category-wise spending:")
    for category, amount in sorted(totals.items()):
        print(f"{category}: Rs. {amount:.2f}")


def main():
    expenses = load_expenses()
    while True:
        print("\n=== EXPENSE TRACKER ===")
        print("1. Add expense")
        print("2. View all expenses")
        print("3. View summary")
        print("4. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            show_summary(expenses)
        elif choice == "4":
            print("Expenses saved. Goodbye.")
            break
        else:
            print("Choose 1, 2, 3 or 4.")


if __name__ == "__main__":
    main()
