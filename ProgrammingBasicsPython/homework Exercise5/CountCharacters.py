# Write a program to find the number of vowels, consonants, digits and white space characters in a string.

def countTypeOfCharacters(sentence):
    vowels = 0
    consonants = 0
    digits = 0
    spaceCharacters = 0

    for i in range(0, len(sentence)):

        char = sentence[i]

        if ( (char >= 'a' and char <= 'z') or
             (char >= 'A' and char <= 'Z') ):

            char = char.lower()

            if (char == 'a' or char == 'e' or char == 'i'
                    or char == 'o' or char == 'u'):
                vowels += 1
            else:
                consonants += 1
        elif char.isdigit():
            digits += 1
        elif char == " ":
            spaceCharacters += 1
        else:
            continue

    print("Vowels:", vowels)
    print("Consonant:", consonants)
    print("Digits:", digits)
    print("Space characters:", spaceCharacters)


sentence = "Computers do not deal with characters, they deal with numbers (binary). " \
           "Even though you may see characters on your screen, internally it is stored " \
           "and manipulated as a combination of 0's and 1's."
countTypeOfCharacters(sentence)
