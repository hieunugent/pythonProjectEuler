from turtle import Screen
import time

from player import Player 
from bridge import Bridge
from ball import Ball
screen = Screen()
screen.setup(width=1000, height=1000)

screen.tracer(0)
player = Player()
ball  = Ball()

screen.listen()
screen.onkey(player.go_left, "Left")
screen.onkey(player.go_right, "Right")
bridge = Bridge()
bridge.create_bridge()

game_is_running = True
while game_is_running:
    screen.update()
    ball.move_ball_turnleft()
    
    ball.move_ball_forward()
   
    time.sleep(0.1)
    
