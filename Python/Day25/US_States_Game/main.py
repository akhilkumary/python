from turtle import Turtle, Screen
import pandas as pd
import time

NUM_GUESSES = 5

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgpic('blank_states_img.gif')

game_status = 'on'
guesses = 0

t = Turtle()
t.penup()
t.hideturtle()

def game_over():
    t.goto(0,0)
    t.write(arg=f'GAME OVER!!!', move=False, align='center', font=('Courier', 12, 'normal'))
    
while game_status == 'on':
    screen.update()

    time.sleep(1)
    state = screen.textinput('US States Game', "Guess a state: ")
    df = pd.read_csv('50_states.csv')

    for idx, val in df["state"].items():
        if val == state:
            x_cor = df["x"][idx]
            y_cor = df["y"][idx]
            t.goto(x_cor, y_cor)
            t.pendown()
            t.write(arg=f'{state}', move=False, align='center', font=('Courier', 12, 'normal'))
            t.penup()
            break
        if idx == len(df["state"].to_list()) - 1 and df["state"][idx] != state:
            guesses += 1

    if guesses > NUM_GUESSES:
        game_status = 'off'
        game_over()

screen.exitonclick()

