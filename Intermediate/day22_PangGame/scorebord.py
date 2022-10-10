from turtle import Turtle
ALIGN = "center"
FONT = ('Courier', 80, 'normal')


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        # must before writing
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(position)

    def score_display(self):
        # Take data out to be the constants
        # Easy to Change
        self.write(f"{self.score}", align=ALIGN, font=FONT)  # font need a tuple

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER 😭", align=ALIGN, font=FONT)  # font need a tuple

    def count(self):
        self.score += 1
        self.clear()
        self.score_display()
