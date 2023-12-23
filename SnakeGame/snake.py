# Imports
from turtle import Turtle

# Constants
SNAKE_INITIAL_SEGMENT_COUNT = 3
SNAKE_SEGMENT_SIZE = 20
SNAKE_MOVE_DISTANCE = 20
UP_DIRECTION = 90
DOWN_DIRECTION = 270
LEFT_DIRECTION = 180
RIGHT_DIRECTION = 0


class Snake:

    def __init__(self):
        """Constructor of the Snake class."""
        self.segments = []
        self.create_initial_snake()
        self.snake_head = self.segments[0]

    def create_initial_snake(self):
        """Responsible for creating the initial snake segments."""
        for n in range(SNAKE_INITIAL_SEGMENT_COUNT):
            """Create the initial snake segments."""
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            if n != 0:
                """From the second segment onwards, append other body parts after it."""
                previous_segment = self.segments[n - 1]
                segment.setposition(previous_segment.xcor() - SNAKE_SEGMENT_SIZE, 0)
            self.segments.append(segment)

    def move(self):
        """Responsible for moving the snake."""
        # for n in range(len(segments) - 1, 0, -1):
        for seg_num in reversed(range(len(self.segments))):
            if seg_num > 0:
                """Get the next segment and move into that position."""
                next_segment = self.segments[seg_num - 1]
                x_cor = next_segment.xcor()
                y_cor = next_segment.ycor()
                self.segments[seg_num].setposition(x_cor, y_cor)
            else:
                """The snake head element moves front."""
                self.snake_head.forward(SNAKE_MOVE_DISTANCE)

    def up(self):
        """Turn the snake angle 90."""
        if self.snake_head.heading() != DOWN_DIRECTION:
            self.snake_head.setheading(UP_DIRECTION)

    def down(self):
        """Turn the snake angle 270."""
        if self.snake_head.heading() != UP_DIRECTION:
            self.snake_head.setheading(DOWN_DIRECTION)

    def left(self):
        """Turn the snake angle 180."""
        if self.snake_head.heading() != RIGHT_DIRECTION:
            self.snake_head.setheading(LEFT_DIRECTION)

    def right(self):
        """Turn the snake angle 0."""
        if self.snake_head.heading() != LEFT_DIRECTION:
            self.snake_head.setheading(RIGHT_DIRECTION)
