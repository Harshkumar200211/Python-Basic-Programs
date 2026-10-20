"""88. Check Whether Two Strings Are Anagrams

Python practice program 88 of 100.
"""

first = input("Enter first word: ").replace(" ", "").lower()
second = input("Enter second word: ").replace(" ", "").lower()
if sorted(first) == sorted(second):
    print("Anagrams")
else:
    print("Not anagrams")
