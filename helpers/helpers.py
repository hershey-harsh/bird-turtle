import random
from helpers.colors import colors

def draw_random_angle_quadrilateral(turtle, min_x, max_x, min_y, max_y):
    turtle.color(random.choice(colors))

    if random.choice([True, False]):
        turtle.begin_fill()

    side_lengths = [random.randint(50, 100) for _ in range(4)]

    rotation_angles = [random.randint(0, 360) for _ in range(4)]

    for i in range(4):
        turtle.forward(side_lengths[i])
        turtle.left(rotation_angles[i])

    if random.choice([True, False]):
        turtle.end_fill()

    turtle.penup()
    turtle.goto(random.uniform(min_x, max_x), random.uniform(min_y, max_y))
    turtle.pendown()
