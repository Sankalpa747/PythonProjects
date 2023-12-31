# Imports
from turtle import Turtle
import random

# Constants
CAR_STRETCH_WIDTH = 1
CAR_STRETCH_LENGTH = 2.5
CAR_HEADING = 180
CAR_INITIAL_X_COORDINATE = 330
CAR_END_X_COORDINATE = -330
CAR_LANE_TOP_Y_BOUND = 250
CAR_LANE_BOTTOM_Y_BOUND = -230
CAR_LANE_GAP = 70
CAR_COLORS = ("white", "red", "green", "yellow", "violet", "blue", "orange", "brown", "grey", "pink")
PROBABILITY_OF_ADDING_CARS = 0.3
CAR_SPEED_INCREMENTER = 2


class CarManger:

    def __init__(self):
        """Constructor of the CarManger."""
        self.car_pool = []
        self.active_cars = []
        self.car_speed = 10

    def create_car(self):
        """Responsible for creating cars."""
        car = Turtle()
        car.penup()
        car.color(random.choice(CAR_COLORS))
        car.hideturtle()
        car.speed("fastest")
        car.shape("square")
        car.shapesize(stretch_wid=CAR_STRETCH_WIDTH, stretch_len=CAR_STRETCH_LENGTH)
        car.setheading(CAR_HEADING)
        return car

    def update(self):
        """Responsible for updating the car traffic."""
        car = None
        self.handle_cars()

        if len(self.car_pool) == 0:
            """Create a new car."""
            car = self.create_car()
        else:
            """Obtain a car from the car pool."""
            car = self.car_pool.pop()

        # Add the car into the active car list
        self.active_cars.append(car)

        # Configure the new car coordinates
        car_xcor = random.choice(range(CAR_INITIAL_X_COORDINATE + 10, 350))
        car_ycor = random.choice(range(CAR_LANE_BOTTOM_Y_BOUND, CAR_LANE_TOP_Y_BOUND, 5))
        car.goto(car_xcor, car_ycor)

        # Show the car
        car.showturtle()

        print(f"Car pool size: {len(self.car_pool)}")
        print(f"Car active list size: {len(self.active_cars)}")

    def move_cars(self):
        """Responsible for moving active cars forward by 10 pixels."""
        for car in self.active_cars:
            car.goto(car.xcor() - self.car_speed, car.ycor())

        if random.random() < PROBABILITY_OF_ADDING_CARS:
            self.update()

    def handle_cars(self):
        """Responsible for handling the cars. Move active cars into the car-pool based on the screen coordinates."""
        for car in reversed(self.active_cars):
            if car.xcor() < CAR_END_X_COORDINATE:
                """Car has passed the left screen coordinates."""
                self.car_pool.append(car)
                self.active_cars.remove(car)
                car.hideturtle()

    def increase_speed(self):
        """Increase the car speed."""
        self.car_speed += CAR_SPEED_INCREMENTER

    def is_hit(self, player_position):
        """Responsible for verifying whether there is a hit."""
        for car in self.active_cars:
            if car.distance(player_position) < 30:
                return True
        return False
