import colorgram
import turtle as t
import random

color_extract = colorgram.extract('spot_hirst.jpg', 35)

def random_color(colors):
    col = random.choice(colors)
    r = col.rgb.r
    g = col.rgb.g
    b = col.rgb.b
    color = (r, g, b)
    return color

def draw_hirst_painting(colors):
    circle_radius = 8
    gap = 6
    num_dots = 10
    start_x = -((num_dots/2)*circle_radius - circle_radius + (num_dots/2) * gap * circle_radius - (gap/2) * circle_radius)
    start_y = -((num_dots/2)*circle_radius - circle_radius + (num_dots/2) * gap * circle_radius - (gap/2) * circle_radius)
    margin = 2* circle_radius * gap
    screen.setup(-2*start_x + margin, -2*start_y + margin, None, 50)
    for i in range(num_dots):
        start_pos_x = start_x
        start_pos_y = start_y + i * gap * circle_radius
        tim.penup()
        tim.setposition(start_pos_x, start_pos_y)
        for x in range(num_dots):
            tim.pendown()
            tim.color(random_color(color_extract))
            tim.begin_fill()
            tim.circle(circle_radius)
            tim.end_fill()
            tim.penup() 
            tim.fd(gap*circle_radius)

screen = t.Screen()
tim = t.Turtle()

screen.title('Hirst Painting')
t.colormode(255)
tim.speed('fastest')
tim.shape('turtle')

draw_hirst_painting(color_extract)

tim.hideturtle()

screen.exitonclick()