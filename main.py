import turtle as t
import random
from ColorList import color_list

# Set configuration of turtle module
t.colormode(255)
t.speed("fastest")
t.hideturtle()

# Create Tom, our turtle :)
tom = t.Turtle(visible=False)
tom.pensize(3)
radius = 10
distance = 2 * radius

for i in range(1, 11):
    for _ in range(10):
        color = random.choice(color_list)
        tom.color(color)
        tom.dot(radius)
        tom.penup()
        tom.forward(distance)
        tom.pendown()
    tom.penup()
    tom.setpos(0, distance * i)
    tom.pendown()


screen = t.Screen()
screen.exitonclick()
