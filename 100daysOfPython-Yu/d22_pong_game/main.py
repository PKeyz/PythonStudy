import time
from turtle import Screen
import racket
import scoreboard
import ball

MAX_ROUNDS = 10

y = range(-300, 300)
x = range(-400, 400)

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("My Pong Game")
screen.tracer(0)

# create classes here
scoreboard_dashed = scoreboard.Scoreboard()
scoreboard = scoreboard.Scoreboard()
racket_l = racket.Racket('left')
racket_r = racket.Racket('right')
ball = ball.Ball()

screen.listen()

screen.onkeypress(racket_l.move_up, "w")
screen.onkeypress(racket_l.move_down, "s")
screen.onkeypress(racket_l.move_up, "W")
screen.onkeypress(racket_l.move_down, "S")
screen.onkeypress(racket_r.move_up, "Up")
screen.onkeypress(racket_r.move_down, "Down")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    scoreboard_dashed.dashed_line()

    ball.random_direction()
    ball.ball_move()
    ball.check_bounce()

    #Detect collision with paddle
    if (ball.distance(racket_l) < 50 and ball.xcor() < -320) or (ball.distance(racket_r) < 50 and ball.xcor() > 320):
        ball.bounce_x()

    if ball.xcor() <= -400:
        scoreboard.increase_score('right')
        racket_r.racket_increase_score()
        ball.reset_position()
    elif ball.xcor() >= 400:
        scoreboard.increase_score('left')
        racket_l.racket_increase_score()
        ball.reset_position()

    if racket_l.score == 10 or racket_r.score == 10:
        scoreboard.print_game_over()
        is_game_on = False

    scoreboard.display()

screen.exitonclick()
