import turtle

STARTING_POSITION_1 = (-350, 0)
STARTING_POSITION_2 = (350, 0)
SPEED = 0
HEADING_UP = 90
HEADING_DOWN = 270


class Racket(turtle.Turtle):
    """
    position left of right to create racket 1( left ) and 2 ( right )
    """

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.shapesize(1, 4)
        self.penup()
        self.color('white')
        self.speed(SPEED)
        self.setheading(HEADING_UP)

        if position == 'left':
            self.goto(STARTING_POSITION_1)
        elif position == 'right':
            self.goto(STARTING_POSITION_2)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
