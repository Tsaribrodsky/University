# Modify the previous program such that only the users Alice and Bob are greeted with their names.

yourName = input("Please, write your name!: ")

if yourName == "Alice" or yourName == "Bob":
    print("Have a nice day " + yourName + "!")
else:
    print("This incident will be reported " + yourName + "!")