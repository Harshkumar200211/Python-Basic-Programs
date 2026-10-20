"""Project 5: Unit Converter
Concepts: functions, input, arithmetic and menu-driven logic.
"""

def read_value():
    while True:
        try:
            return float(input("Enter value: "))
        except ValueError:
            print("Please enter a valid number.")


def main():
    while True:
        print("\n=== UNIT CONVERTER ===")
        print("1. Kilometres to miles")
        print("2. Miles to kilometres")
        print("3. Celsius to Fahrenheit")
        print("4. Fahrenheit to Celsius")
        print("5. Kilograms to pounds")
        print("6. Pounds to kilograms")
        print("7. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "7":
            print("Converter closed.")
            break
        if choice not in {"1", "2", "3", "4", "5", "6"}:
            print("Please choose a listed option.")
            continue

        value = read_value()
        if choice == "1":
            result, unit = value * 0.621371, "miles"
        elif choice == "2":
            result, unit = value / 0.621371, "kilometres"
        elif choice == "3":
            result, unit = value * 9 / 5 + 32, "Fahrenheit"
        elif choice == "4":
            result, unit = (value - 32) * 5 / 9, "Celsius"
        elif choice == "5":
            result, unit = value * 2.20462, "pounds"
        else:
            result, unit = value / 2.20462, "kilograms"

        print(f"Converted value: {result:.2f} {unit}")


if __name__ == "__main__":
    main()
