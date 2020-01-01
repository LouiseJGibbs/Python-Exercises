#047 Add numbers

sum = 0
print("Current sum: " + str(sum))
while input("Would you like to add another number to the sum? y/n ")=="y":
    sum = sum + int(input("What number would you like to add to " + str(sum)))
    print("New sum is " + str(sum))
print("Final sum: " + str(sum))
