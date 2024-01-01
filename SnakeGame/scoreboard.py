# Imports
from turtle import Turtle

# Constants
SCOREBOARD_X_COORDINATES = 0
SCOREBOARD_Y_COORDINATES = 270
SCOREBOARD_ALIGNMENT = "center"
SCOREBOARD_FONT = ("Arial", 16, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        """Constructor of the ScoreBoard class."""
        super().__init__()
        self.score = 0
        self.highscore = self.read_highscore()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.setposition(SCOREBOARD_X_COORDINATES, SCOREBOARD_Y_COORDINATES)
        self.update_scoreboard()

    def add_score(self):
        """Responsible for incrementing the score and display it."""
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        """Responsible for displaying the score."""
        self.clear()
        self.write(arg=f"Score: {self.score} High score: {self.highscore}", align=SCOREBOARD_ALIGNMENT, font=SCOREBOARD_FONT)

    def reset(self):
        """Responsible for resetting the game. Handle the score and the highscore."""
        if self.score > self.highscore:
            self.highscore = self.score
            self.write_highscore(self.highscore)
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     """Responsible for printing the game over text."""
    #     self.setposition(0, 0)
    #     self.color("red")
    #     self.write(arg="GAME OVER", align=SCOREBOARD_ALIGNMENT, font=SCOREBOARD_FONT)

    def read_highscore(self):
        """Responsible for reading the highscore from the file and return the integer."""
        with open("data.txt", mode="r") as file:
            return int(file.read())

    def write_highscore(self, new_highscore):
        """Responsible for writing the new highscore to the file."""
        with open("data.txt", mode="w") as file:
            file.write(str(new_highscore))
