from scoreboard import Scoreboard
from ball import Ball
from paddle import  Paddle
from turtle import Screen
import time

LEFT_PADDLE = (-350, 0)
RIGHT_PADDLE = (350, 0)


#TODO Create a canvas
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


#TODO Paddle creation
paddle_left = Paddle(LEFT_PADDLE)
paddle_right = Paddle(RIGHT_PADDLE)


#TODO Create a ball and keeps moving
ball = Ball()
scoreboard = Scoreboard()



screen.textinput("Start Game", "Press 'OK' when you are ready to record!")
screen.listen()

#TODO Paddle Movement
# Left Paddle movement
screen.onkeypress(paddle_left.up, "w")
screen.onkeypress(paddle_left.down, "s")

# Right Paddle movement
screen.onkeypress(paddle_right.up, "Up")
screen.onkeypress(paddle_right.down, "Down")



#screen.onkey(paddle.up, "Up")
#screen.onkey(paddle.down, "Down")

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.ball_move()
    # TODO Detect collision of ball with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # TODO Detect collision with the paddle
    if ball.distance(paddle_right) < 50 and ball.xcor()>320:
        ball.bounce_x_right_paddle()
    if ball.distance(paddle_left) < 50 and ball.xcor()<-320:
        ball.bounce_x_left_paddle()

    # TODO Detect when paddle misses
    #right misses
    if ball.xcor()>380:
        scoreboard.left_point()
        scoreboard.update_score()
        ball.game_restart()

    #left misses
    if ball.xcor()<-380:
        scoreboard.right_point()
        scoreboard.update_score()
        ball.game_restart()
screen.exitonclick()









#TODO Keep track of the score



