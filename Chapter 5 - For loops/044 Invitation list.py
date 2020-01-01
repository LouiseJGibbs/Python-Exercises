#044 Invitation list

count = int(input("How many people will you invite to the party: "))

if count<=10:
    for i in range(1,count + 1):
        name = input("What is the name of guest " + str(i) + "? ")
        print(name, "has been invited")
else:
    print("Too many people, party cancelled")
    
