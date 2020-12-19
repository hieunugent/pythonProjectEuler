
from turtle import Turtle
ALINEMENT = "center"
FONT = ("Arial", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.update_scoreboard()
        self.hideturtle()
        
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALINEMENT, font=FONT) 
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALINEMENT, font=FONT)
    def  increase_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()
    def reset(self):
        self.score = 0
        self.clear()
        self.update_scoreboard()