#077 Invitation list - remove invite
names = ["Tom", "Dick", "Harry"]
print(names)

while input("Would you like to invite someone else? Yes/No ").lower() != "no":
    names.append(input("Please type the name? " ))
    

print("You have invited " +  str(len(names)) + " people to the party");
print(names)

while input("Are you sure you want to invite these people to the party? Yes/No ").lower() == "no":
    n = input("Please type a name ")
    if n in names:
        print(n + " has invitation number " + str(names.index(n)))
        if input("Would you like to delete " + n + " from the list? Yes/No").lower() == "yes":
            del names[names.index(n)]
    else:
        print(n + " does not appear in the list")
    print(names)

print("You have invited " +  str(len(names)) + " people to the party");
print(names)
    
