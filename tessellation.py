from turtle import *
import math

#Name your turtle
ke=Turtle()
colormode(255)

#Set Up your screen and starting position.
setup(500,300)
ke.setposition(0,0)

### Write you code below:
ke.pendown()
ke.pencolor("blue")
for number in range (3):
    for number in range (6):
        ke.forward(30)
        ke.right(60)
    ke.left(120)

penup()

ke.forward(90)
pendown()
for number in range (3):
    for number in range (6):
        ke.forward(30)
        ke.right(60)
    ke.left(120)

exitonclick()
