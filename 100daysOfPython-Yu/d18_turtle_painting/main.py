import turtle
import random

phil_turtle = turtle.Turtle()
phil_turtle.shape('classic')
phil_turtle.color('red2')


# # turtle square
# for x in range(4):
#     blue_turtle.forward(100)
#     blue_turtle.right(90)

# # draw dashed line: line 10 gap 10 repeat 50 times
# for x in range(15):
#     blue_turtle.forward(10)
#     blue_turtle.penup()
#     blue_turtle.forward(10)
#     blue_turtle.pendown()

# Draw triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon in sequence
# from the same starting position
# changing to a random color for each row

# counter = 0
# distance = 100
# shapes = [
#     {'shape': 'triangle',
#      'sides': 3,
#      'angles': 120},
#     {'shape': 'square',
#      'sides': 4,
#      'angles': 90},
#     {'shape': 'pentagon',
#      'sides': 5,
#      'angles': 72},
#     {'shape': 'hexagon',
#      'sides': 6,
#      'angles': 60},
#     {'shape': 'heptagon',
#      'sides': 7,
#      'angles': 51 + 3/7},
#     {'shape': 'octagon',
#      'sides': 8,
#      'angles': 45},
#     {'shape': 'nonagon',
#      'sides': 9,
#      'angles': 40},
#     {'shape': 'decagon',
#      'sides': 10,
#      'angles': 36}
# ]
# color = f'#{random.randrange(256**3):06x}'
#
# while counter < 8:
#     color = f'#{random.randrange(256 ** 3):06x}'
#     blue_turtle.color(color)
#
#     for y in range(shapes[counter].get('sides')):
#         blue_turtle.forward(distance)
#         blue_turtle.right(shapes[counter].get('angles'))
#     counter += 1

# Random Walk: (my V.1)
# increase thickness of the line
# each distance is equal to the ones before
# increase speed of turtle
# random color for each random move

# is_running = True
# blue_turtle.speed(30)
# blue_turtle.pensize(3)
#
# while is_running:
#     direction = random.randint(1,4)
#     color = f'#{random.randrange(256**3):06x}'
#     blue_turtle.color(color)
#
#     if direction == 1:
#         continue
#     elif direction == 2:
#         blue_turtle.right(180)
#     elif direction == 3:
#         blue_turtle.right(90)
#     elif direction == 4:
#         blue_turtle.left(90)
#     blue_turtle.forward(15)


# direction = [0, 90, 180, 270]
# blue_turtle.speed(30)
# blue_turtle.pensize(3)
#
# for _ in range(400):
#     color = f'#{random.randrange(256 ** 3):06x}'
#     blue_turtle.color(color)
#
#     blue_turtle.forward(15)
#     blue_turtle.setheading(random.choice(direction))
#
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#
#     random_color = (r, g, b)
#     return random_color


# Make Spirograph: V.1
# e.g from pos(0) create a circle with diameter of x
# then move a little/ add a degree until 360
# also in random color

def draw_spirograph(size_of_gap: float):
    phil_turtle.speed("fastest")
    angle = 0

    for _ in range(int(360 / size_of_gap)):
        color = f'#{random.randrange(256 ** 3):06x}'
        phil_turtle.color(color)

        phil_turtle.circle(100)
        phil_turtle.left(angle)
        angle += size_of_gap


draw_spirograph(10)

# must be at the end of the Code to visualize, else returns empty screen
screen = turtle.Screen()
screen.exitonclick()
