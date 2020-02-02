import csv

file = open("Books.csv", "w")
newRecord = "0, To Kill a Mocking Bird, Harper Lee, 1960\n"
file.write(str(newRecord))

newRecord = "1, A Brief History Of Time, Stephen Hawking, 1988\n"
file.write(str(newRecord))

newRecord = "2, The Great Gatsby, F. Scott Fitzgerald, 1922\n"
file.write(str(newRecord))

newRecord = "3, The Man Who Mistook His Wife For A Hat, Oliver Sacks, 1985\n"
file.write(str(newRecord))

newRecord = "4, Pride and Prejudice, Jane Austen, 1813\n"
file.write(str(newRecord))

file.close()



