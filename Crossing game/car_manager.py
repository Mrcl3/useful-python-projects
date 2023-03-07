COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random

class CarManager():

    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        car = Turtle()
        car.shape("square")
        car.shapesize(1, 2)
        car.penup()
        random_color = random.choice(COLORS)
        car.color(random_color)
        y_pos = random.randint(-250,250)
        car.goto(320, y_pos)
        self.all_cars.append(car)

    def move(self):
        for item in self.all_cars:
            item.backward(self.speed)

    def increase_speed(self):
        self.speed = self.speed + MOVE_INCREMENT


