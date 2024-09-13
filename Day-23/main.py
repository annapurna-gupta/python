import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
score = Scoreboard()
screen.listen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car1 = CarManager()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car1.create_car()
    car1.move_car()

    for car in car1.all_cars:
        if car.distance(player) < 25:
            game_is_on = False
            score.gameover()

    if player.is_in_finish_line():
        player.goto(0, -280)
        car1.level_up()
        score.clear()
        score.increase_level()


screen.exitonclick()
