# Write a program that converts a text from both a file  and user input to Morse code and displays it.
# (Optional:  And also plays it with with computer speaker. )


import os

morseCodeDictionary = {'A': '.-', 'B': '-...',
                       'C': '-.-.', 'D': '-..', 'E': '.',
                       'F': '..-.', 'G': '--.', 'H': '....',
                       'I': '..', 'J': '.---', 'K': '-.-',
                       'L': '.-..', 'M': '--', 'N': '-.',
                       'O': '---', 'P': '.--.', 'Q': '--.-',
                       'R': '.-.', 'S': '...', 'T': '-',
                       'U': '..-', 'V': '...-', 'W': '.--',
                       'X': '-..-', 'Y': '-.--', 'Z': '--..',
                       '1': '.----', '2': '..---', '3': '...--',
                       '4': '....-', '5': '.....', '6': '-....',
                       '7': '--...', '8': '---..', '9': '----.',
                       '0': '-----', ', ': '--..--', '.': '.-.-.-',
                       '?': '..--..', '/': '-..-.', '-': '-....-',
                       '(': '-.--.', ')': '-.--.-', " ": "  "}

def choice():
    decide = input("Do you want to read the text from file or enter the text from keyboard? "
                   "Choice 1 or 2: ")
    if decide == "1":
        file()
    elif decide == "2":
        userInput()
    else:
        print("You don't have another choice!")

def convertToMorse(text):
    morseCode = ""
    for letter in text:
        if letter.upper() in morseCodeDictionary:
            morseCode += morseCodeDictionary[letter.upper()]
        else:
            print("There is no symbol as this.")
    return morseCode

def file():
    with open("text.txt", "r") as f:
        text = f.read().replace("\n", "")
    print(convertToMorse(text))
    sounds(text)

def userInput():
    text = input("Enter some text: ")
    print(convertToMorse(text))
    sounds(text)

# The method "def sounds(text)" works only on Linux. You must have library "sox" on your Linux.
def sounds(text):
    for char in convertToMorse(text):
        if char == ".":
            duration = 0.05
            freq = 400
            os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
        elif char == "-":
            duration = 0.1
            freq = 700
            os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))

choice()