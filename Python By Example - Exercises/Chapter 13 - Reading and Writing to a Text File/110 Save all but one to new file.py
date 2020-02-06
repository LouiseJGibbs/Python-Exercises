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
        
