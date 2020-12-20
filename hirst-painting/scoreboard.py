
from turtle import Turtle

ALINEMENT = "center"
FONT = ("Arial", 24, "normal")

import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'data.txt')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(my_file, mode="r") as data:
           self.highscore =  int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.update_scoreboard()
        self.hideturtle()
        
    def update_scoreboard(self):
        self.write(f"Score: {self.score}  High Score: {self.highscore}", align=ALINEMENT, font=FONT) 
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALINEMENT, font=FONT)
    def  increase_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()
    def reset(self):
        if (self.highscore < self.score ):
            self.highscore= self.score
            with open(my_file, mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.clear()
        self.update_scoreboard()