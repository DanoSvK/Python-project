from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []


def create_turtles():
    y = -70
    i = 0
    t = Turtle()
    for color in colors:
        t = Turtle()
        t.shape("turtle")
        t.color(color)
        t.penup()
        t.goto(x=-230, y=y)
        turtles.append(t)
        y += 30
        i += 1



def race():
    create_turtles()
    is_race_on = False
    if user_bet:
        is_race_on = True
    while is_race_on:
        for turtle in turtles:
            random_int = random.randint(0, 10)
            turtle.forward(random_int)
            print(turtle.xcor() == 250)
            if turtle.xcor() >= 230:
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You have won! The {winning_color} turtle is the winner.")
                else:
                    print(f"You have lost! The {winning_color} turtle is the winner.")
                is_race_on = False


race()
