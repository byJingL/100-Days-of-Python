import turtle
from turtle import Turtle, Screen
import turtle as t
import random


# Todo: Draw different shapes
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_shape(num_lines):
    angle = 360 / num_lines
    for _ in range(num_lines):
        ema.forward(100)
        ema.right(angle)


turtle.colormode(255)
ema = t.Turtle()
for lines in range(3, 11):
    ema.color(random_color())
    draw_shape(lines)

# Todo: Draw a square
tim = Turtle()
tim.shape("turtle")
tim.color("red", "lightpink")
for _ in range(4):  # remember (0, 4)
    tim.forward(100)
    tim.right(90)

# Todo: Draw a dashed line
jen = t.Turtle()
jen.color("green")
jen.goto(-200, 150)
for _ in range(15):
    jen.forward(10)
    jen.penup()
    jen.forward(10)
    jen.pendown()

screen = Screen()
screen.exitonclick()
