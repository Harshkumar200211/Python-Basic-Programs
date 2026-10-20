"""97. Basic Password Strength Checker

An educational demonstration, not a complete security audit.
"""

password = input("Enter a password to check: ")
has_number = any(char.isdigit() for char in password)
has_letter = any(char.isalpha() for char in password)
has_special = any(not char.isalnum() for char in password)
if len(password) >= 8 and has_number and has_letter and has_special:
    print("Meets the basic strength checks")
else:
    print("Use 8+ characters with letters, numbers and a symbol")
