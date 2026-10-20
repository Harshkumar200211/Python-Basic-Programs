"""19. Divisible by 5 and 11

Python practice program 19 of 100.
"""

number = int(input("Enter a number: "))
if number % 5 == 0 and number % 11 == 0:
    print("Divisible by both 5 and 11")
else:
    print("Not divisible by both")
