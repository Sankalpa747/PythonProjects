# Imports
from turtle import Turtle
import random

# Constants
MAX_COORDINATE_BOUND_POSITIVE = 280
MAX_COORDINATE_BOUND_NEGATIVE = -280


class Food(Turtle):

    def __init__(self):
        """Constructor of the Food class."""
        super().__init__()
        # Since inherited from the turtle class, now we can modify turtle class properties
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def generate_random_coordinate(self):
        """Responsible for generating random coordinates."""
        return random.randint(MAX_COORDINATE_BOUND_NEGATIVE, MAX_COORDINATE_BOUND_POSITIVE)

    def refresh(self):
        """Responsible for relocating the food."""
        self.goto(self.generate_random_coordinate(), self.generate_random_coordinate())
