from turtle import Turtle

SCREEN_HEIGHT = 600
MARGIN = 20

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = self.get_highscore()
        self.color('white')
        self.penup()
        self.goto(0, int(SCREEN_HEIGHT/2) - MARGIN)
        self.pendown()
        self.hideturtle()
        self.write_score()

    def get_highscore(self):
        with open('highscore.txt', mode='r') as highscore_file:
            contents = highscore_file.read()
            if contents != '':
                high_score = int(contents)
            else:
                return 0
        return high_score
    
    def update_highscore(self):
        with open('highscore.txt', mode='w') as highscore_file:
            highscore_file.write(str(self.highscore))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write_score()
    
    def write_score(self):
        self.write(arg=f'Score: {self.score} Highscore: {self.highscore}', move=False, align='center', font=('Arial', 12, 'normal'))
        
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg=f'GAMEOVER! Your score is: {self.score}.', move=False, align='center', font=('Arial', 12, 'normal'))
        
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        
        high_score_on_file = self.get_highscore()
        if self.highscore > high_score_on_file:
            self.update_highscore()

        self.score = 0
        self.clear()
        self.write_score()