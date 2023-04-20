from turtle import Turtle

INITIAL_NUMBER_OF_SEGMENTS = 3
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def add_segment(self, position):
        seg = Turtle(shape="square")
        seg.color("white")
        seg.penup()
        seg.goto(position)
        self.segments.append(seg)

    def create_snake(self):
        for index in range(0, INITIAL_NUMBER_OF_SEGMENTS):
            self.add_segment((-20 * index, 0))

    def move(self):
        for index_ext in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[index_ext - 1].xcor()
            new_y = self.segments[index_ext - 1].ycor()
            self.segments[index_ext].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def extend(self):
        self.add_segment(self.segments[- 1].position())
