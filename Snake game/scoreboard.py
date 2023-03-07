from turtle import Turtle
ALIGMENT = "center"
FONT = ("Arial", 24, "normal")
class scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        with open("data.txt", mode="r") as file:
            value = file.read()
            self.high_score = int(value)
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.write(f"The score is {self.score}", align=ALIGMENT, font=FONT)
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"The score is {self.score} High Score: {self.high_score}", align=ALIGMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()