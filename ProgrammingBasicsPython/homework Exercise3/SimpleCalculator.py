# Python Program to Make a Simple Calculator

number1 = float(input("Enter first number: "))
operator = input("Enter operator: ")
number2 = float(input("Enter second number: "))

if operator == "+":
    print(number1 + number2)
elif operator == "-":
    print(number1 - number2)
elif operator == "*":
    print(number1 * number2)
elif operator == "/":
    print(number1 / number2)
else:
    print("Wrong operator.")