import turtle
from turtle import Turtle, Screen
import turtle as t
import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# Todo: Draw random walks
# Todo: Solution 1
def random_direction():
    direction = [0, 90, 180, 270]
    angle = random.choice(direction)
    return angle


turtle.colormode(255)
ema = t.Turtle()
ema.shape("circle")
ema.pensize(5)
ema.speed(0)
for _ in range(150):
    ema.color(random_color())
    ema.setheading(random_direction())
    ema.forward(15)


# # Todo: Solution 2
# def random_direction_draw(turtle_name):
#     direction = ["right", "left", "forward", "backward"]
#     next_step = random.choice(direction)
#     if next_step == "right":
#         turtle_name.right(90)
#         turtle_name.forward(15)
#     elif next_step == "right":
#         turtle_name.left(90)
#         turtle_name.forward(15)
#     elif next_step == "forward":
#         turtle_name.forward(15)
#     else:
#         turtle_name.backward(15)
#
#
# turtle.colormode(255)
# ema = t.Turtle()
# ema.pensize(5)
# ema.speed(0)
# for _ in range(500):
#     ema.color(random_color())
#     random_direction_draw(ema)

screen = Screen()
screen.bgcolor("lightgreen")
screen.exitonclick()

