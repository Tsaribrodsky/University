# Write a guessing game where the user has to guess a secret number.
# After every guess the program tells the user whether their number
# was too large or too small. At the end the number of tries needed
# should be printed. It counts only as one try if they input the same
# number multiple times consecutively.
import random

assumptions = 0

number = random.randrange(1, 10)

while True:
    guess = int(input("Guess the number between 1 and 10: "))
    assumptions += 1
    if guess == number:
        print("You got it!")
        break
    elif guess > number:
        print("Too large.")
    else:
        print("Too small.")

print("The number is {} and you made {} tries." .format(number, assumptions))