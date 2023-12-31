# Imports
from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManger
import time

# Constants
SCREEN_UPDATE_DELAY = 0.2
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
PLAYER_SCORE_YCOR = 300

# Create the screen
screen = Screen()
screen.title("Turtle Crossing Game")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
# Set auto update disabled
screen.tracer(0)

# Create player
player = Player()

# Create scoreboard
scoreboard = Scoreboard()

# Create car manager
car_manager = CarManger()

# Key events
screen.listen()
screen.onkeypress(key="Up", fun=player.move_forward)

is_game_on = True
while is_game_on:
    # Screen updates
    time.sleep(SCREEN_UPDATE_DELAY)
    screen.update()

    # Continuously move the cars
    car_manager.move_cars()

    if player.ycor() > PLAYER_SCORE_YCOR:
        player.reset()
        scoreboard.add_score()
        car_manager.increase_speed()

    if car_manager.is_hit(player.pos()):
        scoreboard.game_over()
        is_game_on = False

# Close the screen on click
screen.exitonclick()
