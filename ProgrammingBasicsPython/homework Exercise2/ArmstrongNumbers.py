# Find Armstrong Number in an Interval

print("An Armstrong number, also known as narcissistic number,"
      "is a number that is equal to the sum of the cubes of its own digits."
      "Program for Armstrong Number in an Interval")
lowerLimit = int(input("Enter lower limit: "))
upperLimit = int(input("Enter upper limit: "))

for number in range(lowerLimit, upperLimit +1):

    orderNumbers = len(str(number))
    sum = 0
    temp = number

    while temp > 0:
        digit = temp % 10
        sum += digit ** orderNumbers
        temp //= 10

    if number == sum:
        print(number)
