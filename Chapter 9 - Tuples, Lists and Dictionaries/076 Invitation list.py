#076 Invitation list
names = ["Tom", "Dick", "Harry"]
print(names)

while input("Would you like to invite someone else? Yes/No ").lower() != "no":
    names.append(input("Please type the name? " ))
    print(names)

print("You have invited " +  str(len(names)) + " people to the party");
