# Write a program for personal contact book.
# Menu based interface for creating, updating, searching and removing records.
# The information need to be stored in comma separated text file.

import pickle
contactDict = {}
loadedContactDict = {}
createNewContactDict = {}


def menu():
    print("1. Create a new contact")
    print("2. Update a contact")
    print("3. Search a contact")
    print("4. Remove a contact")
    number = int(input("Enter a number to make a choice: "))

    if number == 1:
        createContact()
    elif number == 2:
        updateContact()
    elif number == 3:
        searchContact()
    elif number == 4:
        deleteContact()
    else:
        print("Wrong number!")


def saveFile():
    with open("contacts.p", "wb") as f:
        pickle.dump(contactDict, f)


def loadFile():
    with open("contacts.p", "rb") as f:
        loadedContactDict = pickle.load(f)
        return loadedContactDict


# It takes me enormous free time to understand and wrote working dictionary. But I'm happy at the end. Not perfect but it works.
def createContact():
    with open("contacts.p", "rb") as f:
        loadedContactDict = pickle.load(f)
    contactDict = loadedContactDict
    newName = input("Enter a name: ")
    print("Enter data for", newName)

    createNewContactDict = {
    newName: {"address": "", "birthDay": "", "phoneNumber": "", "email": "", "profession": "", "interests": ""}}
    createNewContactDict["newName"] = newName
    createNewContactDict[newName]["address"] = input("Enter an address: ")
    createNewContactDict[newName]["birthDay"] = int(input("Enter a birth day: "))
    createNewContactDict[newName]["phoneNumber"] = int(input("Enter a phone number: "))
    createNewContactDict[newName]["email"] = input("Enter an email: ")
    createNewContactDict[newName]["profession"] = input("Enter a profession: ")
    createNewContactDict[newName]["interests"] = input("Enter interests: ")
    contactDict.update(createNewContactDict)

    with open("contacts.p", "wb") as f:
        pickle.dump(contactDict, f)


def searchContact():
    contactDict = loadFile()
    print("Look up name.")
    name = input("Enter name: ")
    if name in contactDict:
        print("Information for", name, " is: ", contactDict[name])
    else:
        print(name, "was not found.")


def updateContact():
    with open("contacts.p", "rb") as f:
        loadedContactDict = pickle.load(f)
    contactDict = loadedContactDict
    name = input("Enter a name: ")
    print("Update all information about", name)

    createNewContactDict = {
        name: {"address": "", "birthDay": "", "phoneNumber": "", "email": "", "profession": "", "interests": ""}}
    createNewContactDict["name"] = name
    createNewContactDict[name]["address"] = input("Enter an address: ")
    createNewContactDict[name]["birthDay"] = int(input("Enter a birth day: "))
    createNewContactDict[name]["phoneNumber"] = int(input("Enter a phone number: "))
    createNewContactDict[name]["email"] = input("Enter an email: ")
    createNewContactDict[name]["profession"] = input("Enter a profession: ")
    createNewContactDict[name]["interests"] = input("Enter interests: ")
    contactDict.update(createNewContactDict)

    with open("contacts.p", "wb") as f:
        pickle.dump(contactDict, f)


def deleteContact():
    with open("contacts.p", "rb") as f:
        loadedContactDict = pickle.load(f)
    contactDict = loadedContactDict
    name = input("Enter name to remove the contact: ")
    if name in contactDict:
        del contactDict[name]
        contactDict.update(createNewContactDict)
        with open("contacts.p", "wb") as f:
            pickle.dump(contactDict, f)
        print(name, "was removed")
    else:
        print(name, "was not found!")


menu()