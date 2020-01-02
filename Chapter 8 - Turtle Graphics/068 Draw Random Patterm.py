import turtle
import random

#068 Draw Random Pattern
num1 = random.randint(1,100)
num2 = random.randint(1,10)


for i in range(0, num1):
    for j in range(0,num2):
            turtle.forward(100/(num2/5))
            turtle.right(360/num2)
        
    turtle.right(360/num1)
