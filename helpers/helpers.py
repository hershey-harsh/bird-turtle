import random

def draw_random_angle_quadrilateral(turtle, min_x, max_x, min_y, max_y):
    turtle.color(random.random(), random.random(), random.random())
    turtle.begin_fill()
    
    side_lengths = [random.randint(50, 100) for _ in range(4)]
    rotation_angles = [random.randint(0, 360) for _ in range(4)]

    for i in range(4):
        turtle.forward(side_lengths[i])
        turtle.left(rotation_angles[i])

    turtle.end_fill()

    turtle.penup()
    turtle.goto(random.uniform(min_x, max_x), random.uniform(min_y, max_y))
    turtle.pendown()