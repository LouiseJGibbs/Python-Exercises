#023 Print section of string
rhyme = input("Please enter the first line of a nursery rhyme: ")
rhymeLength = len(rhyme)
print("You've entered", rhymeLength, "characters")

num1 = int(input("Please enter a number that is less than " + str(rhymeLength) + ": "))
num2 = int(input("Please enter a number between " + str(num1) + " and "+ str(rhymeLength) + ": "))
print(rhyme[num1:num2])
