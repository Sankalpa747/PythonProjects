# Imports
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Constants
SNAKE_INITIAL_SEGMENT_COUNT = 3
SNAKE_SEGMENT_SIZE = 20
SNAKE_MOVE_SLEEP_TIME = 0.1
SNAKE_FOOD_COLLISION_DISTANCE = 15

# Initiate the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
# Screen does not update until the update() is triggered everytime
screen.tracer(0)

# Create snake
snake = Snake()

# Create food
food = Food()

# Create scoreboard
scores = Scoreboard()

# Start listening for keys
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True
while game_is_on:
    """Update the screen with a short delay time and move snake segments."""
    screen.update()
    time.sleep(SNAKE_MOVE_SLEEP_TIME)
    snake.move()

    if snake.snake_head.distance(food) < SNAKE_FOOD_COLLISION_DISTANCE:
        """Snake head goes near the food and consume the food."""
        food.refresh()
        scores.add_score()
        snake.add_segment()

    if snake.is_collision():
        scores.game_over()
        game_is_on = False


# Screen exist on click
screen.exitonclick()
