"""94. Find patterns in text with the re module."""

import re

text = input("Enter text containing numbers and email-like text: ")
numbers = re.findall(r"\d+", text)
emails = re.findall(r"[\w.-]+@[\w.-]+\.\w+", text)

print("Numbers found:", numbers)
print("Email-like values found:", emails)

cleaned_text = re.sub(r"\s+", " ", text).strip()
print("Cleaned text:", cleaned_text)
