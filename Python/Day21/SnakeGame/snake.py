from turtle import Turtle

SEGMENT_LENGTH = 20

class Snake:
    def __init__(self):
        self.segments = 3
        self.snake = []
        self.createsnake()
        self.head = self.snake[0]

    def createsnake(self):
        for i in range(self.segments):
            self.add_segment(i)

    def add_segment(self, pos):
        self.snake.append(Turtle('square'))
        self.snake[pos].color('white')
        self.snake[pos].penup()
        if pos > 0:
            self.snake[pos].setposition(self.snake[pos-1].xcor() - SEGMENT_LENGTH, self.snake[pos-1].ycor())

    def extend(self):
        self.segments += 1
        self.add_segment(self.segments-1)

    def move(self):
        for i in range(self.segments):
            s = self.segments - i - 1
            if s > 0:
                cor = self.snake[s - 1].pos()
                self.snake[s].goto(cor)
        self.head.forward(SEGMENT_LENGTH)

    def move_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def move_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def move_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def move_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)