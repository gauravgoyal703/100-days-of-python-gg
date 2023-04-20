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
screen.onkey(player.move, "Up")

scoreboard = Scoreboard()
car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move()

    # Check if car reaches the end
    car_manager.check_car_hits_wall()

    # Check if player collides with cars()
    if car_manager.collides(player):
        scoreboard.game_over()
        game_is_on = False

    # Check if player is at finish
    if player.is_at_finish():
        scoreboard.add_score()
        player.reset()
        car_manager.increment_speed()



screen.exitonclick()