# Python Program to Print the Fibonacci sequence

number = int(input("Enter a number to print the Fibonacci sequence: "))

n0, n1 = 0, 1

if number <= 0:
    number = int(input("Enter a number bigger than 0: "))
    print(n0)
    while n1 < number:
        print(n1)
        n0, n1 = n1, n0 + n1
elif number == 1:
    print(n0)
else:
    print(n0)
    while n1 < number:
        print(n1)
        n0, n1 = n1, n0 + n1