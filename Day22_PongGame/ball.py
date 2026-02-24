from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def ball_move(self):
        self.goto(self.xcor()+self.x_move, self.ycor()+self.y_move)


    def bounce_y(self):
        self.y_move *= -1
        self.move_speed *= 0.9

    def bounce_x_left_paddle(self):
        self.x_move = (abs(self.x_move))
        self.move_speed *= 0.9

    def bounce_x_right_paddle(self):
        #self.x_move *= -1
        self.x_move = -(abs(self.x_move))
        self.move_speed *= 0.9

    # def bounce_x(self):
    #     self.x_move *= -1
    #     self.move_speed *= 0.9



    def game_restart(self):
        self.goto(0,0)
        self.move_speed = 0.1
        #self.bounce_x()
        self.x_move *= -1




