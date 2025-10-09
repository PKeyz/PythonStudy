import turtle
import random

# keep last to visualize the actions properly
screen = turtle.Screen()
screen.setup(width=500, height=450)

# turtle_names = ['blue_turtle', 'green_turtle', 'yellow_turtle', 'red_turtle', 'black_turtle']
turtles_lst = []

start = -250
end_state = 230
max_step = 30

# short version for creating multiple objects from Udemy:
# colors = ['red','blue',....,]
# y_positions = [-70, -30, 10, 50, ...]
#
# for turtle_index in range(0, 6):
#     tim = turtle.Turtle(shape='turtle')
#     tim.penup()
#     tim.goto(x=start, y= y_positions[turtle_index])

blue_turtle = turtle.Turtle('turtle', 0, True)
blue_turtle.color('blue')
blue_turtle.penup()
blue_turtle.setpos(start, 110)
turtles_lst.append(blue_turtle)

green_turtle = turtle.Turtle('turtle', 0, True)
green_turtle.color('green')
green_turtle.penup()
green_turtle.setpos(start, 70)
turtles_lst.append(green_turtle)

yellow_turtle = turtle.Turtle('turtle', 0, True)
yellow_turtle.color('yellow')
yellow_turtle.penup()
yellow_turtle.setpos(start, 30)
turtles_lst.append(yellow_turtle)

red_turtle = turtle.Turtle('turtle', 0, True)
red_turtle.color('red')
red_turtle.penup()
red_turtle.setpos(start, -10)
turtles_lst.append(red_turtle)

black_turtle = turtle.Turtle('turtle', 0, True)
black_turtle.color('black')
black_turtle.penup()
black_turtle.setpos(start, -50)
turtles_lst.append(black_turtle)


user_popup = screen.textinput('TurtleRace', 'Who will win the race? Enter a colour:')

is_game_over = False

while not is_game_over:
    for turtle in turtles_lst:
        turtle.forward(random.randint(0, max_step))
        if turtle.xcor() >= end_state:
            winner_turtle = turtle.color()[0]
            if winner_turtle == user_popup:
                print(f'You Win. The {winner_turtle} turtle is the winner!')
            elif winner_turtle != user_popup:
                print(f'You Loose. The {winner_turtle} turtle is the winner!')
            is_game_over = True
            break

screen.exitonclick()
