# Imports
from turtle import Turtle, Screen

# Turtle object
tim = Turtle()
tim.shape("turtle")


def move_forward():
    """Move turtle forward by 10."""
    tim.forward(10)


def move_backward():
    """Move turtle backward by 10."""
    tim.backward(10)


def turn_clockwise():
    """Turn turtle clockwise by angle 10."""
    tim.right(10)
    # tim.setheading(tim.heading() + 10)


def turn_anti_clockwise():
    """Turn turtle anti-clockwise by angle 10."""
    tim.left(10)
    # tim.setheading(tim.heading() - 10)


def clear_screen():
    """Reset the screen."""
    screen.reset()


# Screen object
screen = Screen()
# Start listening
screen.listen()

# Set event
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=turn_clockwise)
screen.onkey(key="a", fun=turn_anti_clockwise)
screen.onkey(key="c", fun=clear_screen)

# Set exit on click
screen.exitonclick()
