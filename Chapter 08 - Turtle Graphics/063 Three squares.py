import turtle

#063 Three squares
colour=["red", "green", "blue"]
turtle.penup()
turtle.left(135)
turtle.forward(300)
turtle.right(135)

turtle.shape("turtle")
for i in range(0,3):
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("black", colour[i])
    for i in range(0,4):
        turtle.forward(100)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(120)
