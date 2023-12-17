# Imports
from turtle import Turtle, Screen

# Create a turtle object
turtle_obj = Turtle()

# Modify the object attributes
turtle_obj.shape("turtle")
turtle_obj.color("chartreuse3")

# Trigger behavior
turtle_obj.forward(100)

# Display
screen_obj = Screen()
screen_obj.exitonclick()

# ---------------------------------------------------------------------------------------------------------------------

# Imports
from prettytable import PrettyTable

# Create table object
table = PrettyTable()

# Add columns to the table
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

# Change attributes (Left align)
table.align = "l"

# Printing the table
print(table)

