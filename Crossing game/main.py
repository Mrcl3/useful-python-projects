import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

cars = CarManager()
player = Player()
scoreboard = Scoreboard()

screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")

game_is_on = True
counter = 0
while game_is_on:

    time.sleep(0.1)
    screen.update()
    if counter%7 ==0:
        cars.create_car()
    cars.move()
    counter += 1

    #detect if the player reaches the end
    if player.ycor() > 280:
        player.reset_position()
        scoreboard.point()
        scoreboard.update_scoreboard()
        cars.increase_speed()
    if player.ycor() < -290:
        scoreboard.game_over()
        game_is_on = False

    # Detect crash with a car
    for item in cars.all_cars:
        if player.distance(item) < 15:
            scoreboard.game_over()
            game_is_on = False
            screen.exitonclick()


