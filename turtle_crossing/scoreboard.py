from turtle import Turtle

FONT = ("Courier", 24, "normal")
LEFT = "left"
CENTER = "center"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.penup()
        self.goto(-270, 270)
        self.update_scoreboard()
        self.hideturtle()

    def add_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level = {self.score}", move=False, align=LEFT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=CENTER, font=FONT)