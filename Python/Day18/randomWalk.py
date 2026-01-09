from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()

colors = ['dark violet', 'medium blue', 'firebrick', 'yellow', 'cyan', 'medium turquoise', 'black', 'red', 'gold', 'deep pink', 'dark olive green']
heading = [0, 90, 180, 270]

tim.shape('turtle')

for i in range(200):
    tim.color(random.choice(colors))
    tim.seth(random.choice(heading)) 
    tim.pensize(10)
    tim.fd(20)

screen.exitonclick()

