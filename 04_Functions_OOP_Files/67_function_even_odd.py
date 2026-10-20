"""67. Function to Check Even or Odd

Python practice program 67 of 100.
"""

def is_even(number):
    return number % 2 == 0

n = int(input("Enter a number: "))
if is_even(n):
    print("Even")
else:
    print("Odd")
