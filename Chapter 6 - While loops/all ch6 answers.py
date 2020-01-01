#045 Stop at 50
num = 0

while num <= 50:
    num = num + int(input("Please enter a number: "))
    print("New total = " +  str(num))

print("Total has reached 50")

#046 new number until greater than 5
num = int(input("Please enter a number less than 5: "))
while num < 5:
    num = int(input("Please enter a number less than 5: "))

print("The last number you entered was " + str(num))

#047 Add numbers
sum = 0
print("Current sum: " + str(sum))
while input("Would you like to add another number to the sum? y/n ")=="y":
    sum = sum + int(input("What number would you like to add to " + str(sum)))
    print("New sum is " + str(sum))
print("Final sum: " + str(sum))

#048 Party invitations
while input("Would you like to invite someone to the party? y/n ") == "y":
    name = input("Who would you like to invite? ")
    print("You have invited ", name)

#049 guess the number
compnum = 50
count = 1
guess = int(input("Guess the number: "))
while guess != compnum:
    if(guess>compnum):
        print("Too High")
    else:
        print("Too Low")
    count = count + 1
    guess = int(input("Guess the number: "))

print("You finally guessed it. It only took you "+ str(count) +" attempts")

#050 Enter number between 10 and 20
num = int(input("Please enter a number between 10 and 20: "))
while num<=10 or num>=20:
    if num<=10:
        print("Too Low")
    else:
        print("Too High")
    num = int(input("Please enter a number between 10 and 20: "))
print("Thankyou")

#051 10 Green Bottles
for num in range(10, 0, -1):
    bottlesString = str(num) + " green bottles, hanging on the wall.\n" + str(num) + " green bottles, hanging on the wall.\nAnd if 1 green bottle should accidentally fall"
    print(bottlesString)
    while int(input("How many bottles will be hanging on the wall? ")) != num-1:
              print("Try again")
    print("There will be ", str(num - 1), "hanging on the wall")
