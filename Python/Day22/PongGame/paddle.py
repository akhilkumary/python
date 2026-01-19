from turtle import Turtle

SCREEN_HEIGHT = 600
MARGIN = 40

class Paddle(Turtle):
    def __init__(self, xcor):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.penup()
        self.goto(xcor, 0)
        self.left(90)

    def move_up(self):
        if self.ycor() < int(SCREEN_HEIGHT/2) - MARGIN:
            self.setheading(90)
            self.forward(20)

    def move_down(self):
        if self.ycor() > -int(SCREEN_HEIGHT/2) + MARGIN:
            self.setheading(90)
            self.backward(20)
