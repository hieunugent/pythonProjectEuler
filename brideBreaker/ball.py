from turtle import Turtle

class Ball:
    def __init__(self):
        self.ball = Turtle()
        self.ball.shape("circle")
        self.ball.color("red")
        self.ball.penup()
        self.ball.goto(0,-300)
    def speedup(self):
        self.speed(self.speed()+1)
    def move_ball_turnleft(self):
        self.ball.left(45)
    def move_ball_turnright(self):
        self.ball.right(45)
    def move_ball_forward(self):
        self.ball.forward(10)
    def move_ball_backward(self):
        self.ball.backward(10)