from turtle import Turtle

FONT = ("Courier", 10, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.hideturtle()
        self.goto(-250,250)
        self.score_board()

    def level_up(self):
        self.score += 1
        self.score_board()

    def score_board(self):
        self.clear()
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over!", align="center", font=FONT)

