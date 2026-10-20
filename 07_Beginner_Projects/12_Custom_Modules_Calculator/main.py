"""Project 12: Calculator Built with Custom Modules
Run this file from its own folder: python main.py
Concepts: import, custom modules, functions and exception handling.
"""

from calculator_operations import add, subtract, multiply, divide
from geometry import circle_area, rectangle_area


def read_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Enter a valid number.")


def main():
    while True:
        print("\n=== MODULAR CALCULATOR ===")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Rectangle area")
        print("6. Circle area")
        print("7. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "7":
            print("Goodbye.")
            break
        if choice not in {"1", "2", "3", "4", "5", "6"}:
            print("Choose an option from 1 to 7.")
            continue

        try:
            if choice in {"1", "2", "3", "4"}:
                a = read_number("Enter first number: ")
                b = read_number("Enter second number: ")
                if choice == "1":
                    result = add(a, b)
                elif choice == "2":
                    result = subtract(a, b)
                elif choice == "3":
                    result = multiply(a, b)
                else:
                    result = divide(a, b)
            elif choice == "5":
                length = read_number("Enter rectangle length: ")
                breadth = read_number("Enter rectangle breadth: ")
                result = rectangle_area(length, breadth)
            else:
                radius = read_number("Enter circle radius: ")
                result = circle_area(radius)
            print("Result:", round(result, 2))
        except (ZeroDivisionError, ValueError) as error:
            print("Cannot complete operation:", error)


if __name__ == "__main__":
    main()
