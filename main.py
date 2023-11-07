import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
FINISH_LINE_Y = 280
screen = Screen()
screen.title("Cross the Turtle")
screen.setup(width=600, height=600)
screen.tracer(0)
player=Player()
Car=CarManager()
score=Scoreboard()
game_is_on = True
screen.listen()
screen.onkey(player.move_forward,"Up")
while game_is_on:

    time.sleep(0.1)
    if player.ycor()>FINISH_LINE_Y:
        player.movement()
        Car.car_speed+=10
        Car.car_movement()
        score.increase_level()

    screen.update()
    Car.car()
    Car.car_movement()
    for car in Car.cars:
       if player.distance(car)<18:
           game_is_on=False
           score.game_over()

screen.exitonclick()
