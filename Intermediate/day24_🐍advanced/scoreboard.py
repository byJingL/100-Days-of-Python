from turtle import Turtle
ALIGN = "center"
FONT = ('Arial', 18, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("score.txt", mode="r") as data:
            # return String
            self.high_score = int(data.read())
        # must before writing
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)

    def score_display(self):
        # Take data out to be the constants
        # Easy to Change
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGN, font=FONT)  # font need a tuple

    def count(self):
        self.score += 1
        self.score_display()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score.txt", mode="w") as data_w:
                # "w" mode can create a new file
                data_w.write(str(self.high_score))
        self.score = 0
        self.score_display()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER 😭", align=ALIGN, font=FONT)  # font need a tuple


