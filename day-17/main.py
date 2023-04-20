import turtle as t
import random

timmy_the_turtle = t.Turtle()
timmy_the_turtle.color("red", "blue")
timmy_the_turtle.shape("turtle")
#timmy_the_turtle.pensize(5)
timmy_the_turtle.speed("fastest")
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

#sides = 3
#for _ in range(8):
#    for _ in range(sides):
#        random_num = round(sides/(sides + 2), 2)
#        tup = (random_num, random_num, random_num)
#        timmy_the_turtle.pencolor(tup)
#        timmy_the_turtle.forward(100)
#        timmy_the_turtle.right(360 / sides)
#    sides += 1

########### Challenge 4 - Random Walk ########
#colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
#directions = [0, 90, 180, 270]


#for _ in range(100):
    #timmy_the_turtle.forward(20)
    #timmy_the_turtle.setheading(random.choice(directions))
    #random_num = random.randint(0, 255)
    #timmy_the_turtle.pencolor(random_color())
    #timmy_the_turtle.pencolor(choice(colours))

########### Challenge - 5 ########
angle = 5
rotate = 4
for _ in range((360 * rotate) // angle):
    timmy_the_turtle.setheading(timmy_the_turtle.heading() + angle)
    timmy_the_turtle.circle(100)
    timmy_the_turtle.pencolor(random_color())



screen = t.Screen()
screen.exitonclick()