"""110. Simple Email Format Check."""

email = input("Enter email address: ").strip()

if " " not in email and email.count("@") == 1:
    name, domain = email.split("@")
    if name and "." in domain and not domain.startswith(".") and not domain.endswith("."):
        print("Email format looks valid")
    else:
        print("Invalid email format")
else:
    print("Invalid email format")
