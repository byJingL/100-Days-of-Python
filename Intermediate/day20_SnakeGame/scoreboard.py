from turtle import Turtle
ALIGN = "center"
FONT = ('Arial', 18, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        # must before writing
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)

    def score_display(self):
        # Take data out to be the constants
        # Easy to Change
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)  # font need a tuple

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER 😭", align=ALIGN, font=FONT)  # font need a tuple

    def count(self):
        self.score += 1
        self.clear()
        self.score_display()
