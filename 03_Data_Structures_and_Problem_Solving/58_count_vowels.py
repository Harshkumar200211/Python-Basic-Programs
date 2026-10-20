"""58. Count Vowels in a String

Python practice program 58 of 100.
"""

text = input("Enter text: ").lower()
count = 0
for character in text:
    if character in "aeiou":
        count += 1
print("Vowels =", count)
