# Find Factorial of Number Using Recursion

def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)


number = int(input("Enter a number: "))

if number < 0:
    print("Factorial doesn't exist for negative numbers.")
elif number == 0:
    print("The Factorial of 0 is 1.")
else:
    print("The Factorial of", number, "is", factorial(number))
