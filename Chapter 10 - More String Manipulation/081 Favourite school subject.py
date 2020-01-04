#081 Favourite school subject
subject = input("What is your favourite subject at school? ")
newString = ""
for i in subject:
    newString = newString + i + "-"

print(newString[:-1])
