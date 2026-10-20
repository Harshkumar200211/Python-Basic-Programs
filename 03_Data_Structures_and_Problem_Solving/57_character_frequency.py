"""57. Character Frequency in a String

Python practice program 57 of 100.
"""

text = input("Enter text: ")
frequency = {}
for character in text:
    if character != " ":
        frequency[character] = frequency.get(character, 0) + 1
for character, count in frequency.items():
    print(character, ":", count)
