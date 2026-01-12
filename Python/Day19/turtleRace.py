from turtle import Turtle, Screen
import random

GAP = 50
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400
START = -(SCREEN_WIDTH/2) + GAP

colors = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
turtles = []
NUM_TURTLES = len(colors)
global new_race

new_race = ''

def start_race():
    finish_line = 0
    while finish_line == 0:
        for j in range(NUM_TURTLES):
            turtles[j].fd(random.randint(0, int(GAP/3)))
        for i in range(NUM_TURTLES):
            if turtles[i].xcor() >= (-START + GAP):
                finish_line = 1
                global new_race 
                new_race = screen.textinput("Winner", f"Turtle {turtles[i].pencolor()} Wins!!")
        
def set_start_state():
    global new_race

    finish = Turtle()
    finish.hideturtle()
    finish.penup()
    finish.goto(-START + GAP, (SCREEN_HEIGHT/2))
    finish.right(90)
    finish.pensize(5)
    for _ in range(int((SCREEN_HEIGHT)/int(2*GAP/5))):
        finish.pendown()
        finish.fd(int(GAP/5))
        finish.penup()
        finish.fd(int(GAP/5))

    for i in range(NUM_TURTLES):
        turtles.append(Turtle('turtle'))
        turtles[i].color(colors[i])
        turtles[i].penup()
        turtles[i].goto(START - GAP, i*GAP - (SCREEN_HEIGHT/2) + GAP)
        
screen = Screen()

while new_race != 'q':
    set_start_state()
    screen.listen()
    screen.onkey(key='s', fun=start_race)
    
screen.exitonclick()
