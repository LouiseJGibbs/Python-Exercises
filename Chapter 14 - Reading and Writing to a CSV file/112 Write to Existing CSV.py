import csv

while input("Would you like to add a record to books.csv? Enter Y or y: ").lower() == "y":
    name = input("What is the name of the book? ")
    author = input("What is the authors name? ")
    year = input("When was the book written? ")

    file = open("Books.csv", "r")
    rows = sum(1 for row in file) + 1

    file = open("Books.csv", "a")
    newRecord = str( str(rows) + ", " + name + ", " + author + ", " +  year + "\n")
    file.write(newRecord)
    file.close()

    
