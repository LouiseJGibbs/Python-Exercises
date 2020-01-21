#106 Write 5 names to a document on different lines
file = open("Names.txt", "a")

for i in range(0,5):
    file.write(str(input("Please enter a name: ")) + "\n")

file.close();

