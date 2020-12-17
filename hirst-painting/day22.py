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


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PING PONG GAME")

paddle = Turtle("square")
paddle.color("white")
paddle.penup()
paddle.shapesize(stretch_wid=5,stretch_len=1)
paddle.goto(350,0)

def  go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)
def  go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")






screen.exitonclick()