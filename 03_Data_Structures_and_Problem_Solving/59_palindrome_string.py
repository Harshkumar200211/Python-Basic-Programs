"""59. Check Palindrome String

Python practice program 59 of 100.
"""

text = input("Enter text: ").lower().replace(" ", "")
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
