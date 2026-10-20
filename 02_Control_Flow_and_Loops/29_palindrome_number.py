"""29. Check Palindrome Number

Python practice program 29 of 100.
"""

number = int(input("Enter a non-negative integer: "))
original = number
reverse = 0
while number > 0:
    reverse = reverse * 10 + number % 10
    number //= 10
if original == reverse:
    print("Palindrome number")
else:
    print("Not a palindrome")
