from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.speed("fastest")
        self.penup()
        self.left(90)
        self.goto(STARTING_POSITION)

    def move_up(self):
        y_new = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), y_new)

    def move_down(self):
        y_new = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), y_new)

    def reset_position(self):
        self.goto(STARTING_POSITION)

