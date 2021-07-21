# Write a program that prints all prime numbers.


# I don't know what will happen if I print all prime numbers
# therefor I'll print prime numbers from 1 to 100.

for numbers in range(1, 100):
    if numbers > 1:
        for i in range(2, numbers):
            if numbers % i == 0:
                break
        else:
            print(numbers)