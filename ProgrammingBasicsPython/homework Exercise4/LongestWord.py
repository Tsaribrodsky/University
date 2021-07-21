# Write a python program to find the longest word in a given sentence

def longestWord(sentence):
    lengthWord = 0

    for i in sentence.split():
        if len(i) > lengthWord:
            lengthWord = len(i)

    return lengthWord


sentence = "List is a collection which is ordered and changeable Allows duplicate members"
print(longestWord(sentence))