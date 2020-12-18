FONT = ("Courier", 24, "normal")
ALINEMENT = "center"
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.level =0
        self.penup()
        self.update_scoreboard()
        self.hideturtle()
    def update_scoreboard(self):
        self.clear()
        self.goto(-280,270)
        self.write(f"Level: {self.level}", font=FONT) 
    def levelup(self):
        self.level +=1
        self.update_scoreboard()
    def resetlevel(self):
        self.level =0
        self.update_scoreboard()
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALINEMENT, font=FONT)
        
   
        
