# Write a python program to find number of occurrences of given number without using built-in methods

def countOccurrences(n, listOfNumbers):
    count = 0
    for i in listOfNumbers:
        if i == n:
            count += 1
    return count


listOfNumbers = [23, 6, 23, 10, 23, 20, 10, 23, 23]
n = 23
print('{} has occurred {} times'.format(n, countOccurrences(n, listOfNumbers)))