from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


def screen_control():
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")


def user_choice():
    user = screen.textinput(title="Your choice", prompt="Do you want to continue the game? yes/no")
    return user


screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
scoreboard.score_display()

screen_control()

game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with Food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.food_extend()
        scoreboard.count()

    # Detect collision with wall
    if (snake.head.xcor() > 280) or (snake.head.xcor() < -280) or \
            (snake.head.ycor() > 280) or (snake.head.ycor() < -280):
        ask = user_choice()
        if ask == "yes":
            scoreboard.reset()
            snake.reset()
            screen_control()
        else:
            game_is_on = False
            scoreboard.game_over()

    # Detect collision with tail
    # head collides with any segments
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            ask = user_choice()
            if ask == "yes":
                scoreboard.reset()
                snake.reset()
                screen_control()
            else:
                game_is_on = False
                scoreboard.game_over()

screen.exitonclick()
