# Imports
import turtle
import pandas

# Constants
IMAGE_NAME = "./blank_states_img.gif"
STATE_COLUMN = "state"
X_COLUMN = "x"
Y_COLUMN = "y"

# The screen
screen = turtle.Screen()

# Screen configuration
screen.title("US States Game")
# Loading an image as a new image
screen.addshape(IMAGE_NAME)
# Then add that loaded image to turtle
turtle.shape(IMAGE_NAME)

# Arrange the data (Loading to the data frame)
data = pandas.read_csv("./50_states.csv")
# List of states
states_list = data.state.to_list()

# Array holding already founded states
found_states = []

is_game_on = True
while is_game_on:
    # Prompt the user for state name input
    answer_state = screen.textinput(title=f"{len(found_states)}/{len(data)} Stats Correct", prompt="What's another state's name?")
    if answer_state is not None and answer_state.lower() != "exit":
        # Check for the user entered state (Case ignored)
        # state = data[data["state"].str.contains(answer_state, case=False)]
        # Check for the user entered state (Title case)
        state = data[data["state"] == answer_state.title()]
        if not state.empty:
            state_name = str(state["state"].item())
            if state_name not in found_states:
                found_states.append(state_name)
                new_state = turtle.Turtle()
                new_state.penup()
                new_state.hideturtle()

                # Obtain the coordinates
                # x = int(state["x"].iloc[0])
                # y = int(state["y"].iloc[0])
                # x = int(state.x)
                # y = int(state.y)
                x = int(state["x"].item())
                y = int(state["y"].item())

                new_state.goto(x, y)
                new_state.write(arg=state_name, align="left", font=("Arial", 8, "normal"))
            else:
                print(f"Already entered state: {state_name}")

        else:
            print(f"Incorrect state name: {answer_state}")

    elif answer_state is None or answer_state.lower() == "exit":
        print(f"Use cancelled/exit")
        is_game_on = False

        # Generate report
        # Create the missing states list
        # states_to_learn = [state for state in states_list if state not in found_states]
        states_to_learn = []
        for state in states_list:
            if state not in found_states:
                states_to_learn.append(state)

        # Create a dictionary of missing states
        state_dict = {
            "states": states_to_learn
        }

        # Create a data frame of missing states and export it as a .csv file
        print_df = pandas.DataFrame(state_dict)
        print_df.to_csv("./report.csv")

    # Set game exit logic
    if len(data) == len(found_states):
        print("All states are found, Congratulations!")
        is_game_on = False

# Keep the screen open
turtle.mainloop()
