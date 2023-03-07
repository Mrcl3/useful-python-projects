from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import scoreboard
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)



snake = Snake()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
food = Food()
scoreboard = scoreboard()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #Detection collision with food
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()


    #Detect collission with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() <-280:
        scoreboard.reset()
        snake.reset()

    #Detect if the snakes collide with the tail
    for item in snake.segments:
        if item == snake.head:
            pass
        elif snake.head.distance(item) < 10:
            scoreboard.reset()
            snake.reset()






screen.exitonclick()