"""82. Write and Read a Text File

Python practice program 82 of 100.
"""

# This creates notes.txt in the current folder.
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Python is easy to learn.\n")
    file.write("Practice a little every day.\n")

with open("notes.txt", "r", encoding="utf-8") as file:
    print(file.read())
