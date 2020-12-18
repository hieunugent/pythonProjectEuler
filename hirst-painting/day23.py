#  build turtle crossing game 
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboardcs import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
scoreboard = Scoreboard()
gamer  = Player()
car_manager =CarManager()
screen.listen()
screen.onkey(gamer.move_up, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    # detect collition with car
    for car in car_manager.all_cars:
        if car.distance(gamer)<20:
            game_is_on=False
            scoreboard.game_over()
    if gamer.finished_line():
        gamer.reset_player() 
        scoreboard.levelup()


screen.exitonclick()             