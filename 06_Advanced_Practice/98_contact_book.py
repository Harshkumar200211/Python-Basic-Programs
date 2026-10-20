"""98. Mini Project: Contact Book

Contacts are stored in a dictionary while the program runs.
"""

contacts = {}
while True:
    print("\n1. Add contact\n2. View contacts\n3. Search contact\n4. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        name = input("Name: ").strip()
        phone = input("Phone: ").strip()
        contacts[name] = phone
        print("Contact saved")
    elif choice == "2":
        if contacts:
            for name, phone in contacts.items():
                print(name, ":", phone)
        else:
            print("No contacts saved")
    elif choice == "3":
        name = input("Name to search: ").strip()
        print(contacts.get(name, "Contact not found"))
    elif choice == "4":
        print("Goodbye")
        break
    else:
        print("Choose 1, 2, 3 or 4")
