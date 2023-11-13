import turtle
import random
from config import min_x, max_x, min_y, max_y, bgcolor, speed
from helpers.helpers import draw_random_angle_quadrilateral

screen = turtle.Screen()
screen.bgcolor(bgcolor)

turtle.speed(int(speed))

while turtle.xcor() < max_x and turtle.ycor() < max_y:
    draw_random_angle_quadrilateral(turtle, min_x, max_x, min_y, max_y)

turtle.hideturtle()
turtle.done()
