import time
from turtle import Screen
import player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)
player = player.Player()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

