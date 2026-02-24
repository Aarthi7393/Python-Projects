import random
import colorgram
import turtle as t
#colorgram.py is a Python library that lets you extract colors from images.
# Compared to other libraries, the colorgram algorithm’s results are more intense.
colors = colorgram.extract('download.jpeg', 50)
extracted_color =[]
for color in colors:
    #current_color = color.rgb
    current_color = (color.rgb.r, color.rgb.g, color.rgb.b)
    extracted_color.append(current_color)

#from extracted colors, remove white and get other colors.
colors = [ (243, 250, 246), (250, 244, 248), (240, 245, 250), (234, 225, 84), (195, 8, 69), (231, 54, 132), (197, 77, 17), (113, 177, 213), (194, 164, 14), (216, 162, 102), (29, 104, 167), (34, 187, 113), (14, 24, 64), (20, 29, 169), (231, 224, 7), (215, 134, 177), (201, 32, 132), (14, 182, 210), (231, 167, 197), (127, 188, 161), (10, 48, 28), (54, 20, 10), (40, 132, 75), (140, 218, 203), (108, 92, 210), (235, 64, 34), (131, 217, 231), (183, 17, 8), (11, 96, 53), (75, 10, 28), (167, 182, 234), (242, 167, 153), (10, 84, 102), (253, 4, 50), (64, 95, 11), (248, 12, 8), (15, 46, 248)]
tim = t.Turtle()
screen = t.Screen()
t.colormode(255)
tim.speed("fastest")
#screen.setup(width=200, height= 200)
screen.bgcolor("white")

def turtle_to_start(turtle):
    turtle.hideturtle()
    turtle.penup()
    turtle.setheading(220)
    turtle.fd(300)
    turtle.setheading(0)

def turtle_movement(turtle, total_dots):
    for dotcount in range(1, total_dots+1):
        turtle.pendown()
        turtle.pencolor(random.choice(colors))
        turtle.dot(10)
        turtle.penup()
        turtle.fd(50)
        if dotcount %10 == 0:
            turtle.setheading(90)
            turtle.forward(50)
            turtle.setheading(180)
            turtle.forward(500)
            turtle.setheading(0)


total_dots = 100
turtle_to_start(tim)
turtle_movement(tim, total_dots)


screen.exitonclick()