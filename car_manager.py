COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random
class CarManager():
    def __init__(self) :
        self.cars=[]
        self.car_speed=STARTING_MOVE_DISTANCE
    def car(self):
        a=random.randint(1,6)
        if a==6:
           new_car=Turtle()
           new_car.shape("square")
           new_car.shapesize(stretch_wid=1,stretch_len=2)
           new_car.penup()
           new_car.color(random.choice(COLORS))
           rand_y=random.randint(-250,250)
           new_car.goto(300,rand_y)
           self.cars.append(new_car)
    def car_movement(self):
        for car in self.cars:
            car.backward(self.car_speed)

