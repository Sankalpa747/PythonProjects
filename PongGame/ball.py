# Imports
from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        """Constructor of the Ball."""
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("white")
        self.penup()
        self.speed("fast")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """Responsible for moving the ball."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Responsible for handling the ball bounce with top and bottom walls."""
        self.y_move *= -1

    def bounce_x(self):
        """Responsible for handling the ball bounce with paddles."""
        self.x_move *= -1
        # Increase the speed of the ball move
        self.move_speed *= 0.9

    def reset_position(self):
        """Rest the ball position."""
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.1
