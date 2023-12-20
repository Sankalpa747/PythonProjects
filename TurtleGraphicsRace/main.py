# Imports
from turtle import Turtle, Screen
import random

# Screen object
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

# Attributes
is_race_on = False
turtles = []
colors = ["red", "green", "blue", "yellow", "orange", "purple"]
starting_x_coordinate = -230
starting_y_coordinate = -120

for n in range(6):
    """Executes per turtle."""
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.speed("fastest")
    turtle.color(colors[n])
    turtle.goto(starting_x_coordinate, starting_y_coordinate)
    turtles.append(turtle)
    starting_y_coordinate += 50

if user_bet:
    is_race_on = True

winning_x_coordinate = 230

while is_race_on:
    """Executes while the race is over."""
    for turtle in turtles:
        """Execute per turtle until the race is over."""
        random_distance = random.randint(1, 10)
        turtle.forward(random_distance)
        if turtle.xcor() >= winning_x_coordinate:
            if turtle.pencolor() == user_bet:
                print(f"You've won. The {user_bet} turtle is the winner!")
            else:
                print(f"Try again. The {user_bet} turtle is the winner!")
            is_race_on = False

# Set screen close on click
screen.exitonclick()
