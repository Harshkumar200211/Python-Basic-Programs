"""16. Check Vowel or Consonant

Python practice program 16 of 100.
"""

letter = input("Enter one alphabet: ").lower()
if len(letter) != 1 or not letter.isalpha():
    print("Enter one alphabet only")
elif letter in "aeiou":
    print("Vowel")
else:
    print("Consonant")
