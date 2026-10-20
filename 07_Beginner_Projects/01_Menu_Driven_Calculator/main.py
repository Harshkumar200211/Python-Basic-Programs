"""Project 1: Menu-Driven Calculator
Concepts: functions, input, operators, if-elif and loops.
"""

def read_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Please enter a valid number.")


def main():
    while True:
        print("\n=== CALCULATOR ===")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Choose an option: ").strip()
        if choice == "5":
            print("Calculator closed.")
            break
        if choice not in {"1", "2", "3", "4"}:
            print("Please choose 1, 2, 3, 4 or 5.")
            continue

        first = read_number("Enter first number: ")
        second = read_number("Enter second number: ")

        if choice == "1":
            result = first + second
        elif choice == "2":
            result = first - second
        elif choice == "3":
            result = first * second
        else:
            if second == 0:
                print("Division by zero is not allowed.")
                continue
            result = first / second

        print("Result:", result)


if __name__ == "__main__":
    main()
