from turtle import Turtle

SCREEN_HEIGHT = 600
MARGIN = 20

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, int(SCREEN_HEIGHT/2) - MARGIN)
        self.pendown()
        self.hideturtle()
        self.write_score()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write_score()
    
    def write_score(self):
        self.write(arg=f'Score: {self.score} ', move=False, align='center', font=('Arial', 12, 'normal'))
        
    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f'GAMEOVER! Your score is: {self.score}.', move=False, align='center', font=('Arial', 12, 'normal'))
        