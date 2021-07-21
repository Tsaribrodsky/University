# Write a Python program to find the list of words that are longer than n from a given list of words

def findLongerWordsThanN(n, listOfWords):
    lengthWord = []
    phrase = listOfWords.split(" ")
    for i in phrase:
        if len(i) > n:
            lengthWord.append(i)
    return lengthWord


print(findLongerWordsThanN(2, "Python is a popular programming language. It was created by Guido van Rossum, and released in 1991."))