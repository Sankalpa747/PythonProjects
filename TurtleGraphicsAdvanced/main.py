# Imports
from turtle import Turtle, Screen, colormode
import random

# Initiate the turtle
turtle = Turtle()
turtle.shape("turtle")
turtle.color("green")

# Turtle art

# 1
# Draw Square
# for _ in range(4):
#     turtle.forward(100)
#     turtle.right(90)


# 2
# Draw dashed line
# is_pen_down = True
# for _ in range(30):
#     if is_pen_down:
#         turtle.pendown()
#     else:
#         turtle.penup()
#     turtle.forward(10)
#     is_pen_down = not is_pen_down
# Alternative solution
# for _ in range(10):
#     turtle.pendown()
#     turtle.forward(10)
#     turtle.penup()
#     turtle.forward(10)


# 3
# Drawing different shapes
# total_angle = 360
# colors = ["GreenYellow", "DarkOrchid", "Blue", "Gold", "Red", "Cyan", "Black", "Yellow"]
#
#
# def draw_shape(number_of_sides):
#     """Draw shapes based on the sides."""
#     angle = total_angle / number_of_sides
#     turtle.color(random.choice(colors))
#     for _ in range(number_of_sides):
#         turtle.forward(100)
#         turtle.right(angle)
#
#
# for sides in range(3, 10):
#     draw_shape(sides)


# 4
# Drawing a random walk
# FORWARD = 30
# LEFT = "left"
# RIGHT = "right"
# angles = [0, 90, 180, 270]
# directions = [LEFT, RIGHT]
#
#
# def random_color():
#     """Generate random RGB colors tuple and return."""
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color
#
#
# def walk(direction, angle):
#     """Responsible for controlling the turtle with the given properties."""
#     turtle.color(random_color())
#     turtle.pensize(15)
#     turtle.speed("fastest")
#     turtle.forward(FORWARD)
#     if direction == LEFT:
#         turtle.left(angle)
#     else:
#         turtle.right(angle)
#     # Alternatively for calling left() or right()
#     # turtle.setheading(angle)
#
#
# # Calling turtle color mode function
# colormode(255)
# for _ in range(300):
#     walk(random.choice(directions), random.choice(angles))


# 5
# Draw a Spirograph
turtle.speed("fastest")
colormode(255)


def random_color():
    """Generate random RGB colors tuple and return."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(size_of_gap):
    """Draw spirograph."""
    for _ in range(int(360 / size_of_gap)):
        turtle.color(random_color())
        turtle.circle(100)
        turtle.setheading(turtle.heading() + size_of_gap)


# Draw spirograph
draw_spirograph(5)


# Screen configuration
screen = Screen()
screen.exitonclick()

