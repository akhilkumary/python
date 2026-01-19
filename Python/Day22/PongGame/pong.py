from turtle import Turtle


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
PADDLE_MARGIN = 20
PADDLE_ONE_X = -int(SCREEN_WIDTH/2) + PADDLE_MARGIN
PADDLE_TWO_X = int(SCREEN_WIDTH/2) - PADDLE_MARGIN

PONG_DEFLECT_Y = int(SCREEN_HEIGHT/2) - PADDLE_MARGIN
STEP = 5

class Pong(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.setheading(30)
        # self.speed('fastest')
        
    def move(self):
        self.forward(STEP)

    def deflect(self, angle, paddle):
        self.setheading(180 - angle)
        # if paddle == 1:
        #     self.setheading((angle - 90) % 360)
        # else:
        #     self.setheading((360 - 2*angle) % 360) 

    def wall_deflect(self, angle):
        if self.xcor() > PADDLE_ONE_X and self.xcor() < PADDLE_TWO_X and abs(abs(self.ycor()) - PONG_DEFLECT_Y) < 20:
            self.setheading(360 - angle)