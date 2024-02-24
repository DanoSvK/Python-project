import colorgram
import random
import turtle as t
from turtle import Screen
colors = colorgram.extract('spot-colors.jpg', 20)
colors_list = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    colors_list.append((r, g, b))
print(colors_list)
rgb_colors = [(250, 247, 244), (248, 245, 246), (213, 154, 96), (52, 107, 132), (179, 77, 31), (202, 142, 31),
              (115, 155, 171), (124, 79, 99), (122, 175, 156), (229, 236, 239), (226, 198, 131), (242, 247, 244),
              (192, 87, 108), (11, 50, 64), (55, 38, 19), (45, 168, 126), (47, 127, 123), (200, 121, 143),
              (168, 21, 29), (228, 92, 77)]

my_screen = Screen()

print(my_screen.screensize())


def draw_spots(size):
    iterations = 0
    y = -200
    draw = True
    t.speed(20)
    while draw:
        x = -200
        t.teleport(x, y)
        for _ in range(size):
            random_color = random.choice(rgb_colors)
            t.colormode(255)
            t.color(random_color)
            t.begin_fill()
            t.circle(20)
            t.end_fill()
            t.penup()
            t.forward(50)
            t.pendown()
        y += 50
        iterations += 1
        if iterations == 10:
            draw = False


draw_spots(10)


my_screen.exitonclick()
