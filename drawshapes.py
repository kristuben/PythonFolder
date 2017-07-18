from turtle import *
import math

#Name your turtle
ke=Turtle()
colormode(255)

#Set Up your screen and starting position.
setup(500,300)
ke.setposition(0,0)

### Write you code below:
color=input('Enter the color of the shapes:')
ke.pendown()
ke.pencolor(color)

length = input('Enter the length of the shapes:')
for number in range (4):
    ke.forward(int(length))
    ke.right(90)
for number in range (3):
    ke.forward(int(length))
    ke.left(120)

sides= input('Enter the number of sides for the shape:')
for number in range (int(sides)):
    ke.forward(int(length))
    ke.left(int(360/int(sides)))

exitonclick()
