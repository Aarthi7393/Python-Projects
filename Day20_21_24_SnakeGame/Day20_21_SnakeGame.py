import time
from turtle import Screen

from scoreboard import Scoreboard
from snake import Snake
from food import Food

#Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

#TODO Create snake
snake = Snake()
food = Food()

#TODO Create scoreboard
scoreboard = Scoreboard()

#TODO Control the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

#screen.textinput("Start Game", "Press 'OK' when you are ready to record!")
#TODO Move the snake
is_game_on = True
while is_game_on:
    snake.once_per_frame = True
    screen.update()
    time.sleep(0.1)
    snake.move()

    #TODO Detect Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend_snake()

    # TODO Detect collision with wall
    if snake.head.xcor()> 280 or snake.head.xcor()< -280 or snake.head.ycor()> 280 or snake.head.ycor()< -280:
        scoreboard.reset()
        snake.reset()
        # is_game_on = False
        # scoreboard.game_over()

    # TODO Detect collision with tail
    for segment in snake.segments[1:]:
        # if segment == snake.head:
        #     pass
        # elif snake.head.distance(segment) < 10:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            # is_game_on = False
            # scoreboard.game_over()



screen.exitonclick()