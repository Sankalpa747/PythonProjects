# Imports
from turtle import Turtle

# Constants
SCOREBOARD_X_COORDINATES = 0
SCOREBOARD_Y_COORDINATES = 250
SCOREBOARD_ALIGNMENT = "center"
SCOREBOARD_FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        """Constructor of the ScoreBoard class."""
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.setposition(SCOREBOARD_X_COORDINATES, SCOREBOARD_Y_COORDINATES)
        self.update_scoreboard()

    def add_score_l(self):
        """Responsible for incrementing the left score and display it."""
        self.l_score += 1
        self.update_scoreboard()

    def add_score_r(self):
        """Responsible for incrementing the right score and display it."""
        self.r_score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        """Responsible for displaying the score."""
        self.clear()
        self.write(arg=f"{self.l_score} : {self.r_score}", align=SCOREBOARD_ALIGNMENT, font=SCOREBOARD_FONT)

    def game_over(self):
        """Responsible for printing the game over text."""
        self.setposition(0, 0)
        self.color("red")
        self.write(arg="GAME OVER", align=SCOREBOARD_ALIGNMENT, font=SCOREBOARD_FONT)
