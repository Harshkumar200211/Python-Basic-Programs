"""10. Quotient and Remainder

Python practice program 10 of 100.
"""

a = int(input("Enter dividend: "))
b = int(input("Enter divisor: "))
if b != 0:
    print("Quotient:", a // b)
    print("Remainder:", a % b)
else:
    print("Divisor cannot be zero")
