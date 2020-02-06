#105 Write 5 numbers to a document
file = open("Number.txt", "a")

for i in range(0,5):
    file.write(str(int(input("Please enter a number: "))) + ", ")

file.write("\n")
file.close()

#106 Write 5 names to a document on different lines
file = open("Names.txt", "a")

for i in range(0,5):
    file.write(str(input("Please enter a name: ")) + "\n")

file.close();

#107 Display names from file
file = open("Names.txt", "r")
print(file.read())
file.close()

#108 Add names to file
filename = "Names.txt"

file = open(filename, "r")
print(file.read())

file = open(filename, "a")
while input("Would you like to add another name to the list? Y/N ").lower() == "y":
    file.write(input("Please enter a name: ") + "\n")
file.close()

file = open(filename, "r")
print("Final List: \n" + file.read())

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

#110 Save all but one to new file
file1 = open("Names.txt", "r")
print(file1.read())
file1.close()

file2 = open("Names2.txt", "w")

name = input("Please enter a name: ") + "\n"

file1 = open("Names.txt", "r")
for i in file1:
    if i != name:
        file2 = open("Names2.txt", "a")
        file2.write(i + "\n")
        file2.close()

file2 = open("Names2.txt", "r")
print(file2.read())
        
