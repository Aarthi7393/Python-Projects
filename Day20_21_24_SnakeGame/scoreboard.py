from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 10, "normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        #self.high_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        with open("data.txt","r") as file:
            self.high_score = int(file.read())
        self.refresh_score()


    def increase_score(self):
        self.score += 1
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.write(f"Score : {self.score} HighScore : {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.refresh_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self. write("GAME OVER", align=ALIGNMENT, font=FONT)
