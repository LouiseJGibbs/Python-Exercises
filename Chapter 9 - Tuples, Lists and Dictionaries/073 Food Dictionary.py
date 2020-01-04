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
    
