# Write a program that takes your full name as input and displays
# the abbreviations of the first and middle names except the last
# name which is displayed as it is. For example, if your name is
# PetarIvanov Petrov, then the output should be P.I.Petrov.

def abbreviationNameMaker(fullName):

    while len(fullName.split()) < 3:
        fullName = input("Enter your full name: ")


    listName =fullName.split()
    newListName = ""

    for i in range(len(listName)-1):
        fullName = listName[i]
        newListName += (fullName[0].upper() + ".")

    newListName += listName[-1].title()

    return newListName

fullName = input("Enter your full name: ")
print(abbreviationNameMaker(fullName))

