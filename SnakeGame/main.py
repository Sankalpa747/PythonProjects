# Imports
from turtle import Screen
from snake import Snake
import time

# Constants
SNAKE_INITIAL_SEGMENT_COUNT = 3
SNAKE_SEGMENT_SIZE = 20
SNAKE_MOVE_SLEEP_TIME = 0.2

# Initiate the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
# Screen does not update until the update() is triggered everytime
screen.tracer(0)

# Create snake
snake = Snake()

# Start listening for keys
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True
while game_is_on:
    """Update the screen, delay a short time and move snake segments."""
    screen.update()
    time.sleep(SNAKE_MOVE_SLEEP_TIME)
    snake.move()

# Screen exist on click
screen.exitonclick()
