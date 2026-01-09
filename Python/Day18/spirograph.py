import turtle as t
import random

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_spirograph(size_of_graph):
    for _ in range(int(360 / size_of_graph)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_graph)

screen = t.Screen()
tim = t.Turtle()

t.colormode(255)
tim.speed('fastest')

draw_spirograph(1)

screen.exitonclick()