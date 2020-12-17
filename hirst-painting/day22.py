# day 22 goal is make ping pong gamegi
# Create the screen 
# Create and move a paddle
# create another paddle
# create a ball and make it move
# detect collition with wall and bounce
# detect collition with paddle
# detect when paddle misses
#  keep score

from turtle import Screen, Turtle

from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PING PONG GAME")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))



    
    
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
game_is_on = True
while game_is_on:
    screen.update()
    




screen.exitonclick()