from turtle import Turtle
ALINEMENT = "center"
FONT = ("Arial", 90, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.lscore = 0
        self.rscore = 0
        self.color("white")
        self.penup()
        self.update_scoreboard()
        self.hideturtle()
        
    def update_scoreboard(self):
        self.clear()
        self.goto(-100,200)
        self.write(f"{self.lscore}", align=ALINEMENT, font=FONT) 
        self.goto(100,200)
        self.write(f"{self.rscore}", align=ALINEMENT, font=FONT) 
        
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALINEMENT, font=FONT)
    def  increase_lscore(self):
        self.lscore +=1
        self.update_scoreboard()
        
    def  increase_rscore(self):
        self.rscore +=1
        self.update_scoreboard()