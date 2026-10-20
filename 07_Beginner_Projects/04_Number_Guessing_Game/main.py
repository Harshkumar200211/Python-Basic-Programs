"""Project 4: Number Guessing Game
Concepts: random module, loops, conditions and input validation.
"""

import random


def main():
    secret_number = random.randint(1, 20)
    maximum_attempts = 6
    print("I have selected a number from 1 to 20.")
    print(f"You have {maximum_attempts} attempts to guess it.")

    for attempt in range(1, maximum_attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}: "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        if not 1 <= guess <= 20:
            print("Choose a number between 1 and 20.")
            continue

        if guess == secret_number:
            print(f"Correct! You guessed it in {attempt} attempt(s).")
            break
        if guess < secret_number:
            print("Too low. Try a higher number.")
        else:
            print("Too high. Try a lower number.")
    else:
        print(f"No attempts left. The number was {secret_number}.")


if __name__ == "__main__":
    main()
