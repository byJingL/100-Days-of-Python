import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(player.move, "w")

scoreboard = Scoreboard()
scoreboard.score_display()

cars = CarManager()
game_is_on = True

# n = 0
while game_is_on:
    time.sleep(cars.move_speed)
    screen.update()
    # if n % 6 == 0:
    #     cars.add_car()
    cars.add_car()  # 在class里实现(create 1 car)/(6 round)
    cars.move()
    # n += 1

    # Detect the collision with car
    for each_car in cars.car_list:
        if player.distance(each_car) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect the collision with edge
    if player.is_at_fish_line():
        player.reset()
        cars.level_up()
        scoreboard.count_level()

screen.exitonclick()



