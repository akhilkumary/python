from turtle import Turtle, Screen
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500
SEGMENT_LENGTH = 5
MARGIN = 40

class Snake:
    def __init__(self):
        self.segments = 3
        self.snake_body = []
        self.food = Food()
        self.score = 0

        for i in range(self.segments):
            self.snake_body.append(Turtle('square'))
            self.snake_body[i].penup()
            self.snake_body[i].speed('fastest')
            if i > 0:
                self.snake_body[i].setposition(self.snake_body[i-1].xcor() - 2*SEGMENT_LENGTH, self.snake_body[i-1].ycor())
        
        self.head = self.snake_body[0]
        self.food.food_produce()

    def auto_move(self):
        self.head.forward(int(3*SEGMENT_LENGTH))
        for i in range(0, self.segments - 1):
            s = self.segments - i - 1
            if s > 0:
                x_cor = self.snake_body[s-1].xcor()
                y_cor = self.snake_body[s-1].ycor()
                print(f"S: {s}")
                self.snake_body[s].setposition(x_cor, y_cor)
                self.snake_body[s].showturtle()
    
    def move_left(self):
        if self.snake_body[0].heading() != 0:
            self.snake_body[0].setheading(180)

    def move_right(self):
        if self.snake_body[0].heading() != 180:
            self.snake_body[0].setheading(0)

    def move_up(self):
        if self.snake_body[0].heading() != 270:
            self.snake_body[0].setheading(90)

    def move_down(self):
        if self.snake_body[0].heading() != 90:
            self.snake_body[0].setheading(270)

    def increase_length(self):
        self.snake_body.append(Turtle('square'))
        self.snake_body[-1].hideturtle()
        self.snake_body[-1].penup()
        self.snake_body[-1].speed('fastest')

    def food_collission(self):
        if (abs(self.head.xcor() - self.food.food.xcor()) < 15) and (abs(self.head.ycor() - self.food.food.ycor()) < 15):
            print(f"XCOR: {abs(self.head.xcor() - self.food.food.xcor())} and YCOR: {abs(self.head.ycor() - self.food.food.ycor())}")
            self.food.food_produce()
            self.score += 1
            self.segments += 1
            self.increase_length()
            print(f"Segments: {self.segments}")

    def wall_collission(self):
        if abs(self.head.xcor() - int(SCREEN_WIDTH/2)) < 10 and abs(self.head.ycor() - int(SCREEN_HEIGHT/2)) < 10:
            return False
        return True

class Food:
    def __init__(self):
        self.food = Turtle("circle")
        self.food.shapesize(0.5, 0.5)
        self.food.penup()

    def food_produce(self):
        self.food.hideturtle()
        self.food.teleport(random.randint(-(int(SCREEN_WIDTH/2) - MARGIN), (int(SCREEN_WIDTH/2) - MARGIN)), random.randint(-(int(SCREEN_HEIGHT/2) - MARGIN), (int(SCREEN_HEIGHT/2) - MARGIN)))
        self.food.showturtle()


# UI - Screen setup - Scoreboard position
# snake start, initial food point
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

snake = Snake()
game_status = 'on'

while game_status == 'on':
    # Snake auto movement each instant
    snake.auto_move()
    snake.food_collission()
    if not snake.wall_collission():
        break
    screen.listen()
    # Keyboard Controls for controlling the snake
    screen.onkeypress(key='w', fun=snake.move_up)
    screen.onkeypress(key='s', fun=snake.move_down)
    screen.onkeypress(key='d', fun=snake.move_right)
    screen.onkeypress(key='a', fun=snake.move_left)

screen.exitonclick()

# Score update when snake eats food
# snake's length increase

# detect snake collission with it's body. final score display

# mage/snake goes out of the screen - pops up the other side