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


# Todo: Draw Spirograph
# Todo: Solution 1

def per_switch(draw_times):
    angle = 360 / draw_times
    return angle


turtle.colormode(255)
ema = t.Turtle()
ema.speed("fastest")
times = 100
for i in range(times):
    ema.color(random_color())
    ema.setheading(per_switch(times) * i)
    ema.circle(100)


screen = t.Screen()
screen.exitonclick()
