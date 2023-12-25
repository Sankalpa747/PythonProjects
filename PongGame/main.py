# Imports
from turtle import Screen
from paddle import Paddle
from ball import Ball
from line import Line
from scoreboard import Scoreboard
import time

# Constants
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
STARTING_X_COORDINATES_LEFT = -((SCREEN_WIDTH / 2) - 20)
STARTING_X_COORDINATES_RIGHT = ((SCREEN_WIDTH / 2) - 20)
STARTING_Y_COORDINATES = 0

# Create the screen and configure
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Pong Arcade Game")
screen.bgcolor("black")
# Turn off the automatic update (Should call the update method manually)
screen.tracer(0)

# Draw the middle line
line = Line(SCREEN_HEIGHT - 40)

# Create pedals
left_paddle = Paddle(STARTING_X_COORDINATES_LEFT, STARTING_Y_COORDINATES)
right_paddle = Paddle(STARTING_X_COORDINATES_RIGHT, STARTING_Y_COORDINATES)

# Key listen configuration
screen.listen()
# Configure the left paddle key events
screen.onkeypress(key="w", fun=left_paddle.move_up)
screen.onkeypress(key="s", fun=left_paddle.move_down)
# Configure the right paddle key events
screen.onkeypress(key="Up", fun=right_paddle.move_up)
screen.onkeypress(key="Down", fun=right_paddle.move_down)

# Create ball
ball = Ball()

# Scoreboard
score = Scoreboard()

hit_count = 1
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()

    # Detect wall collisions
    if ball.ycor() > 280:
        """Top wall hit."""
        ball.bounce_y()
    elif ball.ycor() < -280:
        """Bottom wall hit."""
        ball.bounce_y()

    # Detect paddle collisions
    if ball.distance(left_paddle) < 50 and ball.xcor() < STARTING_X_COORDINATES_LEFT + 30:
        """Left paddle hit."""
        ball.bounce_x()
        score.add_score_l()
        hit_count += 1
    elif ball.distance(right_paddle) < 50 and ball.xcor() > STARTING_X_COORDINATES_RIGHT - 30:
        """Right paddle hit."""
        ball.bounce_x()
        score.add_score_r()
        hit_count += 1

    # Move the ball (Continuous moving)
    ball.move()

    # Detect right paddle miss
    if ball.xcor() > STARTING_X_COORDINATES_RIGHT:
        ball.reset_position()
        score.add_score_l()

    # Detect left paddle miss
    if ball.xcor() < STARTING_X_COORDINATES_LEFT:
        ball.reset_position()
        score.add_score_r()

# Configure to close the screen on click
screen.exitonclick()
