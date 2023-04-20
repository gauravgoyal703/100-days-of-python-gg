from turtle import Turtle

NORMAL_ = ('Courier', 20, 'normal')
CENTER = 'center'


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.update_scoreboard()
        self.hideturtle()

    def add_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score} High Score: {self.high_score }", move=False, align=CENTER, font=NORMAL_)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=CENTER, font=NORMAL_)