import random

#052 Random int between 1 and 100
print(str(random.randint(1, 100)))

#053 Choose random fruit
print(random.choice(["banana", "apple", "pear", "orange", "grape"]))

#054 heads or tails
coinToss = random.choice(["h", "t"])
choice = input("Heads or Trails (h/t)")
while choice != "h" and choice!= "t":
    choice = input("Invalid Answer. Heads or Trails (h/t)")
if choice == coinToss:
    print("You Win")
else:
    print("You Lose")

#055, 056 and 057 Guess the random number
r = random.randint(1, 10)
c = int(input("What is the random number? ")) 
while c != r:
    if(c<r):
        print("Too low")
    else:
        print("Too high")
    c = int(input("What is the random number? ")) 

print("Well done, the correct number was " + str(r))

#058 Maths quiz
score = 0;
for i in range(1, 10):
    num1 = random.randint(0,100)
    num2 = random.randint(0,100)

    answer = int(input(str(num1) + " + " + str(num2) + "="))
    if answer == (num1+num2):
        print("Correct")
        score = score + num1 + num2
    else:
        print("Incorrect")
    print("Current score: " + str(score))

#059 Pick the correct colour
colour = random.choice(["Red", "Yellow", "Green", "Blue", "Purple"])

while input("Guess the colour, start with capital, rest in lower case: ") != colour:
    if colour == "Red":
        print("Incorrect, this will make you angry")
    elif colour == "Yellow":
        print("Incorrect, aren't you a ray of sunshine")
    elif colour == "Green":
        print("Incorrect, i'm envious that you've not guessed this")
    elif colour == "blue":
        print("Incorrect, I guess you feel a little down now")
    elif colour == "purple":
        print("Incorrect, its not red or blue, what could it be?")

print("Correct, the answer is " + colour)
