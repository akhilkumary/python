from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)

PADDLE_RIGHT_X = 350

paddle1 = Paddle(-PADDLE_RIGHT_X)
paddle2 = Paddle(PADDLE_RIGHT_X)
ball = Ball()
scoreboard = Scoreboard()

game_status = 'on'

while game_status == 'on':
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Wall Collission
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Paddle Collission
    # Right
    if ball.distance(paddle2) < 50 and ball.xcor() > 340 or ball.distance(paddle1) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    # Paddle misses the ball
    if ball.xcor() < -380 or ball.xcor() > 380:
        if ball.xcor() < 0:
            scoreboard.increase_score2()
        else:
            scoreboard.increase_score1()
        ball.reset_ball()

    screen.listen()
    screen.onkey(paddle1.move_up, 'Up')
    screen.onkey(paddle1.move_down, 'Down')
    screen.onkey(paddle2.move_up, 'w')
    screen.onkey(paddle2.move_down, 's')

screen.exitonclick()