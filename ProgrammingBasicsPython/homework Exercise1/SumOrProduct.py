# Write a program that asks the user for a number n and gives them the possibility to choose
# between computing the sum and computing the product of 1,...,n.

n = int(input("Please, enter a number: "))
choice = input("What is your choice? Sum or Product?: ")

if choice == "sum":
    print(sum(range(1, n+1)))
elif choice == "product":
    product = 1
    for i in range(1, n+1):
        product *= i
    print(product)