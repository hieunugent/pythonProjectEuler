from turtle import Turtle
COLORS = ["red", "blue", "green", "yellow", "orange", "purple", "pink"]
class Bridge:
    def __init__(self):
        self.all_bridge=[]
    def create_bridge(self, x, y, color):
        new_bridge = Turtle("square")
        new_bridge.shapesize(stretch_wid=1, stretch_len=3)
        new_bridge.penup()
        new_bridge.color(COLORS[color])
        new_bridge.goto(x, y)
        self.all_bridge.append(new_bridge)
    def create_all_bridge_row(self, y=0):
        x = -400
        for i in range(0, 1400, 100):
            self.create_bridge(x,y, i//200)
            x += 65        
    def create_all_bridge_col(self):
        y = 0
        for line in range(1, 14, 1):
            self.create_all_bridge_row(y)
            y += 30 
    def create_all_bridge(self):
        self.create_all_bridge_col()
        print(self.all_bridge)
    def remove_bridge(self, index):
        self.all_bridge[index].reset()
    def bridge_location(self, index):
        location = self.all_bridge[index].pos()
        return location
    def check_match(self, ball_location):
        for i in range(len(self.all_bridge)):
            if abs(self.bridge_location(i)[0]- ball_location[0])<= 30 and abs(self.bridge_location(i)[1]- ball_location[1])<=30:
                self.remove_bridge(i)
                return True
        return False
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             