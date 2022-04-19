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
    def rotate_left(self):
        self.ball.left(45)
    def rotate_right(self):
        self.ball.right(45)
    def move(self):
        self.ball.forward(10)
    def location(self):
        return (self.ball.pos())
