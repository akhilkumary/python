from turtle import Turtle, Screen

STEP_SIZE = 1

def move_forward():
    tim.fd(STEP_SIZE)

def move_backward():
    tim.backward(STEP_SIZE)

def move_clockwise():
    tim.right(1)
    tim.fd(STEP_SIZE)

def move_anti_clockwise():
    tim.left(1)
    tim.fd(STEP_SIZE)

def clear_screen():
    tim.reset()

screen = Screen()
tim = Turtle()

tim.speed('fastest')
tim.shape('turtle')

screen.listen()

screen.onkeypress(key='w', fun=move_forward)
screen.onkeypress(key='s', fun=move_backward)
screen.onkeypress(key='a', fun=move_clockwise)
screen.onkeypress(key='d', fun=move_anti_clockwise)
screen.onkeypress(key='c', fun=clear_screen)

screen.exitonclick()