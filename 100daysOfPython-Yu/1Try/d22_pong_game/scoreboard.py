import turtle

DASHES = 50
DASH_STEPS_VISIBLE = 9
DASH_STEPS_INVISIBLE = 16
DASH_PENSIZE = 5
MOVEMENT = False
ALIGNMENT = "center"
FONT = ("Courier", 15, "bold")


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score_1 = 0
        self.score_2 = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0, 280)

    def dashed_line(self):
        """
        creates a dashed line, separating each side of the board
        """
        self.setheading(270)
        self.speed('fastest')
        self.pensize(DASH_PENSIZE)
        amount_dashes = 0
        while amount_dashes < DASHES:
            self.pendown()
            self.forward(DASH_STEPS_VISIBLE)
            self.penup()
            self.forward(DASH_STEPS_INVISIBLE)
            amount_dashes += 1

    def display(self):
        """
        update the scoreboard
        """
        self.clear()
        self.write(f"{self.score_1} : {self.score_2}", MOVEMENT, ALIGNMENT, FONT)

    def increase_score(self, player_side):
        """
        increases the score of the respective player side
        """
        if player_side == 'left':
            self.score_1 += 1
        elif player_side == 'right':
            self.score_2 += 1

    def print_game_over(self):
        """
        prints game over
        """
        self.goto(0, 0)
        self.write(f"GAME OVER", MOVEMENT, ALIGNMENT, FONT)
