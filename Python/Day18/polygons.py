from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()

colors = ['dark violet', 'medium blue', 'firebrick', 'yellow', 'cyan', 'medium turquoise', 'black', 'red', 'gold', 'deep pink', 'dark olive green']

tim.shape('turtle')

for i in range(3, 13):
    angle = 360/i
    tim.color(random.choice(colors))

    for x in range(i):
        tim.fd(50)
        tim.left(angle)
    
screen.exitonclick()