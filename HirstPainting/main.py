# Imports
import colorgram

# # Attributes
# rgb_colors = []
#
# # Extract colors
# colors = colorgram.extract('hirst_paint.jpg', 108)
#
# # Extract the RGB colors
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

# --------------------------------------------------------------------------------------------------------------------

# Imports
from turtle import Turtle, Screen, colormode
import random

# Attributes
color_list = [(252, 248, 242), (190, 16, 63), (11, 115, 178), (236, 142, 72), (245, 218, 75), (170, 44, 109),
              (40, 50, 120), (231, 123, 159), (228, 53, 107), (184, 223, 239), (231, 76, 59), (61, 170, 77),
              (224, 241, 235), (109, 169, 214), (121, 192, 147), (127, 75, 44), (151, 210, 220), (216, 155, 4),
              (10, 141, 58), (254, 226, 0), (3, 176, 210), (21, 99, 47), (15, 54, 101), (118, 42, 34), (253, 236, 243),
              (70, 77, 41), (2, 80, 53), (150, 207, 202), (238, 163, 185), (237, 170, 160), (182, 185, 217),
              (115, 117, 163), (1, 77, 124), (86, 27, 72), (48, 34, 34)]

# Turtle object
turtle_obj = Turtle()
turtle_obj.speed("fastest")
turtle_obj.penup()
colormode(255)
turtle_obj.hideturtle()

# Starting positions
x_start_position = -225
y_start_position = -225

# Set the initial position to the bottom left of the screen
turtle_obj.setposition(x_start_position, y_start_position)

for _ in range(10):
    """Iterate per each line."""
    for _ in range(10):
        """Iterate per each dot."""
        turtle_obj.dot(20, random.choice(color_list))
        turtle_obj.fd(50)
    # Update the 'y' position
    y_start_position += 50
    # Bring the turtle to the starting point of the next row
    turtle_obj.setposition(x_start_position, y_start_position)

# Screen object
screen = Screen()
screen.exitonclick()
