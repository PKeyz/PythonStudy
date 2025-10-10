import time
from turtle import Screen
import player
import car_manager
import scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)
player = player.Player()
car = car_manager.CarManager()
scoreboard = scoreboard.Scoreboard()

screen.listen()

#player control buttons
screen.onkeypress(player.move_up, "w")
screen.onkeypress(player.move_up, "W")
screen.onkeypress(player.move_up, "Up")

#game
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_left()
    car.vanish()
    player.reset_pos()

    if player.ycor() == 300:
        scoreboard.increment_score()
        scoreboard.display()
        #car.increase_cars_chance()
        car.increase_cars_speed()

    for cars in car.all_cars:
        if cars.distance(player) < 10:
            player.turn_red()
            scoreboard.game_over()

screen.exitonclick()
