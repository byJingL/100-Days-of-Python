# import colorgram
# Todo: Extract from painting, create a color list
# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = []
# for color in colors:
#     color_rgb = (color.rgb.r, color.rgb.g, color.rgb.b)
#     rgb_colors.append(color_rgb)
# print(rgb_colors)

import turtle as t
import random

t.colormode(255)
color_list = [(54, 108, 149), (225, 201, 108), (134, 85, 58), (224, 141, 62),
              (197, 144, 171), (143, 180, 206), (137, 82, 106), (210, 90, 68),
              (232, 226, 194), (188, 78, 122), (69, 101, 86), (132, 183, 132),
              (65, 156, 86), (137, 132, 74), (48, 155, 195), (183, 191, 202),
              (232, 221, 225), (58, 47, 41), (47, 59, 96), (38, 44, 64),
              (106, 46, 54), (41, 55, 48), (12, 104, 95), (118, 125, 145),
              (182, 194, 199), (215, 176, 187), (223, 178, 168), (54, 45, 52)]

tom = t.Turtle()
tom.penup()
tom.hideturtle()
line_of_dots = 10
for i in range(line_of_dots):
    tom.setposition(-200, -200 + 40 * i)
    for _ in range(line_of_dots):
        tom.dot(20, random.choice(color_list))
        tom.forward(40)


screen = t.Screen()
screen.exitonclick()
