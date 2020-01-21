#109 File editing and creation
go = "Y"

while go.lower() == "y":
    print("1) Create a new file")
    print("2) Display a new file")
    print("3) Add a new item to the file")
    selection = int(input("Make a selection 1, 2, or 3 "))
    if selection == 1 or selection == 2 or selection == 3:
        if selection == 1:
            file = open("Subject.txt", "w")
            file.write(input("Please enter the name of a school subject: ") + "\n")
        elif selection == 2:
            file = open("Subject.txt", "r")
            print(file.read())
        else:
            file = open("Subject.txt", "a")
            file.write(input("Please enter the name of a school subject: ") + "\n")
        file.close()
    else:
        print("Invalid selection")
    go = input("Would you like to make a change to the file 'Subject.txt'? Y/N ")

print(open("Subject.txt", "r").read())
