from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=800, height=600)

screen.tracer(0)

screen.bgcolor("black")
screen.title("Pong")

ball = Ball()

l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)

l_scoreboard = Scoreboard(-100, 260)
r_scoreboard = Scoreboard(100, 260)

screen.listen()

screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")

screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")


is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    ball.move_ball()
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.reset_position()
        l_scoreboard.increase_l_score()
    if ball.xcor() < -380:
        ball.reset_position()
        r_scoreboard.increase_r_score()
screen.exitonclick()
