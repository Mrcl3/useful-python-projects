from turtle import Turtle
POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in POSITION:
            self.add_segment(position)


    def move(self):
        for item in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[item - 1].xcor()
            new_y = self.segments[item - 1].ycor()
            self.segments[item].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() !=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() !=UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() !=LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() !=RIGHT:
            self.head.setheading(LEFT)

    def add_segment(self, position):
        snake = Turtle()
        snake.shape("square")
        snake.color("white")
        snake.speed("fastest")
        snake.penup()  # don't draw when turtle moves
        snake.goto(position)  # move the turtle to a location
        # turtle.showturtle()           #make the turtle visible
        # turtle.pendown()              #draw when the turtle moves
        self.segments.append(snake)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
