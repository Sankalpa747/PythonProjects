# Imports
from turtle import Turtle

# Constants
SCOREBOARD_START_POSITION = (-240, 260)
SCOREBOARD_ALIGNMENT = "center"
SCOREBOARD_FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        """Constructor of the Scoreboard class."""
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.goto(SCOREBOARD_START_POSITION)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        """Responsible for updating the scoreboard."""
        self.clear()
        self.write(arg=f"Level: {self.level}", align=SCOREBOARD_ALIGNMENT, font=SCOREBOARD_FONT)
        pass

    def add_score(self):
        """Responsible for updating the levels to the scoreboard."""
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """Responsible for printing the game over text."""
        self.setposition(0, 0)
        self.color("red")
        self.write(arg="GAME OVER", align=SCOREBOARD_ALIGNMENT, font=SCOREBOARD_FONT)
