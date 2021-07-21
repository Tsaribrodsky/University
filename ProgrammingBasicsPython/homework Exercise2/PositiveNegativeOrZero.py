# Check if a Number is Positive, Negative or 0

number = int(input("Enter a number to check if it is positive, negative or 0: "))

if number == 0:
    print(number, "is zero and nothing else.")
elif number > 0:
    print(number, "is positive.")
else:
    print(number, "is negative.")