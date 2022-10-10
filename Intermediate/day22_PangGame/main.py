from turtle import Screen
from paddle import Paddle
from ball import Ball
from scorebord import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pang")
screen.tracer(0)
r_paddle = Paddle((380, 0))
l_paddle = Paddle((-380, 0))
ball = Ball()
r_score = Scoreboard((50, 200))
r_score.score_display()
l_score = Scoreboard((-50, 200))
l_score.score_display()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:

    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 350) or (ball.distance(l_paddle) < 50 and ball.xcor() < -350):
        ball.bounce_x()

    # 🌹Separate: convenient to count score
    # Detect miss right paddles
    if ball.xcor() > 380:
        ball.reset()
        l_score.count()

    # Detect miss right paddles
    if ball.xcor() < -380:
        ball.reset()
        r_score.count()


screen.exitonclick()
