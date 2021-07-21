# Write a Python program to get the largest and the smallest number from a list

def largestAndSmallestNumber(listOfNumbers):
    listOfNumbers.sort()
    print("Largest number is", listOfNumbers[0])
    print("Smallest number is", listOfNumbers[-1])


listOfNumbers = [23, 6, 59, 33, 10]
largestAndSmallestNumber(listOfNumbers)
