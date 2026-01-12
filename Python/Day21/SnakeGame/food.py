from turtle import Turtle
import random

MARGIN = 20
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-int((SCREEN_WIDTH/2)) + MARGIN, int(SCREEN_WIDTH/2) - MARGIN), random.randint(-int(SCREEN_HEIGHT/2) + MARGIN, int(SCREEN_HEIGHT/2) - MARGIN))
