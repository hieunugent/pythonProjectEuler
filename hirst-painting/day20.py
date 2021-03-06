# build snake game 
#Create  snake 
# Move the snake
# control snake
# detect collition with food
# create a scoreboard
# detect collition with wall
# dectec collition with tail 

from  turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)  
    snake.move()

    # detect collition with food 
    if snake.head.distance(food)< 15:
        food.refresh()
        snake.extend()
        score.increase_score()
     # detect colliition with wall   
    if snake.head.xcor() >=300 or snake.head.xcor() <=-300 or snake.head.ycor() >= 300 or snake.head.ycor() <=-300:
            score.reset()
            snake.reset()
    # detect collition with tail
    for segment in snake.segments[1::1]:
       if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()


screen.exitonclick()