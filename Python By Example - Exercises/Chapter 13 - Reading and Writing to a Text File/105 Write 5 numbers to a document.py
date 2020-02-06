#105 Write 5 numbers to a document
file = open("Number.txt", "a")

for i in range(0,5):
    file.write(str(int(input("Please enter a number: "))) + ", ")

file.write("\n")
file.close()
