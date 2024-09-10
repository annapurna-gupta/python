from turtle import Screen
from create_paddle import Paddle
from ball import Ball


screen = Screen()
screen.tracer(1)
r_p = Paddle((360, 0))
l_p = Paddle((-360, 0))
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
    ball.speed(-1)
    screen.update()
    ball.move()
    if ball.ycor() > 278 or ball.ycor() < -278:
        ball.bounce()

screen.exitonclick()
