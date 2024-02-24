from turtle import Turtle
FONT = ("Courier", 24, "normal")
SCORE = 0

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = SCORE
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def game_over(self):
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        self.write(f"Game over", align="center", font=FONT)