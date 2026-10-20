"""96. Number Guessing Game

Python practice program 96 of 100.
"""

import random

secret = random.randint(1, 10)
print("Guess a number from 1 to 10.")
while True:
    try:
        guess = int(input("Your guess: "))
    except ValueError:
        print("Enter a whole number.")
        continue
    if guess == secret:
        print("Correct! You guessed it.")
        break
    elif guess < secret:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")
