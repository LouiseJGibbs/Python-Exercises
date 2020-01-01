import random

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
