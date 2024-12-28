from turtle import Screen, Turtle
import time

from ball import Ball
from paddle import Paddle
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor('black')
screen.setup(800, 600)
screen.title("Pong Game")
screen.tracer(0)
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

ball = Ball()

screen.listen()

screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")
scoreboard = ScoreBoard()
game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    right_paddle.move()
    left_paddle.move()
    screen.update()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with r_paddle
    if ball.distance(right_paddle) < 50 and 320 < ball.xcor() < 340 or ball.distance(left_paddle) < 50 and -340 < ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 400:
        ball.reset()
        right_paddle.reset()
        left_paddle.reset()
        scoreboard.add_l_point()

    if ball.xcor() < -400:
        ball.reset()
        right_paddle.reset()
        left_paddle.reset()
        scoreboard.add_r_point()

screen.exitonclick()