import turtle

MOVEMENT = False
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(-210, 270)

    def display(self):
        self.clear()
        self.write(f"Level: {self.score}", MOVEMENT, ALIGNMENT, FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER\nLevel: {self.score}", MOVEMENT, ALIGNMENT, FONT)

    def increment_score(self):
        self.score += 1
