from turtle import Turtle

MOVEMENT = False
ALIGNMENT = "center"
FONT = ("Courier", 15, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.high_score = self.read_highscore()
        self.data_highscore = None
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0, 270)

    def read_highscore(self):
        with open('data.txt', 'r') as data_file:
            self.high_score = int(data_file.read())
        return self.high_score

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", MOVEMENT, ALIGNMENT, FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", 'w+') as data_file:
                data_file.write(f'{self.high_score}')
        self.score = 0
        self.update_scoreboard()
