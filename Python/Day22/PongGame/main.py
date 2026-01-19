from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle
from pong import Pong

import time

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
WINNING_SCORE = 2
PADDLE_MARGIN = 20
PADDLE_ONE_X = -int(SCREEN_WIDTH/2) + PADDLE_MARGIN
PADDLE_TWO_X = int(SCREEN_WIDTH/2) - PADDLE_MARGIN
PONG_SIZE = 20

screen = Screen()

screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor('black')
screen.title('My Pong Game')
screen.tracer(0)

paddle1 = Paddle(PADDLE_ONE_X)
paddle2 = Paddle(PADDLE_TWO_X)
pong = Pong()
scoreboard = Scoreboard()

game_status = 'on'

while game_status == 'on':

    screen.update()
    time.sleep(0.1)
    pong.move()

    if pong.distance(paddle1) < PONG_SIZE:
        pong.deflect(pong.heading(), 1)

    if pong.distance(paddle2) < PONG_SIZE:
        pong.deflect(pong.heading(), 2)

    pong.wall_deflect(pong.heading())

    if scoreboard.score1 == WINNING_SCORE or scoreboard.score2 == WINNING_SCORE:
        game_status = 'off'

    screen.listen()
    screen.onkeypress(key='Up', fun=paddle1.move_up)
    screen.onkeypress(key='Down', fun=paddle1.move_down)
    screen.onkeypress(key='w', fun=paddle2.move_up)
    screen.onkeypress(key='s', fun=paddle2.move_down)

screen.exitonclick()