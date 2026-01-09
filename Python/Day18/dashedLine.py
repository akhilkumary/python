from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

tim.color('red')
tim.shape('turtle')

for _ in range(0, 10):
    tim.fd(5)
    tim.pu()
    tim.fd(5)
    tim.pd()

screen.exitonclick()