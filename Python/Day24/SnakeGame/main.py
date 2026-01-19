from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

import time

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
MARGIN = 20

screen = Screen()

screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

game_status = 'on'

while game_status == 'on':
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Food Collission
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.update_score()
        snake.extend()
        
    # Wall collission
    if (snake.head.xcor() > (int(SCREEN_WIDTH/2) - MARGIN)) or (snake.head.xcor() < (-int(SCREEN_WIDTH/2) + MARGIN)) or (snake.head.ycor() > (int(SCREEN_HEIGHT/2) - MARGIN)) or (snake.head.ycor() < (-int(SCREEN_HEIGHT/2) + MARGIN)):
        scoreboard.reset()
        snake.reset()

    # Tail collission
    # for i in range(1, snake.segments):
    #     if snake.head.distance(snake.snake[i]) < 10:
    #         game_status = 'off'
    #         scoreboard.game_over()

    for seg in snake.snake[1:]:
        if snake.head.distance(seg) < 10:
            scoreboard.reset()
            snake.reset()
            
    screen.listen()
    screen.onkeypress(key='w', fun=snake.move_up)
    screen.onkeypress(key='s', fun=snake.move_down)
    screen.onkeypress(key='d', fun=snake.move_right)
    screen.onkeypress(key='a', fun=snake.move_left)


screen.exitonclick()
