from turtle import Screen, bgcolor
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

screen.listen()
screen.onkey(player.go_left, "Left")
screen.onkey(player.go_right, "Right")
bridge = Bridge()
bridge.create_all_bridge()

game_is_running = True

ball.rotate_left(45)
ball.rotate_left(45)

while game_is_running:
    screen.update()
    ball.move()
    if bridge.check_match(ball.location()):      
        ball.rotate_left(45) 
    if player.collision(ball.location()):
        ball.rotate_right(45)    
    if ball.location()[0]>=400:
        ball.rotate_left(45)
    if ball.location()[0]<=-400:
        ball.rotate_right(45)
    if ball.location()[1]>=400:
        ball.rotate_right(45)
    time.sleep(0.1)
