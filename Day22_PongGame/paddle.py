from turtle import Turtle
MOVEMENT_STEPS = 20
class Paddle(Turtle):
    def __init__(self, position):
        # TODO Create a paddles that can move
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid= 5,stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def up(self):
        self.goto(self.xcor(), self.ycor()+MOVEMENT_STEPS)

    def down(self):
        self.goto(self.xcor(), self.ycor() - MOVEMENT_STEPS)
