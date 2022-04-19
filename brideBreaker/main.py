from turtle import Screen
import time

from player import Player 
from bridge import Bridge
from ball import Ball
screen = Screen()
screen.setup(width=1200, height=1000)

screen.tracer(0)
player = Player()
ball  = Ball()

screen.listen()
screen.onkey(player.go_left, "Left")
screen.onkey(player.go_right, "Right")
bridge = Bridge()
bridge.create_all_bridge()

game_is_running = True

ball.rotate_left()
ball.rotate_left()

while game_is_running:
    screen.update()
    ball.move()
    if bridge.check_match(ball.location()):
        bridge.remove_bridge(bridge.check_match(ball.location()))
        ball.rotate_left() 
    if player.collision(ball.location()):
        ball.rotate_right()
        ball.rotate_right()
    time.sleep(0.1)
