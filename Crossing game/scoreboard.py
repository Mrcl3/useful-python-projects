FONT = ("Courier", 20, "normal")
from turtle import Turtle
ALIGNMENT = "left"
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 1
        self.update_scoreboard()

    def point(self):
        self.score +=1
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(-280,250)
        self.write(f"Current level is: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)
