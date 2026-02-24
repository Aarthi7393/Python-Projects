from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)
#screen.bgpic("racetrack.gif")

#turtle.textinput(title, prompt)¶
#Pop up a dialog window for input of a string. Parameter title is the title of the dialog window, prompt is a text mostly describing what information to input.
# Return the string input. If the dialog is canceled, return None
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y_position = [-100, -60, -20, 20, 60, 100]
turtles =[]
is_race_on = False
for turtle in range(0,6):
    new_turtle  = Turtle(shape="turtle")
    new_turtle.color(colors[turtle])
    new_turtle.penup()
    new_turtle.goto(-230, y_position[turtle])
    turtles.append(new_turtle)
user_choice = screen.textinput(title="Your BET???", prompt = "Which turtle would win the race? Enter a color : ")
if user_choice:
    is_race_on = True
while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winning_turtle = turtle.pencolor()

            if user_choice == winning_turtle:
                print(f"Congratulations! You won the race! You win with {user_choice}!")
            else:
                print(f"Sorry, you lost. You lost with {user_choice}!\n The winning turtle "
                      f"is {winning_turtle}.  ")
            is_race_on = False


        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)









screen.exitonclick()