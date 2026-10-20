"""Project 8: Contact Book
Stores contacts in contacts.json beside this script.
Concepts: dictionaries, JSON, functions, input validation and CRUD operations.
"""

import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("contacts.json")


def load_contacts():
    if not DATA_FILE.exists():
        return {}
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
        return data if isinstance(data, dict) else {}
    except (json.JSONDecodeError, OSError):
        print("Could not read contacts.json. Starting with an empty contact book.")
        return {}


def save_contacts(contacts):
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(contacts, file, indent=4, ensure_ascii=False)


def main():
    contacts = load_contacts()
    while True:
        print("\n=== CONTACT BOOK ===")
        print("1. Add or update contact")
        print("2. View all contacts")
        print("3. Search contact")
        print("4. Delete contact")
        print("5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = input("Name: ").strip()
            phone = input("Phone number: ").strip()
            email = input("Email (optional): ").strip()
            if not name or not phone:
                print("Name and phone number are required.")
                continue
            contacts[name.casefold()] = {"name": name, "phone": phone, "email": email}
            save_contacts(contacts)
            print("Contact saved.")
        elif choice == "2":
            if not contacts:
                print("No contacts saved.")
            for contact in sorted(contacts.values(), key=lambda item: item["name"].casefold()):
                print(f"{contact['name']} | {contact['phone']} | {contact['email']}")
        elif choice == "3":
            name = input("Name to search: ").strip().casefold()
            contact = contacts.get(name)
            if contact:
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"] or "Not provided")
            else:
                print("Contact not found.")
        elif choice == "4":
            name = input("Name to delete: ").strip().casefold()
            if name in contacts:
                del contacts[name]
                save_contacts(contacts)
                print("Contact deleted.")
            else:
                print("Contact not found.")
        elif choice == "5":
            print("Contacts saved. Goodbye.")
            break
        else:
            print("Choose an option from 1 to 5.")


if __name__ == "__main__":
    main()
