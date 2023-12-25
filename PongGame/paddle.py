# Imports
from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_coordinates, y_coordinates):
        """Constructor of the Paddle."""
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.goto(x_coordinates, y_coordinates)

    def move_up(self):
        """Responsible for moving the paddle up."""
        if self.ycor() < 260:
            self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        """Responsible for moving the paddle down."""
        if self.ycor() > -260:
            self.goto(self.xcor(), self.ycor() - 20)
