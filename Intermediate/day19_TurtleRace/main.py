from turtle import Turtle, Screen
import random


def move_straight(which_turtle, what_step):
    which_turtle.forward(what_step)


screen = Screen()
screen.setup(width=500, height=400)

colors = ["red", "green", "yellow", "blue", "purple", "orange"]
turtle_list = []
for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    turtle_list.append(new_turtle)
    new_turtle.penup()
    new_turtle.setposition(-240, -80 + 30 * turtle_index)

user_bet = screen.textinput(title="Make your bet", prompt="Who will win the race, Enter a color: ")
is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:
    step = random.randint(0, 10)
    turtle = random.choice(turtle_list)
    move_straight(turtle, step)

    # condition is ">", not "=="!
    if turtle.xcor() > 230:
        is_race_on = False
        win_color = turtle.fillcolor()
        if win_color == user_bet:
            print(f"😊You win, {win_color} turtle win!")
        else:
            print(f"😭You lose, {win_color} turtle win!")
screen.exitonclick()
