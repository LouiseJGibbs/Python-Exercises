import random

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
