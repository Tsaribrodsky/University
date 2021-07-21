# Find the Factorial of a Number

number = int(input("Enter a positive number to calculate the factorial: "))
factorial = 1

if number == 0:
    print("Factorial of 0 is 1.")
elif number < 0:
    number = int(input("Enter a positive number to calculate the factorial: "))
    for i in range(1, number +1):
        factorial *= i
    print("Factorial of", number, "is", factorial)
else:
    for i in range(1, number +1):
        factorial *= i
    print("Factorial of", number, "is", factorial)