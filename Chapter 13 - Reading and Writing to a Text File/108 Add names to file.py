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
