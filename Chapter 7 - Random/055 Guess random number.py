import random

#055 Guess the random number
r = random.randint(1, 5)
c = int(input("What is the random number? ")) 
while c != r:
    if(c<r):
        print("Too low")
    else:
        print("Too high")
    c = int(input("What is the random number? ")) 

print("Well done, the correct number was " + str(r))
