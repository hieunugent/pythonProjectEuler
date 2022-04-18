from turtle import Turtle
STARTING_POSITION = (0,-400)
MOVE_DISTANCE = 10

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.color("gray")
        self.penup()
        self.goto(STARTING_POSITION)
        self.speed(0)
        
        
    def go_left(self):
        self.backward(MOVE_DISTANCE)
        
    def go_right(self):
        self.forward(MOVE_DISTANCE)
        
   
        
    
            
   