# Program 9: Print a multiplication table

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)
