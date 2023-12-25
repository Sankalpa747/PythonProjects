# Imports
from turtle import Turtle


class Line(Turtle):

    def __init__(self, screen_height):
        """Constructor of the Line class."""
        super().__init__()
        self.hideturtle()
        self.speed("fastest")
        self.color("white")
        self.penup()
        self.goto(0, -300)
        for num in range(int(screen_height / 10)):
            if num % 2 == 0:
                self.pendown()
            else:
                self.penup()
            self.goto(0, self.ycor() + 10)
