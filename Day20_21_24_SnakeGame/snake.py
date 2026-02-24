from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVEMENT_SPEED = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        # TODO Create snake body
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        #To avoid multiple movements before a refresh
        self.once_per_frame = True

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_snake(position)

    # TODO Move the snake
    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg-1].xcor()
            new_y = self.segments[seg-1].ycor()
            self.segments[seg].goto(new_x, new_y)
            #self.segments[seg].goto(self.segments[seg-1].position())
        self.head.forward(MOVEMENT_SPEED)


    # TODO Control the snake
    def up(self):
        if self.head.heading() != DOWN and self.once_per_frame:
            self.head.setheading(UP)
            self.once_per_frame = False
    def down(self):
        if self.head.heading() != UP and self.once_per_frame:
            self.head.setheading(DOWN)
            self.once_per_frame = False
    def left(self):
        if self.head.heading() != RIGHT and self.once_per_frame:
            self.head.setheading(LEFT)
            self.once_per_frame = False
    def right(self):
        if self.head.heading() != LEFT and self.once_per_frame:
            self.head.setheading(RIGHT)
            self.once_per_frame = False

    #TODO Extend snake
    def add_snake(self, position):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.segments.append(new_turtle)

    def extend_snake(self):
        self.add_snake(self.segments[-1].position())


    def reset(self):
        for segment in self.segments:
            segment.goto(2000,2000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

