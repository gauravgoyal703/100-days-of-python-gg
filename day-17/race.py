import random
from turtle import Turtle, Screen

colors = ["red", "green", "yellow", "blue", "orange", "purple"]
is_race_on = False

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")

race_turtles = []
initial_location = -80
for color in colors:
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(color)
    tim.goto(-240, initial_location)
    initial_location += 40
    race_turtles.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for race_turtle in race_turtles:
        race_turtle.forward(random.randint(0, 10))
        if race_turtle.xcor() > 230:
            is_race_on = False;
            race_win_color = race_turtle.color()[1]
            message = "You lose."
            if race_win_color == user_bet:
                message = "You win."
            print(f"{race_win_color} color turtle wins. {message}")


screen.exitonclick()