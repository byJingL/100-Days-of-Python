from turtle import Turtle
START_POSITION = (0, 0)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(START_POSITION)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # 🌹import: 维持y下降, 改move()里的参数
    # detect the wall
    def bounce_y(self):
        self.y_move *= -1

    # detect the paddles
    def bounce_x(self):
        self.x_move *= -1
        # speed_up
        self.move_speed *= 0.9

    def reset(self):
        self.goto(START_POSITION)
        self.bounce_x()
