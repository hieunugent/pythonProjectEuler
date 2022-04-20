
from turtle import Screen 
import time

from player import Player 
from bridge import Bridge
from ball import Ball
screen = Screen()
screen.setup(width=1200, height=1000)
screen.bgcolor("grey")
screen.tracer(0)
player = Player()
ball  = Ball()
bridge = Bridge()

screen.listen()
screen.onkey(player.go_left, "Left")
screen.onkey(player.go_right, "Right")
game_is_running = True
ball.rotate_left(45)
ball.rotate_left(45)

while game_is_running:
    screen.update()
    ball.move()
    if bridge.check_match(ball.location()):      
        ball.rotate_left(60) 
    if player.collision(ball.location()):
        ball.rotate_right(69)    
    if ball.location()[0]>=450:
        ball.rotate_left(65)
    elif ball.location()[0]<=-450:
        ball.rotate_right(65)
    elif ball.location()[1]>=450:
        ball.rotate_right(65)
    elif ball.location()[1]<=-450:
        ball.rotate_left(65)
    time.sleep(0.1)
