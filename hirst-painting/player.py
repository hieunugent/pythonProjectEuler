STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.setheading(90)
        self.goto(STARTING_POSITION)
        
    def move_up(self):
        self.forward(20)
    def reset_player(self):
        self.goto(STARTING_POSITION)
        
    def finished_line(self):
        currentpos = self.ycor()
        if currentpos >= FINISH_LINE_Y:
            return True
        else:
            return False