from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.create_paddle(x, y)


    def create_paddle(self, x, y):
        self.shape("square")
        self.shapesize(1, 5)
        self.color("white")
        self.penup()
        self.setheading(90)
        self.goto(x, y)

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.backward(20)
