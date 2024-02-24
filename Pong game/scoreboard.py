from turtle import Turtle
FONT = ('Arial', 24, 'normal')
class Scoreboard(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.create_l_score(x, y)
        self.create_r_score(x, y)
    def create_l_score(self, x, y):
        self.goto(x, y)
        self.write(f"{self.l_score}", align="center", font=FONT)

    def create_r_score(self, x, y):
        self.goto(x, y)
        self.write(f"{self.r_score}", align="center", font=FONT)

    def increase_l_score(self):
        self.l_score += 1
        self.clear()
        self.write(f"{self.l_score}", align="center", font=FONT)

    def increase_r_score(self):
        self.r_score += 1
        self.clear()
        self.write(f"{self.r_score}", align="center", font=FONT)
