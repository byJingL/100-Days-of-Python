from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.car_list = []
        self.move_speed = 0.1
        self.add_car()

    def add_car(self):
        # (create 1 car)/(6 round)
        if random.randint(1, 6) == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            y = random.randint(-250, 250)
            new_car.goto(300, y)
            self.car_list.append(new_car)

    def move(self):
        for car in self.car_list:
            car.backward(MOVE_INCREMENT)

    def level_up(self):
        print(self.move_speed)
        self.move_speed *= 0.8
