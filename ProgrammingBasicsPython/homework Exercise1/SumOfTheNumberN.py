# Write a program that asks the user for a number n and prints the sum of the numbers 1 to n

sum = 0
n = int(input("Please, enter a number: "))

for i in range(1, n+1):
    sum += i

print(sum)