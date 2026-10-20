"""83. Count Lines, Words and Characters in a File

Python practice program 83 of 100.
"""

# Create a sample file so this program works independently.
with open("sample.txt", "w", encoding="utf-8") as file:
    file.write("Learn Python\nPractice every day\n")

with open("sample.txt", "r", encoding="utf-8") as file:
    content = file.read()
print("Lines:", len(content.splitlines()))
print("Words:", len(content.split()))
print("Characters:", len(content))
