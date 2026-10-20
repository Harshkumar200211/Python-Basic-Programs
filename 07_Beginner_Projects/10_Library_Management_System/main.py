"""Project 10: Library Management System
Stores book records in library.json beside this script.
Concepts: dictionaries, functions, JSON, menus and simple status tracking.
"""

import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("library.json")


def load_books():
    if not DATA_FILE.exists():
        return {}
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
        return data if isinstance(data, dict) else {}
    except (json.JSONDecodeError, OSError):
        print("Could not read library.json. Starting with an empty library.")
        return {}


def save_books(books):
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(books, file, indent=4, ensure_ascii=False)


def main():
    books = load_books()
    while True:
        print("\n=== LIBRARY MANAGEMENT ===")
        print("1. Add a book")
        print("2. View all books")
        print("3. Issue a book")
        print("4. Return a book")
        print("5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            book_id = input("Book ID: ").strip()
            title = input("Book title: ").strip()
            author = input("Author: ").strip()
            if not book_id or not title:
                print("Book ID and title are required.")
            elif book_id in books:
                print("That Book ID already exists.")
            else:
                books[book_id] = {
                    "title": title,
                    "author": author,
                    "issued_to": "",
                }
                save_books(books)
                print("Book added.")
        elif choice == "2":
            if not books:
                print("No books in the library yet.")
            for book_id, book in sorted(books.items()):
                status = f"Issued to {book['issued_to']}" if book["issued_to"] else "Available"
                print(f"{book_id} | {book['title']} | {book['author']} | {status}")
        elif choice == "3":
            book_id = input("Book ID to issue: ").strip()
            if book_id not in books:
                print("Book not found.")
            elif books[book_id]["issued_to"]:
                print("This book is already issued.")
            else:
                borrower = input("Student name: ").strip()
                if borrower:
                    books[book_id]["issued_to"] = borrower
                    save_books(books)
                    print("Book issued.")
                else:
                    print("Student name cannot be empty.")
        elif choice == "4":
            book_id = input("Book ID to return: ").strip()
            if book_id not in books:
                print("Book not found.")
            elif not books[book_id]["issued_to"]:
                print("This book is already available.")
            else:
                books[book_id]["issued_to"] = ""
                save_books(books)
                print("Book returned.")
        elif choice == "5":
            print("Library records saved. Goodbye.")
            break
        else:
            print("Choose an option from 1 to 5.")


if __name__ == "__main__":
    main()
