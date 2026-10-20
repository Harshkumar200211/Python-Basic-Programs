"""87. Generate random values with the random module."""

import random

print("Dice roll:", random.randint(1, 6))
print("Random decimal:", round(random.random(), 3))

names = ["Aman", "Riya", "Kabir", "Neha"]
print("Randomly selected name:", random.choice(names))
print("Three random numbers:", random.sample(range(1, 21), 3))
