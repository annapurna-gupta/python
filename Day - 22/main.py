from turtle import Screen
from create_paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
score = Scoreboard()
screen.tracer(0)
r_p = Paddle((350, 0))
l_p = Paddle((-350, 0))
screen.title("Pong Game")
screen.setup(800, 600)
screen.bgcolor("black")
ball = Ball()
screen.listen()

screen.onkey(r_p.go_up, "Up")
screen.onkey(r_p.go_down, "Down")
screen.onkey(l_p.go_up, "w")
screen.onkey(l_p.go_down, "s")

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 278 or ball.ycor() < -278:

        ball.bounce_y()

    if ball.distance(r_p) < 50 and ball.xcor() > 330 or ball.distance(l_p) < 50 and ball.xcor() > -330:
        ball.bounce_x()

    if ball.xcor() > 400:
        score.l_point()
        ball.reset_position()

    if ball.xcor() < -400:
        score.r_point()
        ball.reset_position()

screen.exitonclick()
