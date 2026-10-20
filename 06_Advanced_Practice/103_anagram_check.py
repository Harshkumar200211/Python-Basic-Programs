"""103. Check Whether Two Strings Are Anagrams."""

first = input("Enter first word: ").replace(" ", "").lower()
second = input("Enter second word: ").replace(" ", "").lower()

if sorted(first) == sorted(second):
    print("Anagrams")
else:
    print("Not anagrams")
