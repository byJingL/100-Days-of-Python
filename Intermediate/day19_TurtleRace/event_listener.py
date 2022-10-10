from turtle import Turtle, Screen


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


# Todo: 2 ways make turtle draw arc(弧)
# turn left
def move_counter_clockwise():
    # right "-10"
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
    tim.forward(10)


# turn right
def move_clockwise():
    # just turn
    tim.right(10)
    # draw arc
    tim.forward(10)


def clean():
    screen.resetscreen()


def clean2():
    tim.clear()
    tim.penup()
    tim.home()


tim = Turtle()
screen = Screen()

screen.listen()
# function in onkey has no"()"
# if not, just be triggered once
screen.onkey(fun=move_forwards, key="w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=move_counter_clockwise, key="a")
screen.onkey(fun=move_clockwise, key="d")
screen.onkey(fun=clean2, key="c")
screen.exitonclick()

