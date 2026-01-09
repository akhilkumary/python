from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

tim.shape('turtle')
tim.color('orange')

for _ in range(0, 4):
    tim.forward(100)
    tim.left(90)

screen.exitonclick()