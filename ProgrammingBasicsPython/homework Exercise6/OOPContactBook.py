# 1. Write a program for personal contact book using Object Oriented Programming approach.
# Menu based interface for creating, updating, searching and removing records.
# The information needs to be stored in a comma separated text file.
# Following fields need to be used:
# Name, Address, Birthday, Phone number, Email, Profession, Interests
import os


class OOPContactBook:
    def menu(self):
        print("1. Create a new contact")
        print("2. Update a contact")
        print("3. Search a contact")
        print("4. Remove a contact")
        number = int(input("Enter a number to make a choice: "))

        if number == 1:
            self.createContact()
        elif number == 2:
            self.updateContact()
        elif number == 3:
            self.searchContact()
        elif number == 4:
            self.deleteContact()
        else:
            print("Wrong number!")

    def __init__(self):
        self.contactList = ""

    # def saveFile(self):
    #     with open("contacts.txt", "w") as f:
    #         f.writelines(contactList)
    #
    # def loadFile(self):
    #     with open("contacts.txt", "r") as f:
    #         contactList = f.read()

    def createContact(self):
        with open("contacts.txt", "r") as f:
            contactList = f.read()
        newName = input("Enter a name: ")
        print("Enter data for", newName)
        address = input("Enter an address: ")
        birthday = input("Enter a birth day: ")
        phoneNumber = input("Enter a phone number: ")
        email = input("Enter an email: ")
        profession = input("Enter a profession: ")
        interests = input("Enter interests: ")
        createNewContact = newName + ", " + address + ", " + birthday + ", " + phoneNumber + ", " + email + ", " \
                               + profession + ", " + interests
        addToFile = contactList + createNewContact
        with open("contacts.txt", "w") as f:
            f.write(addToFile)
            f.write("\n")

    def searchContact(self):
        print("Look up name.")
        name = input("Enter name: ")
        contactList = open("contacts.txt", "r")
        for line in contactList:
            try:
                if line.startswith(name):
                    print(line)
            except:
                print(name, "was not found")

    def updateContact(self):
        with open("contacts.txt", "r") as f:
            contactList = f.read()
        name = input("Updating the contact. Enter a name: ")
        newName = input("Enter a name: ")
        address = input("Enter an address: ")
        birthday = input("Enter a birth day: ")
        phoneNumber = input("Enter a phone number: ")
        email = input("Enter an email: ")
        profession = input("Enter a profession: ")
        interests = input("Enter interests: ")
        newline = newName + ", " + address + ", " + birthday + ", " + phoneNumber + ", " + email \
                  + ", " + profession + ", " + interests
        oldline = ""
        for line in contactList.splitlines():
            if line.startswith(name):
                print("The contact:")
                print(line)
                oldline = str(line)
        newContactList = contactList.replace(oldline, newline)
        with open("contacts.txt", "w") as f:
            f.write(newContactList)
        print("Was changed to:")
        print(newline)

    def deleteContact(self):
        with open("contacts.txt", "r") as f:
            contactList = f.read()
        name = input("Deleting the contact. Enter a name: ")
        newline = ""
        oldline = ""
        for line in contactList.splitlines():
            if line.startswith(name):
                print("The contact:")
                print(line)
                oldline = str(line)
        newContactList = contactList.replace(oldline, newline)
        newContactList = os.linesep.join([s for s in newContactList.splitlines() if s.strip()])
        with open("contacts.txt", "w") as f:
            f.write(newContactList)
            f.write("\n")
        print("Was deleted.")


contacts = OOPContactBook()
contacts.menu()
