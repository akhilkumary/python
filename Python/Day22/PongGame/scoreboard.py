from turtle import Turtle

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
STEP = 10
MARGIN = 80

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        
        self.hideturtle()
        self.color('white')
        self.draw_board()

        self.goto(0, (int(SCREEN_HEIGHT/2) - MARGIN))
        self.update_score()

    def draw_board(self):
        self.penup()
        self.goto(0, -int(SCREEN_HEIGHT/2))
        self.pensize(4)
        self.setheading(90)
        for _ in range(0, int(SCREEN_HEIGHT/STEP)):
            self.pendown()
            self.forward(STEP)
            self.penup()
            self.forward(STEP)

        self.setheading(0)

    def update_score(self):
        self.write(arg=f'{self.score1}     {self.score2}', move=False, align='center', font=('Arial', 40, 'normal'))

    def increase_score1(self):
        self.score1 += 1
        self.update_score()

    def increase_score2(self):
        self.score2 += 1
        self.update_score()

