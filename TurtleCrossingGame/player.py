# Imports
from turtle import Turtle

# Constant
PLAYER_START_POSITION = (0, -280)
PLAYER_HEADING = 90
PLAYER_MOVE_DISTANCE = 10


class Player(Turtle):

    def __init__(self):
        """Constructor of the Player class."""
        super().__init__()
        self.hideturtle()
        self.shape("turtle")
        self.speed("fastest")
        self.penup()
        self.goto(PLAYER_START_POSITION)
        self.setheading(PLAYER_HEADING)
        self.showturtle()
        self.color("white")

    def move_forward(self):
        """Responsible for moving the player forward."""
        self.goto(self.xcor(), self.ycor() + PLAYER_MOVE_DISTANCE)

    def reset(self):
        """Responsible for resetting the turtle."""
        self.hideturtle()
        self.goto(PLAYER_START_POSITION)
        self.showturtle()
