import turtle
import random

#066 Draw an octogan
turtle.pensize(3)
for i in range(0,8):
    turtle.color(random.choice(["red", "green", "blue", "purple", "orange", "yellow"]))
    turtle.forward(100)
    turtle.right(45)
