import colorgram
import turtle
import random

turtle.colormode(255)

phil_turtle = turtle.Turtle()
phil_turtle.shape('classic')

# rgb_colors = []
# colors = colorgram.extract('damien_hirst_spot.webp',10)
#
# for color in colors:
#     r = color.rgb[0]
#     g = color.rgb[1]
#     b = color.rgb[2]
#     new_rgb_color = (r, g, b)
#     rgb_colors.append(new_rgb_color)
#
# print(rgb_colors)

# paint a paining with a 10x10 rows of spots
# each dot size 20 and distance 50
# choose a random rgb color from list
colors = [(241, 246, 243), (247, 239, 242), (135, 164, 199), (223, 151, 105), (31, 44, 63), (200, 137, 148), (160, 61, 51), (235, 212, 93)]

phil_turtle.speed('fastest')

y = 0
x = 0

for i in range(10):

    phil_turtle.teleport(x, y)
    for j in range(10):
        phil_turtle.penup()
        phil_turtle.hideturtle()
        rgb_color = (random.choice(colors))
        phil_turtle.color(rgb_color)

        phil_turtle.dot(20,rgb_color)
        # blue_turtle.begin_fill()
        # blue_turtle.circle(10)
        # blue_turtle.end_fill()
        #blue_turtle.penup()
        phil_turtle.forward(50)
        #blue_turtle.pendown()
    y += 50



#keep at end of Code
screen = turtle.Screen()
screen.exitonclick()