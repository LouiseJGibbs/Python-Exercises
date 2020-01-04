#069 Country Tuple
country_tuple = ("UK", "France", "Germany", "Holland", "Spain")

print(country_tuple[0:5])
selection = input("Which country would you like: ")
print("You have selected " + selection+ ". The index for this is " + str(country_tuple.index(selection)))

#070 Country Tuple (select index)
country_tuple = ("UK", "France", "Germany", "Holland", "Spain")

for i in range(0,len(country_tuple)):
    print(i, country_tuple[i])

selection = int(input("Which country would you like. Enter a number between 0 and " + str(len(country_tuple)- 1)+ ": "))
while selection > (len(country_tuple)-1):
    selection = int(input("Which country would you like. Enter a number between 0 and " + str(len(country_tuple) - 1) + ": "))

print("You have selected " + country_tuple[selection])

#071 List of sports
sports_list = ["Football", "Cricket"]
anothersport = "yes"
print(sorted(sports_list))
while input("Another Sport? yes/no: ") == "yes":
    sports_list.append(input("What is your favourite sport? "))
    print(sorted(sports_list))

#072 School subjects
topics_list = ["Maths", "French", "German", "English", "Sports", "Art"]
print(sorted(topics_list))
listComplete = "no"

while listComplete != input("Would you like to change subjects? yes/no "):
    d = input("What subject would you like to delete? ")
    r = input("What new subject would you like to add? ")
    topics_list.remove(d)
    topics_list.append(r)
    print(sorted(topics_list))
    
#073 Food Dictionary

food = {}


for i in range(1,5):
    food[i] = input("Please enter a food that you like: ")

print(food)

while input("Type 'Y' or 'y' if you'd like to change something: ").lower() == "y":
    change = int(input("Type the number of the item you'd like to change: "))
    newFood = input("What would you like to replace " + food[change] + " with? ")
    food[change] = newFood
    print(food)
print(sorted(food.values()))

#074 10 colours

colour = []
for i in range(1,11):
    colour.append(input("Please enter a colour (" + str(11-i)+ " to go): "))

start = int(input("Please enter a number between 0 and 4: "))
end = int(input("Please enter a number between 5 and 9: "))

print(colour[start:end])

#075 List of 3 digit numbers
numbers = [123, 523, 623, 723]
n = int(input("Please type in a 3 digit number: "))

if n in numbers:
    print("Well done, this number appears in position " + str(numbers.index(n) + 1))
else:
    print("Number not found")

print(numbers)

#076 Invitation list
names = ["Tom", "Dick", "Harry"]
print(names)

while input("Would you like to invite someone else? Yes/No ").lower() != "no":
    names.append(input("Please type the name? " ))
    print(names)

print("You have invited " +  str(len(names)) + " people to the party");

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
              
#079 List of numbers
nums = []

for i in range(0,3):
    nums.append(int(input("Please enter a number to add to the list: ")))
    print(nums)

while input("Would you like to add another number to the list? Yes/No: ").lower() != "no":
    nums.append(int(input("Please enter a number to add to the list: ")))
    print(nums)
    if input("Are you sure you want to add this number to the list? Yes/No: ").lower() == "no":
        del nums[len(nums) - 1]
    print(nums)

for i in nums:
    print(i)

    



