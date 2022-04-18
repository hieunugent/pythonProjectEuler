from turtle import Turtle
COLORS = ["red", "blue", "green", "yellow", "orange", "purple"]
class Bridge:
    def __init__(self):
        self.all_bridge=[]
    def create_bridge(self):
        new_bridge = Turtle("square")
        new_bridge.shapesize(stretch_wid=1, stretch_len=3)
        new_bridge.penup()
        new_bridge.color(COLORS[0])
        new_bridge.goto(-200,200)
        self.all_bridge.append(new_bridge)