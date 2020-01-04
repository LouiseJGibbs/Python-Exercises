#078 TV program list
shows = ["Coronation Street", "Eastenders", "Emmerdale"]

for i in shows:
    print(str(shows.index(i)), i)

while input("Would you like to add another show? Yes/No ").lower() != "no":
    newShow = input("What is the name of the show? ")
    pos = int(input("What position  in the list would you like to add this show? Enter a number between 0 and " + str(len(shows)) + " "))
    while pos > len(shows) or pos < 0:
            print("Invalid input")
            pos = int(input("What position  in the list would you like to add this show? Enter a number between 0 and " + str(len(shows)) + " "))
    shows.insert(pos, newShow)
    for i in shows:
        print(str(shows.index(i)), i)

print("Final List")
for i in shows:
    print(str(shows.index(i)), i)
              
