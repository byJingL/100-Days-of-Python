from turtle import Turtle
ALIGN = "center"
FONT = ('Arial', 18, 'normal')
END_POSITION = (0,280)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.hideturtle()
        self.penup()

    def count(self):
        self.score += 1

    def game_over(self):
        self.goto(END_POSITION)
        self.write(f"😭Game over, you score is {self.score}/50. Missing States are in red color.", align=ALIGN, font=FONT)

    def win_the_game(self):
        self.goto(END_POSITION)
        self.write(f"😄You win the game!", align=ALIGN, font=FONT)
