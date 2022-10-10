from turtle import Turtle
ALIGN = "left"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        # must before writing
        self.hideturtle()
        self.penup()
        self.goto(-275, 260)

    def score_display(self):
        # Take data out to be the constants
        # Easy to Change
        self.write(f"Level: {self.level}", align=ALIGN, font=FONT)  # font need a tuple

    def count_level(self):
        self.level += 1
        self.clear()
        self.score_display()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)  # font need a tuple
