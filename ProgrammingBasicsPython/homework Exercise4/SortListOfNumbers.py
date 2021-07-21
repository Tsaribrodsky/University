# Write a python program to sort a given list of numbers without using sort() function

def sortGivenList(givenList):
    sortedList = []

    while givenList:
        min = givenList[0]
        for x in givenList:
            if x < min:
                min = x
        sortedList.append(min)
        givenList.remove(min)
    print(sortedList)

givenList = [2, 9, 87, 23, 56, 43, 249]
sortGivenList(givenList)