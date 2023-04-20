from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
NUMBER_OF_CARS = 15


class CarManager:

    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE
        for _ in range(0, NUMBER_OF_CARS):
            self.add_car()

    def add_car(self):
        car = Turtle()
        car.shape("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(random.choice(COLORS))
        car.penup()
        car.setheading(180)
        car.setposition(random.randint(-250, 270), random.randint(-250, 250))
        self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.forward(self.move_distance)

    def increment_speed(self):
        self.move_distance += MOVE_INCREMENT

    def check_car_hits_wall(self):
        for car in self.cars:
            if car.xcor() < -280:
                car.setposition(280, random.randint(-250, 250))
                car.color(random.choice(COLORS))

    def collides(self, player):
        for car in self.cars:
            if car.distance(player) < 20:
                return True
        return False
