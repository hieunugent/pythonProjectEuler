from turtle import Turtle
SPEED_MOVING= 20
class Ball:
    def __init__(self):
        self.ball = Turtle()
        self.ball.penup()
        self.ball.shape("circle")
        self.ball.color("black")
        
        self.ball.goto(0,-300)
        
    def speedup(self):
        self.speed(self.speed()+1)
    def rotate_left(self, degree):
        self.ball.left(degree)
    def rotate_right(self, degree):
        self.ball.right(degree)
    def move(self):
        self.ball.forward(SPEED_MOVING)
    def location(self):
        return (self.ball.pos())
