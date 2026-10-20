# Program 6: Find the larger of two numbers

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a > b:
    print("Largest number is:", a)
elif b > a:
    print("Largest number is:", b)
else:
    print("Both numbers are equal")
