import turtle
import random

# Define constants
TOP_EDGE = 290
BOTTOM_EDGE = -290
LEFT_EDGE = -385
RIGHT_EDGE = 385

STARTING_POSITION_1 = (0, 300)
STARTING_POSITION_2 = (0, -300)
SPEED = "fastest"
HEADING_UP = 90
HEADING_DOWN = 270
HEADING_LEFT = 180
HEADING_RIGHT = 0

TOP_EDGE_ANGLE = 0
BOTTOM_EDGE_ANGLE = 180
LEFT_EDGE_ANGLE = 90
RIGHT_EDGE_ANGLE = -90


class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(1)
        self.penup()
        self.color('white')
        self.speed(SPEED)
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.random_direction()

    def random_direction(self):
        """
        return a random vector to start the pong game with
        """
        self.setheading(random.randint((-180), 180))

    def check_bounce(self):
        """
        make ball bounce_y from top or bottom
        """
        y = self.ycor()
        x = self.xcor()
        if y >= TOP_EDGE or y <= BOTTOM_EDGE:
            self.bounce_y()

    def bounce_y(self):
        """
        change ball direction
        """
        self.y_move *= -1

    def bounce_x(self):
        """
        change ball direction after paddle
        """
        self.x_move *= -1

    def ball_move(self):
        """
        define continuous ball movement
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()

